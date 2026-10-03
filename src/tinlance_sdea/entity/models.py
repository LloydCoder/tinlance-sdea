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


class Entity(SDEAModel):
    id: str
    entity_type: EntityType
    canonical_name: str
    identifiers: tuple[EntityIdentifier, ...] = ()
    aliases: tuple[EntityAlias, ...] = ()
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)
    metadata: dict[str, str] = Field(default_factory=dict)

    @model_validator(mode="after")
    def validate_name(self) -> Entity:
        if not self.canonical_name.strip():
            raise ValueError("canonical_name must be non-empty")
        return self


class EntityResolution(SDEAModel):
    id: UUID = Field(default_factory=uuid4)
    source_value: str
    entity_id: str
    method: str
    confidence: float = Field(ge=0.0, le=1.0)
    matched_identifier: EntityIdentifier | None = None
    rationale: str
