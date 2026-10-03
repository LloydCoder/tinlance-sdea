"""Signal correlation primitives."""

from datetime import timedelta
from itertools import combinations

from ..signals.models import SignalRecord


def correlate_signals(
    signals: tuple[SignalRecord, ...], max_gap: timedelta
) -> tuple[tuple[str, str], ...]:
    """Return same-entity signal pairs within a temporal gap."""

    if max_gap.total_seconds() < 0:
        raise ValueError("max_gap cannot be negative")
    pairs: list[tuple[str, str]] = []
    for left, right in combinations(signals, 2):
        if left.entity_id != right.entity_id:
            continue
        if abs(left.occurred_at - right.occurred_at) <= max_gap:
            pairs.append((str(left.id), str(right.id)))
    return tuple(pairs)
