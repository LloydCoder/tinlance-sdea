"""Acquisition recommendation explanations."""

from pydantic import Field

from ..domain.models import SDEAModel


class AcquisitionExplanation(SDEAModel):
    opportunity_id: str
    mode: str
    reasons: tuple[str, ...] = Field(default_factory=tuple)
