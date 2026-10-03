"""Human adjudication contracts."""

from __future__ import annotations

from pydantic import Field, model_validator

from ..domain.models import SDEAModel


class Adjudication(SDEAModel):
    case_id: str
    decision: str
    reviewer: str
    confidence: float = Field(ge=0.0, le=1.0)

    @model_validator(mode="after")
    def validate_adjudication(self) -> Adjudication:
        if not self.case_id.strip():
            raise ValueError("case_id must be non-empty")
        if not self.decision.strip():
            raise ValueError("decision must be non-empty")
        if not self.reviewer.strip():
            raise ValueError("reviewer must be non-empty")
        return self
