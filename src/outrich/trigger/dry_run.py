import sqlite3

from rich.console import Console
from rich.panel import Panel

from outrich.db import store
from outrich.config import Settings

console = Console()


def trigger_all(settings: Settings, mode: str = "dry_run") -> int:
    """Log all drafted messages that haven't been triggered yet. Returns count."""
    messages = store.get_all_messages(settings.db_path)
    already_sent = _get_sent_message_ids(settings.db_path)

    triggered = 0
    for msg in messages:
        if msg["id"] in already_sent:
            continue

        _display(msg, mode)
        store.log_send(settings.db_path, msg["id"], mode)
        triggered += 1

    return triggered


def _display(msg: sqlite3.Row, mode: str) -> None:
    tag = "[DRY RUN]" if mode == "dry_run" else "[LIVE]"
    lead = f"{msg['full_name']} @ {msg['current_company'] or 'Unknown'}"

    if msg["channel"] == "linkedin_invite":
        title = f"{tag} LinkedIn Invite → {lead}"
        content = msg["body"]
    else:
        title = f"{tag} Follow-up Email → {lead}"
        content = f"Subject: {msg['subject']}\n\n{msg['body']}"

    console.print(Panel(content, title=title, border_style="cyan"))


def _get_sent_message_ids(db_path) -> set[int]:
    import sqlite3 as _sqlite3

    con = _sqlite3.connect(db_path)
    con.row_factory = _sqlite3.Row
    rows = con.execute("SELECT message_id FROM send_log").fetchall()
    con.close()
    return {r["message_id"] for r in rows}
