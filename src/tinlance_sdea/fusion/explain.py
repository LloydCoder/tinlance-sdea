"""Fusion explanation contracts."""

from pydantic import Field

from ..domain.models import SDEAModel


class FusionExplanation(SDEAModel):
    """Explain why signals were grouped or weighted."""

    signal_ids: tuple[str, ...]
    reasons: tuple[str, ...] = Field(default_factory=tuple)


def explain_cluster(
    signal_ids: tuple[str, ...], *, reasons: tuple[str, ...] = ()
) -> FusionExplanation:
    """Create an explicit fusion explanation."""

    return FusionExplanation(signal_ids=signal_ids, reasons=reasons)
