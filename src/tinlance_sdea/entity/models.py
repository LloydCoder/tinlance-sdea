"""Canonical entity identity models."""

from __future__ import annotations

from enum import StrEnum
from uuid import UUID, uuid4

from pydantic import Field, model_validator

from ..domain.models import SDEAModel


class EntityType(StrEnum):
    ORGANIZATION = "organization"
    PERSON = "person"
    PRODUCT = "product"
    PROJECT = "project"
    DOMAIN = "domain"
    OTHER = "other"


class EntityIdentifier(SDEAModel):
    scheme: str
    value: str

    @model_validator(mode="after")
    def validate_non_empty(self) -> EntityIdentifier:
        if not self.scheme or not self.value:
            raise ValueError("entity identifier scheme and value must be non-empty")
        return self


class EntityAlias(SDEAModel):
    value: str
    source: str | None = None

    @model_validator(mode="after")
    def validate_value(self) -> EntityAlias:
        if not self.value.strip():
            raise ValueError("entity alias value must be non-empty")
        return self


class Entity(SDEAModel):
    id: str
    entity_type: EntityType
    canonical_name: str
    identifiers: tuple[EntityIdentifier, ...] = ()
    aliases: tuple[EntityAlias, ...] = ()
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)
    metadata: dict[str, str] = Field(default_factory=dict)

    @model_validator(mode="after")
    def validate_identity(self) -> Entity:
        if not self.id.strip():
            raise ValueError("entity id must be non-empty")
        if not self.canonical_name.strip():
            raise ValueError("canonical_name must be non-empty")
        keys = {(item.scheme.casefold(), item.value.casefold()) for item in self.identifiers}
        if len(keys) != len(self.identifiers):
            raise ValueError("entity identifiers must be unique")
        return self


class EntityResolution(SDEAModel):
    id: UUID = Field(default_factory=uuid4)
    source_value: str
    entity_id: str
    method: str
    confidence: float = Field(ge=0.0, le=1.0)
    matched_identifier: EntityIdentifier | None = None
    rationale: str

    @model_validator(mode="after")
    def validate_resolution(self) -> EntityResolution:
        if not self.source_value.strip():
            raise ValueError("source_value must be non-empty")
        if not self.entity_id.strip():
            raise ValueError("entity_id must be non-empty")
        if not self.method.strip():
            raise ValueError("method must be non-empty")
        if not self.rationale.strip():
            raise ValueError("rationale must be non-empty")
        return self
