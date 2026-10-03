"""Deterministic entity-resolution helpers."""

from __future__ import annotations

from .models import Entity, EntityResolution
from .normalization import normalize_entity_name


class AmbiguousEntityResolution(ValueError):
    """Raised when a normalized value matches multiple entities."""


def resolve_entity(source_value: str, entities: tuple[Entity, ...]) -> EntityResolution | None:
    """Resolve an input by exact normalized canonical name or alias.

    Deterministic matching is intentionally conservative: an ambiguous match
    is rejected rather than silently selecting whichever entity appears first.
    Probabilistic or model-assisted resolution belongs in a later inference layer.
    """

    normalized = normalize_entity_name(source_value)
    if not normalized:
        return None

    matches: list[Entity] = []
    for entity in entities:
        candidates = (entity.canonical_name, *(alias.value for alias in entity.aliases))
        if any(normalize_entity_name(candidate) == normalized for candidate in candidates):
            matches.append(entity)

    if len(matches) > 1:
        raise AmbiguousEntityResolution(
            f"normalized entity value matches multiple entities: {source_value!r}"
        )
    if not matches:
        return None

    entity = matches[0]
    return EntityResolution(
        source_value=source_value,
        entity_id=entity.id,
        method="exact_normalized_name",
        confidence=1.0,
        rationale="Exact normalized canonical name or alias match.",
    )
