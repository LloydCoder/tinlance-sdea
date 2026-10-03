"""Acquisition recommendation contracts."""

from uuid import UUID

from pydantic import Field

from ..domain.models import AcquisitionMode, SDEAModel


class AcquisitionConstraint(SDEAModel):
    mode: AcquisitionMode
    allowed: bool = True
    rationale: str = ""


class AcquisitionRecommendationRecord(SDEAModel):
    opportunity_id: UUID
    mode: AcquisitionMode
    confidence: float = Field(ge=0.0, le=1.0)
    rationale: str
    requires_human_approval: bool = True
