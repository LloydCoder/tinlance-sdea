"""Opportunity relationship graph."""

from ..domain.models import SDEAModel


class OpportunityGraph(SDEAModel):
    nodes: tuple[str, ...]
    edges: tuple[tuple[str, str], ...]


def graph_from_edges(
    nodes: tuple[str, ...], edges: tuple[tuple[str, str], ...]
) -> OpportunityGraph:
    return OpportunityGraph(nodes=nodes, edges=edges)
