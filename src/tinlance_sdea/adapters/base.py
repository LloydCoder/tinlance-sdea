"""Signal adapter extension contract."""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Mapping
from typing import Any

from ..signals.models import SignalRecord


class SignalAdapter(ABC):
    """Translate one source family into canonical SDEA signals."""

    name: str
    source_types: frozenset[str]

    @abstractmethod
    def normalize(self, payload: Mapping[str, Any]) -> tuple[SignalRecord, ...]:
        """Normalize a source payload into canonical signals."""

    def supports(self, source_type: str) -> bool:
        """Return whether this adapter handles a source type."""

        return source_type in self.source_types
