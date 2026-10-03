"""Acquisition constraints."""

from collections.abc import Iterable

from .models import AcquisitionConstraint


def allowed_modes(constraints: Iterable[AcquisitionConstraint]) -> tuple[AcquisitionConstraint, ...]:
    return tuple(item for item in constraints if item.allowed)
