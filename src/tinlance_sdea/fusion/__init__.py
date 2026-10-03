"""Fusion intelligence contracts."""

from .clustering import cluster_signals
from .contradiction import find_contradictions
from .correlator import correlate_signals
from .explain import FusionExplanation, explain_cluster
from .graph import SignalGraph, build_graph
from .source_diversity import source_diversity
from .weighting import weight_signal

__all__ = [
    "FusionExplanation",
    "SignalGraph",
    "build_graph",
    "cluster_signals",
    "correlate_signals",
    "explain_cluster",
    "find_contradictions",
    "source_diversity",
    "weight_signal",
]
