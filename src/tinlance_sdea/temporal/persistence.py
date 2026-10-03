"""Persistence metrics for signal activity."""

from collections.abc import Sequence
from datetime import datetime


def persistence_span(timestamps: Sequence[datetime]) -> float:
    """Return the active span in seconds."""

    if not timestamps:
        return 0.0
    return (max(timestamps) - min(timestamps)).total_seconds()


def persistence_count(timestamps: Sequence[datetime]) -> int:
    """Return the number of observed occurrences."""

    return len(timestamps)
