import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from outrich.config import Settings, SEGMENT_QUOTAS
from outrich.db import store


def generate(settings: Settings, out_path: Path | None = None) -> Path:
    stats = store.get_stats(settings.db_path)
    leads = store.get_qualified_leads(settings.db_path)
    messages = store.get_all_messages(settings.db_path)

    msg_by_lead: dict[int, dict] = {}
    for m in messages:
        lid = m["lead_id"]
        if lid not in msg_by_lead:
            msg_by_lead[lid] = {}
        msg_by_lead[lid][m["channel"]] = m

    selected_ids = set(msg_by_lead.keys())
    selected = [l for l in leads if l["id"] in selected_ids]
    rejected_sample = [l for l in leads if l["id"] not in selected_ids and l["segment"] == "not_relevant"][:5]

    lines: list[str] = []
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines += [
        f"# OutRich Pipeline Run — {ts}",
        "",
        "## Summary",
        "",
        f"| Metric | Count |",
        f"|--------|-------|",
        f"| Leads discovered | {stats['total_discovered']} |",
        f"| Leads qualified | {stats['total_qualified']} |",
        f"| &nbsp;&nbsp;↳ obvious_fit | {stats['segment_obvious_fit']} |",
        f"| &nbsp;&nbsp;↳ high_potential_low_experience | {stats['segment_high_potential_low_experience']} |",
        f"| &nbsp;&nbsp;↳ wild_card | {stats['segment_wild_card']} |",
        f"| &nbsp;&nbsp;↳ not_relevant | {stats['segment_not_relevant']} |",
        f"| Leads selected for outreach | {stats['selected']} |",
        f"| Messages drafted | {stats['messages_drafted']} |",
        f"| Messages triggered (dry-run) | {stats['messages_triggered']} |",
        "",
    ]

    lines += [
        "## Segmentation strategy",
        "",
        "Leads are selected by a quota system that reflects deliberate GTM thinking:",
        "",
        f"- **{SEGMENT_QUOTAS['obvious_fit']} obvious_fit** — proven decision-makers at confirmed Cassandra/DataStax shops. Highest close probability.",
        f"- **{SEGMENT_QUOTAS['high_potential_low_experience']} high_potential_low_experience** — junior engineers at the right companies. Lower authority today, but future champions who influence stack decisions as they grow.",
        f"- **{SEGMENT_QUOTAS['wild_card']} wild_card** — non-obvious but strategically interesting: AI leaders who could become PMs, DevRel figures with community reach, infrastructure investors.",
        "",
        "The qualifier AI assigns each lead to a segment and scores them 0–100. Selection then picks the top-N per quota.",
        "",
    ]

    for segment_key, label in [
        ("obvious_fit", "Obvious fit"),
        ("high_potential_low_experience", "High potential / low experience"),
        ("wild_card", "Wild card"),
    ]:
        segment_leads = [l for l in selected if l["segment"] == segment_key]
        quota = SEGMENT_QUOTAS[segment_key]
        lines += [f"## {label} ({len(segment_leads)}/{quota})", ""]

        for lead in segment_leads:
            lid = lead["id"]
            pain = json.loads(lead["pain_points"] or "[]")
            msgs = msg_by_lead.get(lid, {})
            invite = msgs.get("linkedin_invite")
            email = msgs.get("follow_up_email")
            invite_hooks = json.loads(invite["personalization_hooks"]) if invite else []
            email_hooks = json.loads(email["personalization_hooks"]) if email else []

            lines += [
                f"### {lead['full_name']}",
                f"**{lead['current_title'] or 'N/A'}** at **{lead['current_company'] or 'N/A'}** · {lead['location'] or 'N/A'}",
                f"_{lead['headline'] or ''}_",
                "",
                f"**Score:** {lead['relevance_score']}/100 &nbsp;|&nbsp; **Segment:** `{lead['segment']}`",
                "",
                f"**Qualifier reasoning:** {lead['reasoning']}",
                "",
                f"**ScyllaDB angle:** {lead['scylla_angle']}",
                "",
            ]

            if pain:
                lines += ["**Pain points identified:**", ""]
                for p in pain:
                    lines.append(f"- {p}")
                lines.append("")

            if invite:
                lines += [
                    "**LinkedIn invite** *(dry-run)*",
                    "",
                    f"> {invite['body']}",
                    "",
                    f"*Hooks used: {', '.join(invite_hooks)}*",
                    f"*Characters: {len(invite['body'])}/300*",
                    "",
                ]

            if email:
                lines += [
                    "**Follow-up email** *(dry-run)*",
                    "",
                    f"**Subject:** {email['subject']}",
                    "",
                    email["body"],
                    "",
                    f"*Hooks used: {', '.join(email_hooks)}*",
                    "",
                ]

            lines.append("---")
            lines.append("")

    if rejected_sample:
        lines += ["## Rejected leads (sample — qualifier said no)", ""]
        for lead in rejected_sample:
            lines += [
                f"**{lead['full_name']}** — {lead['current_title']} at {lead['current_company']}",
                f"> {lead['reasoning']}",
                "",
            ]

    out_path = out_path or (settings.sample_run_dir / "report.md")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines))
    return out_path
