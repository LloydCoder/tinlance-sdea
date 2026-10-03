"""Business invariants for SDEA domain contracts."""

from .models import DemandHypothesis, Opportunity


class InvariantViolation(ValueError):
    """Raised when an SDEA domain invariant is violated."""


def require_evidence_for_opportunity(opportunity: Opportunity, evidence_count: int) -> None:
    """Require an opportunity to remain traceable to at least one evidence item."""

    if evidence_count <= 0 or not opportunity.evidence_ids:
        raise InvariantViolation(
            "An SDEA opportunity must remain traceable to at least one evidence item."
        )


def require_rationale(hypothesis: DemandHypothesis) -> None:
    """Require an explicit rationale for every demand hypothesis."""

    if not hypothesis.rationale.strip():
        raise InvariantViolation("A demand hypothesis requires an explicit rationale.")
