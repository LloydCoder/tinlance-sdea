"""Uncertainty primitives."""

from pydantic import Field

from ..domain.models import SDEAModel


class Uncertainty(SDEAModel):
    """Independent uncertainty dimensions."""

    evidence_coverage: float = Field(ge=0.0, le=1.0)
    source_agreement: float = Field(ge=0.0, le=1.0)
    temporal_stability: float = Field(ge=0.0, le=1.0)


def uncertainty_score(value: Uncertainty) -> float:
    """Return a conservative arithmetic mean."""

    return (value.evidence_coverage + value.source_agreement + value.temporal_stability) / 3.0
