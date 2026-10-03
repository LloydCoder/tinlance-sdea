"""Deterministic signal clustering."""

from datetime import timedelta

from ..signals.models import SignalRecord
from .correlator import correlate_signals


def cluster_signals(
    signals: tuple[SignalRecord, ...], max_gap: timedelta
) -> tuple[tuple[str, ...], ...]:
    """Build connected components from correlated signals."""

    adjacency: dict[str, set[str]] = {str(signal.id): set() for signal in signals}
    for left, right in correlate_signals(signals, max_gap):
        adjacency[left].add(right)
        adjacency[right].add(left)

    clusters: list[tuple[str, ...]] = []
    unseen = set(adjacency)
    while unseen:
        root = min(unseen)
        stack = [root]
        component: set[str] = set()
        while stack:
            node = stack.pop()
            if node in component:
                continue
            component.add(node)
            unseen.discard(node)
            stack.extend(adjacency[node] - component)
        clusters.append(tuple(sorted(component)))
    return tuple(sorted(clusters))
