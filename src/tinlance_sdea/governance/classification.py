"""Data classification contracts."""

from enum import StrEnum


class DataClass(StrEnum):
    PUBLIC = "public"
    INTERNAL = "internal"
    CONFIDENTIAL = "confidential"
    RESTRICTED = "restricted"


def can_share(source: DataClass, target: DataClass) -> bool:
    order = {
        DataClass.PUBLIC: 0,
        DataClass.INTERNAL: 1,
        DataClass.CONFIDENTIAL: 2,
        DataClass.RESTRICTED: 3,
    }
    return order[target] <= order[source]
