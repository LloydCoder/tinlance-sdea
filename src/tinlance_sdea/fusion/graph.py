"""Lightweight signal relationship graph."""

from datetime import timedelta

from ..domain.models import SDEAModel
from ..signals.models import SignalRecord
from .correlator import correlate_signals


class SignalGraph(SDEAModel):
    """Serializable signal graph projection."""

    nodes: tuple[str, ...]
    edges: tuple[tuple[str, str], ...]


def build_graph(signals: tuple[SignalRecord, ...], max_gap: timedelta) -> SignalGraph:
    """Build a graph from temporal correlation edges."""

    return SignalGraph(
        nodes=tuple(sorted(str(signal.id) for signal in signals)),
        edges=correlate_signals(signals, max_gap),
    )
