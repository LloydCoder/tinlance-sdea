"""Canonical signal intelligence contracts."""

from .deduplication import deduplicate_signals
from .fingerprint import fingerprint_signal
from .models import SignalRecord
from .normalization import normalize_signal
from .registry import SignalRegistry
from .taxonomy import SIGNAL_TAXONOMY_VERSION, SignalType
from .validation import taxonomy_version, validate_signal

__all__ = [
    "SIGNAL_TAXONOMY_VERSION",
    "SignalRecord",
    "SignalRegistry",
    "SignalType",
    "deduplicate_signals",
    "fingerprint_signal",
    "normalize_signal",
    "taxonomy_version",
    "validate_signal",
]
