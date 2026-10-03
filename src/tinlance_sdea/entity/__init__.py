"""Entity identity and resolution contracts for SDEA."""

from .models import Entity, EntityAlias, EntityIdentifier, EntityResolution, EntityType
from .normalization import normalize_entity_name
from .resolution import AmbiguousEntityResolution, resolve_entity

__all__ = [
    "AmbiguousEntityResolution",
    "Entity",
    "EntityAlias",
    "EntityIdentifier",
    "EntityResolution",
    "EntityType",
    "normalize_entity_name",
    "resolve_entity",
]
