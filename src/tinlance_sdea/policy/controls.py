"""SDEA recommendation-quality policy controls.

These controls are advisory quality gates, not authorization. Agent Platform
remains the authoritative owner of permissions and action approvals.
"""

from enum import StrEnum


class PolicyDecision(StrEnum):
    ELIGIBLE = "eligible"
    REVIEW = "review"
    INSUFFICIENT_EVIDENCE = "insufficient_evidence"


def decide(*, confidence: float, threshold: float = 0.7) -> PolicyDecision:
    """Classify an intelligence result for downstream human review."""

    if not 0.0 <= confidence <= 1.0:
        raise ValueError("confidence must be between 0 and 1")
    if not 0.0 < threshold <= 1.0:
        raise ValueError("threshold must be between 0 and 1")
    if confidence >= threshold:
        return PolicyDecision.ELIGIBLE
    if confidence >= threshold / 2:
        return PolicyDecision.REVIEW
    return PolicyDecision.INSUFFICIENT_EVIDENCE
