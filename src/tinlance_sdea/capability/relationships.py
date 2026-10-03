"""Capability relationship primitives."""

from enum import StrEnum


class CapabilityRelation(StrEnum):
    PARENT = "parent"
    PREREQUISITE = "prerequisite"
    ADJACENT = "adjacent"


def related(
    capability_id: str, relation: CapabilityRelation, target_id: str
) -> tuple[str, str, str]:
    return capability_id, relation.value, target_id
