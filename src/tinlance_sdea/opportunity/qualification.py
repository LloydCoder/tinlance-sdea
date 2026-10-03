"""Opportunity qualification rules."""

from ..domain.models import Opportunity


def qualify(opportunity: Opportunity) -> bool:
    """Require traceable evidence and bounded confidence."""

    return bool(opportunity.evidence_ids) and opportunity.confidence > 0.0
