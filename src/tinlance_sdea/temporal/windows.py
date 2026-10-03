"""Buying-window derivation primitives."""

from datetime import datetime, timedelta

from .intervals import TimeInterval


def derive_window(*, anchor: datetime, horizon_days: int) -> TimeInterval:
    """Create an uncertainty-bearing monitoring window around an anchor."""

    if horizon_days <= 0:
        raise ValueError("horizon_days must be positive")
    return TimeInterval(start=anchor, end=anchor + timedelta(days=horizon_days))
