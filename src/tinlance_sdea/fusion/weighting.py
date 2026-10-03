"""Signal weighting primitives."""

from ..signals.models import SignalRecord


def weight_signal(signal: SignalRecord, *, source_reliability: float = 1.0) -> float:
    """Compute a bounded deterministic weight."""

    if not 0.0 <= source_reliability <= 1.0:
        raise ValueError("source_reliability must be between 0 and 1")
    evidence_factor = min(len(signal.evidence_ids) / 3.0, 1.0)
    return source_reliability * (0.5 + 0.5 * evidence_factor)
