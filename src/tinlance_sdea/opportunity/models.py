"""Opportunity intelligence contracts."""

from uuid import UUID

from pydantic import Field

from ..domain.models import AcquisitionMode, SDEAModel


class OpportunityRecord(SDEAModel):
    id: UUID
    entity_id: str
    capability_id: str
    confidence: float = Field(ge=0.0, le=1.0)
    buying_window_id: UUID | None = None
    acquisition_modes: tuple[AcquisitionMode, ...] = ()
    evidence_ids: tuple[UUID, ...] = ()
    rationale: str


class OpportunityHandoff(SDEAModel):
    opportunity_id: UUID
    entity_id: str
    capability_id: str
    confidence: float = Field(ge=0.0, le=1.0)
    rationale: str
