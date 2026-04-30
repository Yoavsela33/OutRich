import json
import logging
import re
from pathlib import Path

from googleapiclient.discovery import build

from outrich.config import Settings

logger = logging.getLogger(__name__)


def enrich_lead(
    lead_id: int,
    full_name: str,
    settings: Settings,
    use_cache: bool = True,
) -> list[dict]:
    """Return a list of enrichment signal dicts for the given lead."""
    cache_dir = settings.cache_dir / "xray"
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_path = cache_dir / f"{lead_id}.json"

    if use_cache and cache_path.exists():
        return json.loads(cache_path.read_text())

    if not settings.google_cse_api_key or not settings.google_cse_cx:
        logger.debug("Google CSE not configured — skipping enrichment for lead %d", lead_id)
        return []

    query = f'"{full_name}" ("DataStax" OR "Cassandra" OR "Astra DB") -site:linkedin.com'
    try:
        service = build("customsearch", "v1", developerKey=settings.google_cse_api_key)
        response = (
            service.cse()
            .list(q=query, cx=settings.google_cse_cx, num=5)
            .execute()
        )
        items = response.get("items") or []
    except Exception as exc:
        logger.warning("Google CSE failed for lead %d: %s", lead_id, exc)
        return []

    signals = [_classify(item) for item in items]
    cache_path.write_text(json.dumps(signals, indent=2))
    return signals


def _classify(item: dict) -> dict:
    url = item.get("link", "")
    title = item.get("title", "")
    snippet = item.get("snippet", "")

    if re.search(r"github\.com", url):
        kind = "github"
    elif re.search(r"youtube\.com|youtu\.be|conf|summit|keynote|talk", url + title, re.I):
        kind = "talk"
    elif re.search(r"medium\.com|dev\.to|substack|blog|hashnode", url, re.I):
        kind = "blog"
    else:
        kind = "mention"

    return {"kind": kind, "url": url, "title": title, "snippet": snippet}
