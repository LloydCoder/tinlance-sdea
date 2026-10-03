"""JSON Schema helpers."""

from typing import Any, cast


def json_schema(model: Any) -> dict[str, Any]:
    if not hasattr(model, "model_json_schema"):
        raise TypeError("model must be a Pydantic model")
    return cast(dict[str, Any], model.model_json_schema())
