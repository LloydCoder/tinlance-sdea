"""Canonical SDEA domain models."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Any
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field, HttpUrl, model_validator


def _require_aware(value: datetime, field_name: str) -> None:
    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError(f"{field_name} must be timezone-aware")


class EpistemicState(StrEnum):
    """What the available evidence supports epistemically."""

    OBSERVED = "observed"
    CORROBORATED = "corroborated"
    INFERRED = "inferred"
    HYPOTHESIZED = "hypothesized"
    QUALIFIED = "qualified"
    CONFIRMED = "confirmed"


class LifecycleState(StrEnum):
    """Lifecycle of an intelligence object independent of epistemic certainty."""

    ACTIVE = "active"
    STALE = "stale"
    RESOLVED = "resolved"
    EXPIRED = "expired"
    SUPERSEDED = "superseded"
    RETRACTED = "retracted"


# Backward-compatible name for the pre-S1 contract.
EvidenceState = EpistemicState


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
    epistemic_state: EpistemicState = EpistemicState.OBSERVED
    lifecycle_state: LifecycleState = LifecycleState.ACTIVE

    @model_validator(mode="after")
    def validate_temporal_and_identity(self) -> Evidence:
        _require_aware(self.observed_at, "observed_at")
        _require_aware(self.collected_at, "collected_at")
        if self.collected_at < self.observed_at:
            raise ValueError("collected_at cannot be earlier than observed_at")
        if not self.title.strip():
            raise ValueError("title must be non-empty")
        return self


class Signal(SDEAModel):
    id: UUID = Field(default_factory=uuid4)
    entity_id: str
    signal_type: str
    state: EpistemicState = EpistemicState.OBSERVED
    lifecycle_state: LifecycleState = LifecycleState.ACTIVE
    occurred_at: datetime
    observed_at: datetime
    evidence_ids: tuple[UUID, ...] = ()
    attributes: dict[str, Any] = Field(default_factory=dict)

    @model_validator(mode="after")
    def validate_identity_and_temporal_order(self) -> Signal:
        _require_aware(self.occurred_at, "occurred_at")
        _require_aware(self.observed_at, "observed_at")
        if not self.entity_id.strip():
            raise ValueError("entity_id must be non-empty")
        if not self.signal_type.strip():
            raise ValueError("signal_type must be non-empty")
        if self.observed_at < self.occurred_at:
            raise ValueError("observed_at cannot be earlier than occurred_at")
        if not self.evidence_ids:
            raise ValueError("a signal must reference at least one evidence item")
        return self


class SignalCluster(SDEAModel):
    id: UUID = Field(default_factory=uuid4)
    entity_id: str
    signal_ids: tuple[UUID, ...]
    state: EpistemicState = EpistemicState.CORROBORATED
    lifecycle_state: LifecycleState = LifecycleState.ACTIVE
    first_observed_at: datetime
    last_observed_at: datetime
    confidence: float = Field(ge=0.0, le=1.0)

    @model_validator(mode="after")
    def validate_interval_and_membership(self) -> SignalCluster:
        _require_aware(self.first_observed_at, "first_observed_at")
        _require_aware(self.last_observed_at, "last_observed_at")
        if not self.entity_id.strip():
            raise ValueError("entity_id must be non-empty")
        if not self.signal_ids:
            raise ValueError("signal_ids must not be empty")
        if self.last_observed_at < self.first_observed_at:
            raise ValueError("last_observed_at cannot be earlier than first_observed_at")
        return self


class DemandHypothesis(SDEAModel):
    id: UUID = Field(default_factory=uuid4)
    entity_id: str
    statement: str
    state: EpistemicState = EpistemicState.HYPOTHESIZED
    lifecycle_state: LifecycleState = LifecycleState.ACTIVE
    supporting_signal_ids: tuple[UUID, ...] = ()
    confidence: float = Field(ge=0.0, le=1.0)
    rationale: str

    @model_validator(mode="after")
    def validate_hypothesis(self) -> DemandHypothesis:
        if not self.entity_id.strip():
            raise ValueError("entity_id must be non-empty")
        if not self.statement.strip():
            raise ValueError("statement must be non-empty")
        if not self.supporting_signal_ids:
            raise ValueError("supporting_signal_ids must not be empty")
        if not self.rationale.strip():
            raise ValueError("rationale must be non-empty")
        return self


class CapabilityNeed(SDEAModel):
    id: UUID = Field(default_factory=uuid4)
    entity_id: str
    capability: str
    demand_hypothesis_id: UUID
    confidence: float = Field(ge=0.0, le=1.0)
    urgency: float = Field(ge=0.0, le=1.0)
    why_now: str

    @model_validator(mode="after")
    def validate_need(self) -> CapabilityNeed:
        if not self.entity_id.strip():
            raise ValueError("entity_id must be non-empty")
        if not self.capability.strip():
            raise ValueError("capability must be non-empty")
        if not self.why_now.strip():
            raise ValueError("why_now must be non-empty")
        return self


class BuyingWindow(SDEAModel):
    id: UUID = Field(default_factory=uuid4)
    status: str
    starts_at: datetime | None = None
    ends_at: datetime | None = None
    confidence: float = Field(ge=0.0, le=1.0)
    rationale: str

    @model_validator(mode="after")
    def validate_interval(self) -> BuyingWindow:
        if self.starts_at is not None:
            _require_aware(self.starts_at, "starts_at")
        if self.ends_at is not None:
            _require_aware(self.ends_at, "ends_at")
        if (
            self.starts_at is not None
            and self.ends_at is not None
            and self.ends_at < self.starts_at
        ):
            raise ValueError("ends_at cannot be earlier than starts_at")
        if not self.status.strip():
            raise ValueError("status must be non-empty")
        if not self.rationale.strip():
            raise ValueError("rationale must be non-empty")
        return self


class Opportunity(SDEAModel):
    id: UUID = Field(default_factory=uuid4)
    entity_id: str
    capability_need_id: UUID
    state: EpistemicState = EpistemicState.QUALIFIED
    lifecycle_state: LifecycleState = LifecycleState.ACTIVE
    confidence: float = Field(ge=0.0, le=1.0)
    buying_window_id: UUID | None = None
    acquisition_modes: tuple[AcquisitionMode, ...] = ()
    evidence_ids: tuple[UUID, ...] = ()
    rationale: str

    @model_validator(mode="after")
    def validate_opportunity(self) -> Opportunity:
        if not self.entity_id.strip():
            raise ValueError("entity_id must be non-empty")
        if not self.evidence_ids:
            raise ValueError("an opportunity must reference at least one evidence item")
        if not self.rationale.strip():
            raise ValueError("rationale must be non-empty")
        return self


class AcquisitionRecommendation(SDEAModel):
    opportunity_id: UUID
    mode: AcquisitionMode
    confidence: float = Field(ge=0.0, le=1.0)
    rationale: str
    requires_human_approval: bool = True

    @model_validator(mode="after")
    def validate_recommendation(self) -> AcquisitionRecommendation:
        if not self.rationale.strip():
            raise ValueError("rationale must be non-empty")
        if not self.requires_human_approval:
            raise ValueError("SDEA recommendations must require human approval")
        return self
