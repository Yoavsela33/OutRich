from enum import Enum
from typing import Annotated, Optional

from pydantic import BaseModel, Field, field_validator

NonEmptyStrList = Annotated[list[str], Field(min_length=1)]


class Segment(str, Enum):
    OBVIOUS_FIT = "obvious_fit"
    HIGH_POTENTIAL_LOW_EXPERIENCE = "high_potential_low_experience"
    WILD_CARD = "wild_card"
    NOT_RELEVANT = "not_relevant"


class RawProfile(BaseModel):
    linkedin_url: str
    full_name: str
    headline: Optional[str] = None
    current_company: Optional[str] = None
    current_title: Optional[str] = None
    location: Optional[str] = None
    summary: Optional[str] = None
    skills: list[str] = Field(default_factory=list)
    past_roles: list[dict] = Field(default_factory=list)
    education: list[dict] = Field(default_factory=list)
    years_experience: Optional[int] = None
    source: str = "fixture"  # 'apify_live' | 'fixture'


class EnrichmentSignal(BaseModel):
    kind: str  # 'blog' | 'talk' | 'github' | 'mention'
    url: str
    title: str
    snippet: Optional[str] = None


class Qualification(BaseModel):
    segment: Segment
    relevance_score: int = Field(ge=0, le=100)
    reasoning: str = Field(min_length=50, max_length=600)
    pain_points: list[str] = Field(default_factory=list)
    scylla_angle: str = Field(min_length=20, max_length=300)
    tech_stack_signals: list[str] = Field(default_factory=list)


class LinkedInInvite(BaseModel):
    body: str
    personalization_hooks: NonEmptyStrList

    @field_validator("body")
    @classmethod
    def enforce_character_limit(cls, v: str) -> str:
        if len(v) > 300:
            raise ValueError(f"LinkedIn invite must be ≤300 chars, got {len(v)}")
        return v


class FollowUpEmail(BaseModel):
    subject: str = Field(max_length=60)
    body: str = Field(min_length=80)
    personalization_hooks: NonEmptyStrList


class DraftedMessages(BaseModel):
    invite: LinkedInInvite
    email: FollowUpEmail
