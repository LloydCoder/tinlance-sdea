"""Persistence metrics for signal activity."""

from collections.abc import Sequence
from datetime import datetime


def _require_aware(timestamps: Sequence[datetime]) -> None:
    if any(value.tzinfo is None or value.utcoffset() is None for value in timestamps):
        raise ValueError("timestamps must be timezone-aware")


def persistence_span(timestamps: Sequence[datetime]) -> float:
    """Return the active span in seconds."""

    if not timestamps:
        return 0.0
    _require_aware(timestamps)
    return (max(timestamps) - min(timestamps)).total_seconds()


def persistence_count(timestamps: Sequence[datetime]) -> int:
    """Return the number of observed occurrences."""

    _require_aware(timestamps)
    return len(timestamps)
