"""Deterministic entity-resolution helpers."""

from __future__ import annotations

from .models import Entity, EntityResolution
from .normalization import normalize_entity_name


def resolve_entity(source_value: str, entities: tuple[Entity, ...]) -> EntityResolution | None:
    """Resolve an input value by exact normalized canonical name or alias.

    This intentionally performs deterministic matching only. Probabilistic or
    model-assisted resolution belongs in a later inference layer.
    """

    normalized = normalize_entity_name(source_value)
    for entity in entities:
        candidates = (entity.canonical_name, *(alias.value for alias in entity.aliases))
        if any(normalize_entity_name(candidate) == normalized for candidate in candidates):
            return EntityResolution(
                source_value=source_value,
                entity_id=entity.id,
                method="exact_normalized_name",
                confidence=1.0,
                rationale="Exact normalized canonical name or alias match.",
            )
    return None
