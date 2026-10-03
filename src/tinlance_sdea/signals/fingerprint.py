"""Deterministic signal fingerprinting."""

from __future__ import annotations

import hashlib

from .models import SignalRecord


def fingerprint_signal(signal: SignalRecord) -> str:
    """Return a stable identity fingerprint independent of collection UUID."""

    attributes = "\x1f".join(
        f"{key}={value}" for key, value in sorted(signal.attributes.items())
    )
    parts = (
        signal.entity_id,
        signal.signal_type,
        signal.source_event_id,
        signal.occurred_at.isoformat(),
        attributes,
    )
    return hashlib.sha256("\x1f".join(parts).encode("utf-8")).hexdigest()
