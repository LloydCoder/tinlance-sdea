"""In-memory capability ontology."""

from .models import Capability


class CapabilityOntology:
    """Versioned capability registry with parent-integrity checks."""

    def __init__(self, capabilities: tuple[Capability, ...] = ()) -> None:
        self._items: dict[str, Capability] = {}
        for capability in capabilities:
            self.add(capability)

    def add(self, capability: Capability) -> None:
        if capability.id in self._items:
            raise ValueError(f"capability already exists: {capability.id}")
        if capability.parent_id is not None and capability.parent_id not in self._items:
            raise ValueError(f"unknown parent capability: {capability.parent_id}")
        self._items[capability.id] = capability
        self._validate_acyclic()

    def get(self, capability_id: str) -> Capability:
        try:
            return self._items[capability_id]
        except KeyError as exc:
            raise KeyError(f"unknown capability: {capability_id}") from exc

    def all(self) -> tuple[Capability, ...]:
        return tuple(self._items.values())

    def _validate_acyclic(self) -> None:
        for capability in self._items.values():
            seen: set[str] = set()
            current = capability.parent_id
            while current is not None:
                if current in seen:
                    raise ValueError("capability parent relationships contain a cycle")
                seen.add(current)
                parent = self._items.get(current)
                if parent is None:
                    raise ValueError(f"unknown parent capability: {current}")
                current = parent.parent_id
