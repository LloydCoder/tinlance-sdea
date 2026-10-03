"""Source-diversity measures."""

from collections.abc import Iterable


def source_diversity(sources: Iterable[str]) -> float:
    """Return unique-source coverage normalized to three independent sources."""

    unique = {source.strip().casefold() for source in sources if source.strip()}
    return min(len(unique) / 3.0, 1.0)
