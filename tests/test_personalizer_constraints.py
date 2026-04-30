import pytest
from pydantic import ValidationError

from outrich.models import DraftedMessages, FollowUpEmail, LinkedInInvite


def _valid_invite(body: str = "Valid body under 300 chars.", hooks: list[str] | None = None):
    return LinkedInInvite(body=body, personalization_hooks=hooks or ["runs Cassandra at Netflix"])


def _valid_email(hooks: list[str] | None = None):
    return FollowUpEmail(
        subject="Reducing Cassandra latency at scale",
        body="Saw your QCon talk on 5 years of Cassandra. " * 4,
        personalization_hooks=hooks or ["spoke at QCon about Cassandra"],
    )


def test_full_message_round_trip():
    msgs = DraftedMessages(invite=_valid_invite(), email=_valid_email())
    assert msgs.invite.body
    assert msgs.email.subject
    assert msgs.email.body


def test_invite_character_limit_enforced():
    with pytest.raises(ValidationError):
        _valid_invite(body="A" * 301)


def test_invite_exactly_at_limit():
    invite = _valid_invite(body="B" * 300)
    assert len(invite.body) == 300


def test_invite_hooks_cannot_be_empty():
    with pytest.raises(ValidationError):
        LinkedInInvite(body="Valid body", personalization_hooks=[])


def test_email_subject_cannot_exceed_60():
    with pytest.raises(ValidationError):
        FollowUpEmail(
            subject="X" * 61,
            body="valid body content " * 8,
            personalization_hooks=["some real hook"],
        )


def test_email_hooks_cannot_be_empty():
    with pytest.raises(ValidationError):
        FollowUpEmail(
            subject="Valid subject",
            body="valid body content " * 8,
            personalization_hooks=[],
        )
