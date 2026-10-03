"""Capability ontology contracts."""

from pydantic import Field, model_validator

from ..contracts.versions import validate_version
from ..domain.models import SDEAModel


class Capability(SDEAModel):
    id: str
    name: str
    version: str
    parent_id: str | None = None
    aliases: tuple[str, ...] = ()
    metadata: dict[str, str] = Field(default_factory=dict)

    @model_validator(mode="after")
    def validate_capability(self) -> Capability:
        if not self.id.strip():
            raise ValueError("capability id must be non-empty")
        if not self.name.strip():
            raise ValueError("capability name must be non-empty")
        validate_version(self.version)
        if any(not alias.strip() for alias in self.aliases):
            raise ValueError("capability aliases must be non-empty")
        if self.parent_id == self.id:
            raise ValueError("capability cannot be its own parent")
        return self


class CapabilityMapping(SDEAModel):
    source: str
    capability_id: str
    confidence: float = Field(ge=0.0, le=1.0)
    rationale: str

    @model_validator(mode="after")
    def validate_mapping(self) -> CapabilityMapping:
        if not self.source.strip():
            raise ValueError("mapping source must be non-empty")
        if not self.capability_id.strip():
            raise ValueError("mapping capability_id must be non-empty")
        if not self.rationale.strip():
            raise ValueError("mapping rationale must be non-empty")
        return self
