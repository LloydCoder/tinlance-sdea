"""Hypothesis validation."""

from ..domain.models import DemandHypothesis


def validate_hypothesis(hypothesis: DemandHypothesis) -> DemandHypothesis:
    if not hypothesis.rationale.strip():
        raise ValueError("hypothesis rationale must be non-empty")
    return hypothesis
