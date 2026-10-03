"""Acquisition-mode recommendation."""

from uuid import UUID

from ..domain.models import AcquisitionMode
from .models import AcquisitionRecommendationRecord


def recommend(
    opportunity_id: UUID,
    mode: AcquisitionMode,
    confidence: float,
    rationale: str,
) -> AcquisitionRecommendationRecord:
    return AcquisitionRecommendationRecord(
        opportunity_id=opportunity_id,
        mode=mode,
        confidence=confidence,
        rationale=rationale,
    )
