"""Capability ontology contracts."""

from pydantic import Field
from ..domain.models import SDEAModel


class Capability(SDEAModel):
    id: str
    name: str
    version: str
    parent_id: str | None = None
    aliases: tuple[str, ...] = ()
    metadata: dict[str, str] = Field(default_factory=dict)


class CapabilityMapping(SDEAModel):
    source: str
    capability_id: str
    confidence: float = Field(ge=0.0, le=1.0)
    rationale: str
