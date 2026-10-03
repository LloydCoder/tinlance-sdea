"""Signal contract validation helpers."""

from .models import SignalRecord
from .taxonomy import SIGNAL_TAXONOMY_VERSION, SignalType


def validate_signal(signal: SignalRecord) -> SignalRecord:
    """Validate canonical signal semantics and taxonomy membership."""

    SignalType(signal.signal_type)
    if not signal.entity_id.strip():
        raise ValueError("signal entity_id must be non-empty")
    if not signal.source_event_id.strip():
        raise ValueError("signal source_event_id must be non-empty")
    return signal


def taxonomy_version() -> str:
    """Return the canonical signal taxonomy version."""

    return SIGNAL_TAXONOMY_VERSION
