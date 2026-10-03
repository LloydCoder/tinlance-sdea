"""Entity identity and resolution contracts for SDEA."""

from .models import Entity, EntityAlias, EntityIdentifier, EntityResolution, EntityType
from .normalization import normalize_entity_name
from .resolution import resolve_entity

__all__ = [
    "Entity",
    "EntityAlias",
    "EntityIdentifier",
    "EntityResolution",
    "EntityType",
    "normalize_entity_name",
    "resolve_entity",
]
