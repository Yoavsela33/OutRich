import json
import logging

from apify_client import ApifyClient

from outrich.config import Settings
from outrich.models import RawProfile

logger = logging.getLogger(__name__)

_CACHE_FILE = "apify_discover.json"


def discover(settings: Settings, use_cache: bool = True) -> list[RawProfile]:
    cache_path = settings.cache_dir / _CACHE_FILE
    settings.cache_dir.mkdir(parents=True, exist_ok=True)

    if use_cache and cache_path.exists():
        logger.info("Loading Apify results from cache: %s", cache_path)
        raw = json.loads(cache_path.read_text())
        profiles = [_to_profile(item) for item in raw]
    else:
        if not settings.apify_token:
            raise ValueError("APIFY_TOKEN is required for live discovery. Use --source fixture instead.")

        logger.info("Running Apify actor %s ...", settings.apify_actor)
        client = ApifyClient(settings.apify_token)
        run = client.actor(settings.apify_actor).call(
            run_input={
                "keywords": "DataStax",
                "maxItems": settings.apify_limit,
            }
        )
        items = list(client.dataset(run["defaultDatasetId"]).iterate_items())
        cache_path.write_text(json.dumps(items, indent=2))
        logger.info("Cached %d Apify results to %s", len(items), cache_path)
        profiles = [_to_profile(item) for item in items]

    logger.info("Discovered %d DataStax-affiliated profiles (current + former)", len(profiles))
    return profiles


def _to_profile(item: dict) -> RawProfile:
    # harvestapi/linkedin-profile-search uses firstName/lastName, not fullName
    full_name = (
        item.get("fullName")
        or f"{item.get('firstName', '')} {item.get('lastName', '')}".strip()
        or item.get("name")
        or ""
    )

    # current position is an array; first entry is the active role
    current_pos = (item.get("currentPosition") or [{}])[0] if item.get("currentPosition") else {}
    current_company = (
        item.get("currentCompany")
        or current_pos.get("companyName")
        or _extract_company(item)
    )
    current_title = (
        item.get("currentTitle")
        or current_pos.get("position")
        or item.get("title")
    )

    # location is a dict {"linkedinText": "...", ...} or plain string
    raw_loc = item.get("location")
    if isinstance(raw_loc, dict):
        location = raw_loc.get("linkedinText") or raw_loc.get("text")
    else:
        location = raw_loc or item.get("city")

    # topSkills can be a bullet-separated string; skills can be list[str|dict]
    top = item.get("topSkills")
    if isinstance(top, str) and top:
        skills: list[str] = [s.strip() for s in top.split("•") if s.strip()]
    else:
        skills = _normalize_skills(item.get("skills") or [])

    return RawProfile(
        linkedin_url=(
            item.get("linkedInUrl")
            or item.get("linkedinUrl")
            or item.get("url")
            or item.get("profileUrl")
            or ""
        ),
        full_name=full_name,
        headline=item.get("headline"),
        current_company=current_company,
        current_title=current_title,
        location=location,
        summary=item.get("summary") or item.get("about"),
        skills=skills,
        past_roles=item.get("experience") or item.get("positions") or item.get("currentPosition") or [],
        education=item.get("education") or [],
        years_experience=item.get("yearsOfExperience"),
        source="apify_live",
    )


def _normalize_skills(skills: list) -> list[str]:
    result = []
    for s in skills:
        if isinstance(s, str):
            result.append(s)
        elif isinstance(s, dict):
            name = s.get("name", "")
            if name:
                result.append(name)
    return result


def _extract_company(item: dict) -> str | None:
    for key in ("positions", "experience", "currentPosition"):
        positions = item.get(key) or []
        if positions and isinstance(positions, list):
            first = positions[0]
            return first.get("companyName") or first.get("company")
    return None
