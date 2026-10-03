"""Deterministic signal deduplication."""

from __future__ import annotations

from collections.abc import Iterable

from .fingerprint import fingerprint_signal
from .models import SignalRecord


def deduplicate_signals(signals: Iterable[SignalRecord]) -> tuple[SignalRecord, ...]:
    """Keep the first signal for each deterministic fingerprint."""

    seen: set[str] = set()
    unique: list[SignalRecord] = []
    for signal in signals:
        fingerprint = fingerprint_signal(signal)
        if fingerprint in seen:
            continue
        seen.add(fingerprint)
        unique.append(signal.model_copy(update={"fingerprint": fingerprint}))
    return tuple(unique)
