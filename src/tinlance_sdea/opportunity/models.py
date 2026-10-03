"""Opportunity intelligence contracts."""

from __future__ import annotations

from uuid import UUID

from pydantic import Field, model_validator

from ..domain.models import AcquisitionMode, SDEAModel


class OpportunityRecord(SDEAModel):
    id: UUID
    entity_id: str
    capability_id: str
    confidence: float = Field(ge=0.0, le=1.0)
    buying_window_id: UUID | None = None
    acquisition_modes: tuple[AcquisitionMode, ...] = ()
    evidence_ids: tuple[UUID, ...]
    rationale: str

    @model_validator(mode="after")
    def validate_record(self) -> OpportunityRecord:
        if not self.entity_id.strip():
            raise ValueError("entity_id must be non-empty")
        if not self.capability_id.strip():
            raise ValueError("capability_id must be non-empty")
        if not self.evidence_ids:
            raise ValueError("opportunity records require evidence lineage")
        if not self.rationale.strip():
            raise ValueError("rationale must be non-empty")
        return self


class OpportunityHandoff(SDEAModel):
    opportunity_id: UUID
    entity_id: str
    capability_id: str
    confidence: float = Field(ge=0.0, le=1.0)
    evidence_ids: tuple[UUID, ...]
    rationale: str

    @model_validator(mode="after")
    def validate_handoff(self) -> OpportunityHandoff:
        if not self.entity_id.strip():
            raise ValueError("entity_id must be non-empty")
        if not self.capability_id.strip():
            raise ValueError("capability_id must be non-empty")
        if not self.evidence_ids:
            raise ValueError("opportunity handoffs require evidence lineage")
        if not self.rationale.strip():
            raise ValueError("rationale must be non-empty")
        return self
