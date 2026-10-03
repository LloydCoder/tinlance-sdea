"""Outcome event construction."""

from datetime import datetime
from uuid import UUID, uuid4

from .models import OutcomeEvent


def record_event(opportunity_id: UUID, event_type: str, occurred_at: datetime) -> OutcomeEvent:
    return OutcomeEvent(
        id=uuid4(),
        opportunity_id=opportunity_id,
        event_type=event_type,
        occurred_at=occurred_at,
    )
