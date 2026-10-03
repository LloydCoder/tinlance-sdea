"""Registry for canonical signal types."""

from __future__ import annotations

from .taxonomy import SignalType


class SignalRegistry:
    """Explicit registry preventing accidental taxonomy drift."""

    def __init__(self) -> None:
        self._types: dict[str, SignalType] = {item.value: item for item in SignalType}

    def get(self, signal_type: str) -> SignalType:
        """Return a registered signal type or raise ValueError."""

        try:
            return self._types[signal_type]
        except KeyError as exc:
            raise ValueError(f"unknown signal type: {signal_type}") from exc

    def values(self) -> tuple[SignalType, ...]:
        """Return all registered canonical signal types."""

        return tuple(self._types.values())
