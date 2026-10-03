"""In-memory capability ontology."""

from .models import Capability


class CapabilityOntology:
    """Versioned capability registry."""

    def __init__(self, capabilities: tuple[Capability, ...] = ()) -> None:
        self._items = {item.id: item for item in capabilities}

    def add(self, capability: Capability) -> None:
        if capability.id in self._items:
            raise ValueError(f"capability already exists: {capability.id}")
        self._items[capability.id] = capability

    def get(self, capability_id: str) -> Capability:
        try:
            return self._items[capability_id]
        except KeyError as exc:
            raise KeyError(f"unknown capability: {capability_id}") from exc

    def all(self) -> tuple[Capability, ...]:
        return tuple(self._items.values())
