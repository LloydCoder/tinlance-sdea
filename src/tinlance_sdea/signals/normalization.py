"""Deterministic raw-signal normalization."""

from __future__ import annotations

from collections.abc import Mapping
from datetime import datetime
from uuid import UUID

from .models import SignalRecord
from .taxonomy import SignalType


def normalize_signal(
    *,
    entity_id: str,
    signal_type: SignalType,
    source_event_id: str,
    occurred_at: datetime,
    observed_at: datetime,
    evidence_ids: tuple[UUID, ...],
    attributes: Mapping[str, object] | None = None,
) -> SignalRecord:
    """Normalize a raw observation into the canonical signal contract."""

    normalized = {
        str(key).strip(): str(value).strip()
        for key, value in (attributes or {}).items()
        if str(key).strip()
    }
    return SignalRecord(
        entity_id=entity_id.strip(),
        signal_type=signal_type.value,
        source_event_id=source_event_id.strip(),
        occurred_at=occurred_at,
        observed_at=observed_at,
        evidence_ids=evidence_ids,
        attributes=normalized,
    )
