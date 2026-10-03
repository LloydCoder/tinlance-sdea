"""Replaceable model-inference interface."""

from abc import ABC, abstractmethod
from collections.abc import Mapping
from typing import Any


class InferenceModel(ABC):
    """Non-authoritative model interface."""

    @abstractmethod
    def infer(self, features: Mapping[str, Any]) -> Mapping[str, Any]:
        raise NotImplementedError
