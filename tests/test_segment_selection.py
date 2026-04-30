from outrich.config import SEGMENT_QUOTAS
from outrich.models import Segment


def _make_row(id_, segment, score):
    """Minimal dict mimicking a sqlite3.Row for selection logic tests."""
    return {"id": id_, "segment": segment, "relevance_score": score}


def _select(leads):
    """Mirrors pipeline.stage_select selection logic."""
    buckets = {seg: [] for seg in SEGMENT_QUOTAS}
    for lead in leads:
        seg = lead["segment"]
        if seg in buckets:
            buckets[seg].append(lead)

    selected = []
    for seg, quota in SEGMENT_QUOTAS.items():
        candidates = sorted(buckets[seg], key=lambda r: r["relevance_score"], reverse=True)
        selected.extend(r["id"] for r in candidates[:quota])
    return selected


def test_exact_quota_fills():
    leads = (
        [_make_row(i, "obvious_fit", 90 - i) for i in range(6)]
        + [_make_row(i + 10, "high_potential_low_experience", 70 - i) for i in range(3)]
        + [_make_row(20, "wild_card", 60)]
    )
    selected = _select(leads)
    assert len(selected) == 10


def test_top_score_wins_per_segment():
    leads = [
        _make_row(1, "obvious_fit", 95),
        _make_row(2, "obvious_fit", 99),
        _make_row(3, "obvious_fit", 80),
        _make_row(4, "obvious_fit", 70),
        _make_row(5, "obvious_fit", 60),
        _make_row(6, "obvious_fit", 50),
        _make_row(7, "obvious_fit", 40),  # should be excluded (quota = 6)
    ] + [
        _make_row(10, "high_potential_low_experience", 75),
        _make_row(11, "high_potential_low_experience", 65),
        _make_row(12, "high_potential_low_experience", 55),
    ] + [_make_row(20, "wild_card", 60)]

    selected = _select(leads)
    assert 7 not in selected
    assert 2 in selected  # top score
    assert len(selected) == 10


def test_under_quota_does_not_crash():
    leads = [
        _make_row(1, "obvious_fit", 90),
        _make_row(10, "high_potential_low_experience", 70),
        # only 1 obvious, 1 high_potential, 0 wild_card
    ]
    selected = _select(leads)
    assert len(selected) == 2  # short fill, no crash


def test_not_relevant_excluded():
    leads = [
        _make_row(1, "not_relevant", 99),
        _make_row(2, "obvious_fit", 50),
    ] + [_make_row(10, "high_potential_low_experience", 70)] * 3 + [_make_row(20, "wild_card", 60)]
    selected = _select(leads)
    assert 1 not in selected


def test_quotas_match_spec():
    assert SEGMENT_QUOTAS["obvious_fit"] == 6
    assert SEGMENT_QUOTAS["high_potential_low_experience"] == 3
    assert SEGMENT_QUOTAS["wild_card"] == 1
