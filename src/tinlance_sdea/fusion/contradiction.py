"""Contradiction detection for explicit directional signal attributes."""

from ..signals.models import SignalRecord


def find_contradictions(signals: tuple[SignalRecord, ...]) -> tuple[tuple[str, str], ...]:
    """Find same-entity signals with opposite explicit directions."""

    contradictions: list[tuple[str, str]] = []
    for index, left in enumerate(signals):
        left_direction = left.attributes.get("direction")
        if left_direction not in {"increase", "decrease"}:
            continue
        for right in signals[index + 1 :]:
            if right.entity_id != left.entity_id or right.signal_type != left.signal_type:
                continue
            if right.attributes.get("direction") == (
                "decrease" if left_direction == "increase" else "increase"
            ):
                contradictions.append((str(left.id), str(right.id)))
    return tuple(contradictions)
