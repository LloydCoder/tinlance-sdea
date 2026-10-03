"""Deterministic inference rules."""

from ..signals.models import SignalRecord


def rule_match(signal: SignalRecord, signal_type: str) -> bool:
    return signal.signal_type == signal_type
