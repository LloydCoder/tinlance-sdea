"""SDEA policy controls."""

from enum import StrEnum


class PolicyDecision(StrEnum):
    ALLOW = "allow"
    DENY = "deny"
    REVIEW = "review"


def decide(*, confidence: float, threshold: float = 0.7) -> PolicyDecision:
    if not 0.0 <= confidence <= 1.0:
        raise ValueError("confidence must be between 0 and 1")
    if confidence >= threshold:
        return PolicyDecision.ALLOW
    if confidence >= threshold / 2:
        return PolicyDecision.REVIEW
    return PolicyDecision.DENY
