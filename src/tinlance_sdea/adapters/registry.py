"""Explicit signal-adapter registry."""

from __future__ import annotations

from .base import SignalAdapter


class AdapterRegistry:
    """Register and resolve adapters without embedding source logic in SDEA."""

    def __init__(self) -> None:
        self._adapters: dict[str, SignalAdapter] = {}

    def register(self, adapter: SignalAdapter) -> None:
        """Register an adapter by its unique name."""

        if adapter.name in self._adapters:
            raise ValueError(f"adapter already registered: {adapter.name}")
        self._adapters[adapter.name] = adapter

    def get(self, name: str) -> SignalAdapter:
        """Resolve an adapter by name."""

        try:
            return self._adapters[name]
        except KeyError as exc:
            raise KeyError(f"unknown signal adapter: {name}") from exc

    def all(self) -> tuple[SignalAdapter, ...]:
        """Return registered adapters in insertion order."""

        return tuple(self._adapters.values())
