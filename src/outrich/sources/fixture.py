import json
from pathlib import Path

from outrich.models import RawProfile


def load_fixture(fixture_path: Path) -> list[RawProfile]:
    data = json.loads(fixture_path.read_text())
    return [RawProfile(**item, source="fixture") for item in data]
