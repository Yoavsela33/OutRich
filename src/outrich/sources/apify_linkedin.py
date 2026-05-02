import json
import logging
from pathlib import Path

from apify_client import ApifyClient

from outrich.config import Settings
from outrich.models import RawProfile

logger = logging.getLogger(__name__)

_CACHE_FILE = "apify_discover.json"

_SEARCH_TITLES = [
    "Software Engineer",
    "Senior Software Engineer",
    "Staff Engineer",
    "Principal Engineer",
    "Engineering Manager",
    "Data Engineer",
    "Database Engineer",
    "Site Reliability Engineer",
    "Solutions Architect",
    "Data Architect",
    "CTO",
    "VP Engineering",
    "Head of Engineering",
]


def discover(settings: Settings, use_cache: bool = True) -> list[RawProfile]:
    cache_path = settings.cache_dir / _CACHE_FILE
    settings.cache_dir.mkdir(parents=True, exist_ok=True)

    if use_cache and cache_path.exists():
        logger.info("Loading Apify results from cache: %s", cache_path)
        raw = json.loads(cache_path.read_text())
        return [_to_profile(item) for item in raw]

    if not settings.apify_token:
        raise ValueError("APIFY_TOKEN is required for live discovery. Use --source fixture instead.")

    logger.info("Running Apify actor %s ...", settings.apify_actor)
    client = ApifyClient(settings.apify_token)
    run = client.actor(settings.apify_actor).call(
        run_input={
            "keywords": '"DataStax"',
            "currentCompany": ["DataStax"],
            "currentJobTitles": _SEARCH_TITLES,
            "maxItems": settings.apify_limit,
        }
    )
    items = list(client.dataset(run["defaultDatasetId"]).iterate_items())
    cache_path.write_text(json.dumps(items, indent=2))
    logger.info("Cached %d Apify results to %s", len(items), cache_path)

    return [_to_profile(item) for item in items]


def _to_profile(item: dict) -> RawProfile:
    return RawProfile(
        linkedin_url=item.get("linkedInUrl") or item.get("url") or item.get("profileUrl", ""),
        full_name=item.get("fullName") or item.get("name") or "",
        headline=item.get("headline"),
        current_company=item.get("currentCompany") or _extract_company(item),
        current_title=item.get("currentTitle") or item.get("title"),
        location=item.get("location") or item.get("city"),
        summary=item.get("summary") or item.get("about"),
        skills=item.get("skills") or [],
        past_roles=item.get("experience") or item.get("positions") or [],
        education=item.get("education") or [],
        years_experience=item.get("yearsOfExperience"),
        source="apify_live",
        raw_data=item,
    )


def _extract_company(item: dict) -> str | None:
    positions = item.get("positions") or item.get("experience") or []
    if positions and isinstance(positions, list):
        return positions[0].get("companyName") or positions[0].get("company")
    return None
