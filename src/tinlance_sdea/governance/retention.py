"""Retention policy primitives."""

from dataclasses import dataclass


@dataclass(frozen=True)
class RetentionPolicy:
    days: int
    deletion_required: bool = True

    def validate(self) -> None:
        if self.days < 0:
            raise ValueError("retention days cannot be negative")
