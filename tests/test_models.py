import pytest
from pydantic import ValidationError

from outrich.models import LinkedInInvite, FollowUpEmail, Qualification, Segment


def test_linkedin_invite_rejects_over_300_chars():
    with pytest.raises(ValidationError, match="300"):
        LinkedInInvite(body="x" * 301, personalization_hooks=["some hook"])


def test_linkedin_invite_accepts_exactly_300_chars():
    invite = LinkedInInvite(body="x" * 300, personalization_hooks=["some hook"])
    assert len(invite.body) == 300


def test_linkedin_invite_requires_hooks():
    with pytest.raises(ValidationError):
        LinkedInInvite(body="Hi there", personalization_hooks=[])


def test_follow_up_email_subject_limit():
    with pytest.raises(ValidationError):
        FollowUpEmail(subject="x" * 61, body="valid body " * 10, personalization_hooks=["hook"])


def test_qualification_score_range():
    with pytest.raises(ValidationError):
        Qualification(
            segment=Segment.OBVIOUS_FIT,
            relevance_score=101,
            reasoning="x" * 50,
            scylla_angle="x" * 20,
        )

    with pytest.raises(ValidationError):
        Qualification(
            segment=Segment.OBVIOUS_FIT,
            relevance_score=-1,
            reasoning="x" * 50,
            scylla_angle="x" * 20,
        )


def test_qualification_reasoning_min_length():
    with pytest.raises(ValidationError):
        Qualification(
            segment=Segment.OBVIOUS_FIT,
            relevance_score=80,
            reasoning="too short",
            scylla_angle="x" * 20,
        )
