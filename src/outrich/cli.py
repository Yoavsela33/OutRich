import logging
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", category=FutureWarning, module="instructor")
from typing import Annotated, Optional

import typer
from rich.console import Console
from rich.table import Table

from outrich.config import get_settings
from outrich.db import store
from outrich import pipeline

logging.basicConfig(level=logging.WARNING, format="%(levelname)s %(name)s: %(message)s")

app = typer.Typer(
    name="outrich",
    help="AI-powered B2B outreach pipeline — discovery, qualification, and personalization at scale.",
    no_args_is_help=True,
)
console = Console()

SourceArg = Annotated[
    str,
    typer.Option("--source", help="Lead source: 'fixture' (offline) or 'apify' (live)."),
]
NoCacheArg = Annotated[
    bool,
    typer.Option("--no-cache", help="Force fresh API calls, ignoring local cache."),
]


@app.command()
def discover(source: SourceArg = "fixture", no_cache: NoCacheArg = False) -> None:
    """Discover leads from Apify (live) or the committed fixture (offline)."""
    settings = get_settings()
    pipeline.stage_discover(settings, source=source, use_cache=not no_cache)


@app.command()
def enrich(no_cache: NoCacheArg = False) -> None:
    """Enrich existing leads with Google X-ray (blog posts, talks, GitHub)."""
    settings = get_settings()
    pipeline.stage_enrich(settings, use_cache=not no_cache)


@app.command()
def qualify() -> None:
    """Qualify all unqualified leads with AI. Skips already-qualified leads."""
    settings = get_settings()
    pipeline.stage_qualify(settings)


@app.command()
def select() -> None:
    """Select leads per quota (6 obvious_fit / 3 high_potential / 1 wild_card)."""
    settings = get_settings()
    ids = pipeline.stage_select(settings)
    console.print(f"Selected IDs: {ids}")


@app.command()
def personalize() -> None:
    """Draft LinkedIn invites and follow-up emails for selected leads."""
    settings = get_settings()
    selected = pipeline.stage_select(settings)
    pipeline.stage_personalize(settings, selected)


@app.command()
def trigger(
    live: Annotated[bool, typer.Option("--live", help="Send for real (not implemented).")] = False
) -> None:
    """Log all pending messages. Dry-run by default; --live raises NotImplementedError."""
    if live:
        raise NotImplementedError(
            "Live send adapters (LinkedIn API, email SMTP) are not wired. "
            "Remove this guard when integrating a real send layer."
        )
    settings = get_settings()
    pipeline.stage_trigger(settings, mode="dry_run")


@app.command()
def report(
    out: Annotated[Optional[Path], typer.Option("--out", help="Output path for the report.")] = None
) -> None:
    """Generate a markdown report from the current database state."""
    settings = get_settings()
    pipeline.stage_report(settings, out_path=out)


@app.command()
def run(
    source: SourceArg = "fixture",
    no_cache: NoCacheArg = False,
    live: Annotated[bool, typer.Option("--live", help="Send for real (not implemented).")] = False,
) -> None:
    """Run the complete pipeline end-to-end."""
    if live:
        raise NotImplementedError("Live send is not implemented. Run without --live.")
    settings = get_settings()
    pipeline.run_pipeline(
        settings,
        source=source,
        use_cache=not no_cache,
        dry_run_mode=True,
    )


@app.command()
def status() -> None:
    """Print a summary of the current database state."""
    settings = get_settings()
    if not settings.db_path.exists():
        console.print("[yellow]No database found. Run 'outrich run' first.[/yellow]")
        raise typer.Exit(1)

    stats = store.get_stats(settings.db_path)
    table = Table(title="OutRich — Pipeline Status")
    table.add_column("Stage", style="bold")
    table.add_column("Count", justify="right")
    table.add_row("Discovered", str(stats["total_discovered"]))
    table.add_row("Qualified", str(stats["total_qualified"]))
    table.add_row("  ↳ obvious_fit", str(stats["segment_obvious_fit"]))
    table.add_row("  ↳ high_potential_low_experience", str(stats["segment_high_potential_low_experience"]))
    table.add_row("  ↳ wild_card", str(stats["segment_wild_card"]))
    table.add_row("  ↳ not_relevant", str(stats["segment_not_relevant"]))
    table.add_row("Selected for outreach", str(stats["selected"]))
    table.add_row("Messages drafted", str(stats["messages_drafted"]))
    table.add_row("Messages triggered", str(stats["messages_triggered"]))
    console.print(table)
