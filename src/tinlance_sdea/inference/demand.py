"""Demand-hypothesis construction."""

from uuid import UUID

from ..domain.models import DemandHypothesis


def infer_demand(
    *,
    entity_id: str,
    statement: str,
    supporting_signal_ids: tuple[UUID, ...],
    confidence: float,
    rationale: str,
) -> DemandHypothesis:
    return DemandHypothesis(
        entity_id=entity_id,
        statement=statement,
        supporting_signal_ids=supporting_signal_ids,
        confidence=confidence,
        rationale=rationale,
    )
