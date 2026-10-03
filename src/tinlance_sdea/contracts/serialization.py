"""Canonical contract serialization."""

from collections.abc import Mapping
from typing import Any, cast


def serialize(model: Any) -> Mapping[str, Any]:
    if not hasattr(model, "model_dump"):
        raise TypeError("model must be a Pydantic model")
    return cast(Mapping[str, Any], model.model_dump(mode="json"))
