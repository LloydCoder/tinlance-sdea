"""Adapter capability metadata."""

from pydantic import Field

from ..domain.models import SDEAModel


class AdapterCapability(SDEAModel):
    """Declarative source-adapter capability metadata."""

    adapter_name: str
    source_types: frozenset[str] = frozenset()
    version: str
    enabled: bool = True
    max_batch_size: int = Field(default=100, ge=1)
