from pathlib import Path
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"

SEGMENT_QUOTAS: dict[str, int] = {
    "obvious_fit": 6,
    "high_potential_low_experience": 3,
    "wild_card": 1,
}

ICP = (
    "Engineers, architects, and engineering leaders at companies running Cassandra / "
    "DataStax Enterprise / Astra DB workloads — particularly where latency, cost, or "
    "operational complexity are likely pain points. Secondary ICP: AI/ML leaders, "
    "DevRel figures, and infrastructure investors with adjacency to the NoSQL ecosystem."
)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    anthropic_api_key: Optional[str] = None
    gemini_api_key: Optional[str] = None
    apify_token: Optional[str] = None

    claude_model: str = "claude-sonnet-4-6"
    gemini_model: str = "gemini-1.5-flash"
    apify_actor: str = "harvestapi/linkedin-profile-search"
    apify_limit: int = 50

    db_path: Path = DATA_DIR / "outrich.db"
    cache_dir: Path = DATA_DIR / "cache"
    fixture_path: Path = DATA_DIR / "fixtures" / "leads.json"
    sample_run_dir: Path = DATA_DIR / "sample_run"


def get_settings() -> Settings:
    return Settings()
