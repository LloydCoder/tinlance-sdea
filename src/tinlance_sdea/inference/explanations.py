"""Inference explanation contracts."""

from pydantic import Field

from ..domain.models import SDEAModel


class InferenceExplanation(SDEAModel):
    hypothesis_id: str
    evidence_ids: tuple[str, ...] = ()
    reasons: tuple[str, ...] = Field(default_factory=tuple)
