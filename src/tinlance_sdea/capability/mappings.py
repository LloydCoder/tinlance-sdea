"""Source-to-capability mapping helpers."""

from .aliases import normalize_alias
from .models import CapabilityMapping


def mapping_for(source: str, capability_id: str, confidence: float, rationale: str) -> CapabilityMapping:
    return CapabilityMapping(
        source=normalize_alias(source),
        capability_id=capability_id,
        confidence=confidence,
        rationale=rationale,
    )
