import json
import logging
from pathlib import Path

from rich.console import Console
from rich.progress import track

from outrich.ai.personalizer import personalize_lead
from outrich.ai.provider import AIProvider
from outrich.ai.qualifier import qualify_lead
from outrich.config import SEGMENT_QUOTAS, Settings
from outrich.db import store
from outrich.sources import apify_linkedin
from outrich.sources.fixture import load_fixture
from outrich.trigger import dry_run
from outrich.report import markdown

logger = logging.getLogger(__name__)
console = Console()


def stage_discover(settings: Settings, source: str, use_cache: bool) -> int:
    store.init_db(settings.db_path)

    if source == "fixture":
        profiles = load_fixture(settings.fixture_path)
    else:
        profiles = apify_linkedin.discover(settings, use_cache=use_cache)

    count = 0
    for p in track(profiles, description="Saving leads..."):
        store.upsert_lead(settings.db_path, p)
        count += 1

    console.print(f"[green]✓ Discovered {count} leads[/green]")
    return count


def stage_qualify(settings: Settings) -> int:
    provider = AIProvider(settings)
    pending = store.get_leads_without_qualification(settings.db_path)

    if not pending:
        console.print("[yellow]All leads already qualified — skipping[/yellow]")
        return 0

    qualified = 0
    for lead in track(pending, description="Qualifying leads..."):
        profile = json.loads(lead["raw_profile"])
        try:
            qual, model_used = qualify_lead(provider, profile)
            store.save_qualification(settings.db_path, lead["id"], qual, model_used)
            qualified += 1
        except Exception as exc:
            logger.error("Failed to qualify lead %d (%s): %s", lead["id"], lead["full_name"], exc)

    console.print(f"[green]✓ Qualified {qualified} leads[/green]")
    return qualified


def stage_select(settings: Settings) -> list[int]:
    all_qualified = store.get_qualified_leads(settings.db_path)

    buckets: dict[str, list] = {seg: [] for seg in SEGMENT_QUOTAS}
    for lead in all_qualified:
        seg = lead["segment"]
        if seg in buckets:
            buckets[seg].append(lead)

    selected_ids: list[int] = []
    for seg, quota in SEGMENT_QUOTAS.items():
        candidates = sorted(buckets[seg], key=lambda r: r["relevance_score"], reverse=True)
        picks = candidates[:quota]
        selected_ids.extend(r["id"] for r in picks)

        if len(picks) < quota:
            console.print(
                f"[yellow]Warning: only {len(picks)}/{quota} leads for segment '{seg}'[/yellow]"
            )

    console.print(f"[green]✓ Selected {len(selected_ids)} leads for outreach[/green]")
    return selected_ids


def stage_personalize(settings: Settings, selected_ids: list[int]) -> int:
    provider = AIProvider(settings)
    to_personalize = store.get_leads_without_messages(settings.db_path, selected_ids)

    if not to_personalize:
        console.print("[yellow]All selected leads already have messages — skipping[/yellow]")
        return 0

    all_qualified = {r["id"]: r for r in store.get_qualified_leads(settings.db_path)}
    drafted = 0

    for lead_id in track(to_personalize, description="Drafting messages..."):
        lead = all_qualified.get(lead_id)
        if not lead:
            continue
        profile = json.loads(lead["raw_profile"])
        qualification = {
            "segment": lead["segment"],
            "relevance_score": lead["relevance_score"],
            "reasoning": lead["reasoning"],
            "scylla_angle": lead["scylla_angle"],
            "pain_points": json.loads(lead["pain_points"] or "[]"),
        }
        try:
            msgs, model_used = personalize_lead(provider, profile, qualification)
            store.save_messages(settings.db_path, lead_id, msgs, model_used)
            drafted += 1
        except Exception as exc:
            logger.error("Failed to personalize lead %d: %s", lead_id, exc)

    console.print(f"[green]✓ Drafted messages for {drafted} leads[/green]")
    return drafted


def stage_trigger(settings: Settings, mode: str = "dry_run") -> int:
    count = dry_run.trigger_all(settings, mode=mode)
    console.print(f"[green]✓ Triggered {count} messages ({mode})[/green]")
    return count


def stage_report(settings: Settings, out_path: Path | None = None) -> Path:
    path = markdown.generate(settings, out_path)
    console.print(f"[green]✓ Report written to {path}[/green]")
    return path


def run_pipeline(
    settings: Settings,
    source: str = "fixture",
    use_cache: bool = True,
    dry_run_mode: bool = True,
    report_path: Path | None = None,
) -> None:
    console.rule("[bold blue]OutRich Pipeline")

    stage_discover(settings, source, use_cache)
    stage_qualify(settings)
    selected = stage_select(settings)
    stage_personalize(settings, selected)
    stage_trigger(settings, mode="dry_run" if dry_run_mode else "live")
    path = stage_report(settings, report_path)

    stats = store.get_stats(settings.db_path)
    console.rule("[bold green]Done")
    console.print(
        f"Discovered {stats['total_discovered']} · "
        f"Qualified {stats['total_qualified']} · "
        f"Selected {stats['selected']} · "
        f"Messages {stats['messages_triggered']} triggered"
    )
    console.print(f"Report → [link={path}]{path}[/link]")
