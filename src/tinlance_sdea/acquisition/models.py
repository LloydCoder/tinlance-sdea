"""Acquisition recommendation contracts."""

from __future__ import annotations

from pydantic import Field, model_validator

from ..domain.models import AcquisitionMode, SDEAModel


class AcquisitionConstraint(SDEAModel):
    mode: AcquisitionMode
    allowed: bool = True
    rationale: str = ""

    @model_validator(mode="after")
    def validate_constraint(self) -> AcquisitionConstraint:
        if not self.allowed and not self.rationale.strip():
            raise ValueError("a denied acquisition mode requires a rationale")
        return self


class AcquisitionRecommendationRecord(SDEAModel):
    opportunity_id: str
    mode: AcquisitionMode
    confidence: float = Field(ge=0.0, le=1.0)
    rationale: str
    requires_human_approval: bool = True

    @model_validator(mode="after")
    def validate_recommendation(self) -> AcquisitionRecommendationRecord:
        if not self.rationale.strip():
            raise ValueError("recommendation rationale must be non-empty")
        if not self.requires_human_approval:
            raise ValueError("acquisition recommendations require human approval")
        return self
