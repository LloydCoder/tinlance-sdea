"""Inference uncertainty helpers."""

from ..epistemics.uncertainty import Uncertainty


def inference_uncertainty(
    evidence_coverage: float,
    source_agreement: float,
    temporal_stability: float,
) -> Uncertainty:
    return Uncertainty(
        evidence_coverage=evidence_coverage,
        source_agreement=source_agreement,
        temporal_stability=temporal_stability,
    )
