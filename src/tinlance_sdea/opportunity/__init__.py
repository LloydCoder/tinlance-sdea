"""Opportunity intelligence contracts."""

from .buying_window import buying_window
from .decay import opportunity_decay
from .explanation import OpportunityExplanation
from .graph import OpportunityGraph, graph_from_edges
from .handoff import make_handoff
from .lifecycle import transition
from .models import OpportunityHandoff, OpportunityRecord
from .qualification import qualify

__all__ = [
    "OpportunityExplanation",
    "OpportunityGraph",
    "OpportunityHandoff",
    "OpportunityRecord",
    "buying_window",
    "graph_from_edges",
    "make_handoff",
    "opportunity_decay",
    "qualify",
    "transition",
]
