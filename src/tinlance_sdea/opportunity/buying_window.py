"""Buying-window derivation for opportunities."""

from datetime import datetime

from ..temporal.intervals import TimeInterval
from ..temporal.windows import derive_window


def buying_window(anchor: datetime, horizon_days: int) -> TimeInterval:
    return derive_window(anchor=anchor, horizon_days=horizon_days)
