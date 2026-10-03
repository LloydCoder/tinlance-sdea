"""Deterministic entity-name normalization helpers."""

import unicodedata


def normalize_entity_name(value: str) -> str:
    """Normalize an entity name for comparison without discarding Unicode text."""

    normalized = unicodedata.normalize("NFKC", value).casefold().strip()
    output: list[str] = []
    previous_space = False
    for char in normalized:
        category = unicodedata.category(char)
        if category[0] in {"L", "N"}:
            output.append(char)
            previous_space = False
        else:
            if not previous_space:
                output.append(" ")
            previous_space = True
    return "".join(output).strip()
