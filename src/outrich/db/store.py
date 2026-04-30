import json
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Generator

from outrich.models import DraftedMessages, Qualification, RawProfile


def init_db(db_path: Path) -> None:
    schema = (Path(__file__).parent / "schema.sql").read_text()
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(db_path) as conn:
        conn.executescript(schema)


@contextmanager
def _conn(db_path: Path) -> Generator[sqlite3.Connection, None, None]:
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    try:
        yield con
        con.commit()
    except Exception:
        con.rollback()
        raise
    finally:
        con.close()


def upsert_lead(db_path: Path, profile: RawProfile) -> int:
    with _conn(db_path) as con:
        cur = con.execute(
            """
            INSERT INTO leads (linkedin_url, full_name, headline, current_company,
                               current_title, location, raw_profile, source)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(linkedin_url) DO UPDATE SET
                headline        = excluded.headline,
                current_company = excluded.current_company,
                current_title   = excluded.current_title,
                raw_profile     = excluded.raw_profile
            RETURNING id
            """,
            (
                profile.linkedin_url,
                profile.full_name,
                profile.headline,
                profile.current_company,
                profile.current_title,
                profile.location,
                profile.model_dump_json(),
                profile.source,
            ),
        )
        return cur.fetchone()["id"]


def save_qualification(
    db_path: Path, lead_id: int, qual: Qualification, model_used: str
) -> None:
    with _conn(db_path) as con:
        con.execute(
            """
            INSERT INTO qualifications
                (lead_id, segment, relevance_score, reasoning, pain_points,
                 scylla_angle, tech_stack_signals, model_used)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(lead_id) DO NOTHING
            """,
            (
                lead_id,
                qual.segment.value,
                qual.relevance_score,
                qual.reasoning,
                json.dumps(qual.pain_points),
                qual.scylla_angle,
                json.dumps(qual.tech_stack_signals),
                model_used,
            ),
        )


def save_messages(
    db_path: Path, lead_id: int, msgs: DraftedMessages, model_used: str
) -> None:
    with _conn(db_path) as con:
        con.execute(
            """
            INSERT INTO messages (lead_id, channel, subject, body, personalization_hooks, model_used)
            VALUES (?, 'linkedin_invite', NULL, ?, ?, ?)
            ON CONFLICT(lead_id, channel) DO NOTHING
            """,
            (
                lead_id,
                msgs.invite.body,
                json.dumps(msgs.invite.personalization_hooks),
                model_used,
            ),
        )
        con.execute(
            """
            INSERT INTO messages (lead_id, channel, subject, body, personalization_hooks, model_used)
            VALUES (?, 'follow_up_email', ?, ?, ?, ?)
            ON CONFLICT(lead_id, channel) DO NOTHING
            """,
            (
                lead_id,
                msgs.email.subject,
                msgs.email.body,
                json.dumps(msgs.email.personalization_hooks),
                model_used,
            ),
        )


def log_send(db_path: Path, message_id: int, mode: str = "dry_run") -> None:
    with _conn(db_path) as con:
        con.execute(
            "INSERT INTO send_log (message_id, mode, status) VALUES (?, ?, 'logged')",
            (message_id, mode),
        )


# ── read helpers ─────────────────────────────────────────────────────────────


def get_leads_without_qualification(db_path: Path) -> list[sqlite3.Row]:
    with _conn(db_path) as con:
        return con.execute(
            """
            SELECT l.id, l.linkedin_url, l.full_name, l.headline, l.current_company,
                   l.current_title, l.location, l.raw_profile, l.source
            FROM leads l
            LEFT JOIN qualifications q ON l.id = q.lead_id
            WHERE q.id IS NULL
            ORDER BY l.id
            """
        ).fetchall()


def get_qualified_leads(db_path: Path) -> list[sqlite3.Row]:
    with _conn(db_path) as con:
        return con.execute(
            """
            SELECT l.id, l.full_name, l.headline, l.current_company, l.current_title,
                   l.location, l.raw_profile,
                   q.segment, q.relevance_score, q.reasoning,
                   q.pain_points, q.scylla_angle, q.tech_stack_signals, q.model_used
            FROM leads l
            JOIN qualifications q ON l.id = q.lead_id
            ORDER BY q.relevance_score DESC
            """
        ).fetchall()


def get_leads_without_messages(db_path: Path, lead_ids: list[int]) -> list[int]:
    if not lead_ids:
        return []
    with _conn(db_path) as con:
        placeholders = ",".join("?" * len(lead_ids))
        existing = {
            r["lead_id"]
            for r in con.execute(
                f"SELECT DISTINCT lead_id FROM messages WHERE lead_id IN ({placeholders})",
                lead_ids,
            ).fetchall()
        }
    return [lid for lid in lead_ids if lid not in existing]


def get_all_messages(db_path: Path) -> list[sqlite3.Row]:
    with _conn(db_path) as con:
        return con.execute(
            """
            SELECT m.id, m.lead_id, m.channel, m.subject, m.body,
                   m.personalization_hooks, m.model_used, m.drafted_at,
                   l.full_name, l.current_company
            FROM messages m
            JOIN leads l ON m.lead_id = l.id
            ORDER BY m.lead_id, m.channel
            """
        ).fetchall()


def get_stats(db_path: Path) -> dict:
    with _conn(db_path) as con:
        stats: dict = {}
        stats["total_discovered"] = con.execute("SELECT COUNT(*) FROM leads").fetchone()[0]
        stats["total_qualified"] = con.execute("SELECT COUNT(*) FROM qualifications").fetchone()[0]
        for seg in ["obvious_fit", "high_potential_low_experience", "wild_card", "not_relevant"]:
            stats[f"segment_{seg}"] = con.execute(
                "SELECT COUNT(*) FROM qualifications WHERE segment = ?", (seg,)
            ).fetchone()[0]
        stats["selected"] = con.execute(
            "SELECT COUNT(DISTINCT lead_id) FROM messages"
        ).fetchone()[0]
        stats["messages_drafted"] = con.execute("SELECT COUNT(*) FROM messages").fetchone()[0]
        stats["messages_triggered"] = con.execute("SELECT COUNT(*) FROM send_log").fetchone()[0]
        return stats
