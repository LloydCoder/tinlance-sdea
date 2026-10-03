"""Canonical SDEA domain models."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Any
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class EvidenceState(StrEnum):
    OBSERVED = "observed"
    CORROBORATED = "corroborated"
    INFERRED = "inferred"
    HYPOTHESIZED = "hypothesized"
    QUALIFIED = "qualified"
    CONFIRMED = "confirmed"


class AcquisitionMode(StrEnum):
    HIRE = "hire"
    BUILD = "build"
    BUY = "buy"
    PARTNER = "partner"
    FRACTIONAL = "fractional"
    FDE = "fde"
    PROJECT = "project"
    MANAGED_SERVICE = "managed_service"
    AAAS = "aaas"
    PRODUCT = "product"


class SourceType(StrEnum):
    JOB_POSTING = "job_posting"
    FUNDING = "funding"
    PRODUCT_CHANGE = "product_change"
    TECHNOLOGY_CHANGE = "technology_change"
    LEADERSHIP_CHANGE = "leadership_change"
    EXPANSION = "expansion"
    SECURITY_EVENT = "security_event"
    REGULATORY_EVENT = "regulatory_event"
    PARTNERSHIP = "partnership"
    ACQUISITION = "acquisition"
    PROCUREMENT = "procurement"
    OPEN_SOURCE = "open_source"
    OTHER = "other"


class SDEAModel(BaseModel):
    """Shared configuration for canonical contracts."""

    model_config = ConfigDict(
        extra="forbid",
        frozen=True,
        populate_by_name=True,
        str_strip_whitespace=True,
    )


class Evidence(SDEAModel):
    id: UUID = Field(default_factory=uuid4)
    source_type: SourceType
    source_url: HttpUrl | None = None
    observed_at: datetime
    collected_at: datetime
    title: str
    excerpt: str | None = None
    content_hash: str | None = None
    provenance_ref: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class Signal(SDEAModel):
    id: UUID = Field(default_factory=uuid4)
    entity_id: str
    signal_type: str
    state: EvidenceState = EvidenceState.OBSERVED
    occurred_at: datetime
    observed_at: datetime
    evidence_ids: tuple[UUID, ...] = ()
    attributes: dict[str, Any] = Field(default_factory=dict)


class SignalCluster(SDEAModel):
    id: UUID = Field(default_factory=uuid4)
    entity_id: str
    signal_ids: tuple[UUID, ...]
    state: EvidenceState = EvidenceState.CORROBORATED
    first_observed_at: datetime
    last_observed_at: datetime
    confidence: float = Field(ge=0.0, le=1.0)


class DemandHypothesis(SDEAModel):
    id: UUID = Field(default_factory=uuid4)
    entity_id: str
    statement: str
    state: EvidenceState = EvidenceState.HYPOTHESIZED
    supporting_signal_ids: tuple[UUID, ...] = ()
    confidence: float = Field(ge=0.0, le=1.0)
    rationale: str


class CapabilityNeed(SDEAModel):
    id: UUID = Field(default_factory=uuid4)
    entity_id: str
    capability: str
    demand_hypothesis_id: UUID
    confidence: float = Field(ge=0.0, le=1.0)
    urgency: float = Field(ge=0.0, le=1.0)
    why_now: str


class BuyingWindow(SDEAModel):
    id: UUID = Field(default_factory=uuid4)
    status: str
    starts_at: datetime | None = None
    ends_at: datetime | None = None
    confidence: float = Field(ge=0.0, le=1.0)
    rationale: str


class Opportunity(SDEAModel):
    id: UUID = Field(default_factory=uuid4)
    entity_id: str
    capability_need_id: UUID
    state: EvidenceState = EvidenceState.QUALIFIED
    confidence: float = Field(ge=0.0, le=1.0)
    buying_window_id: UUID | None = None
    acquisition_modes: tuple[AcquisitionMode, ...] = ()
    evidence_ids: tuple[UUID, ...] = ()
    rationale: str


class AcquisitionRecommendation(SDEAModel):
    opportunity_id: UUID
    mode: AcquisitionMode
    confidence: float = Field(ge=0.0, le=1.0)
    rationale: str
    requires_human_approval: bool = True