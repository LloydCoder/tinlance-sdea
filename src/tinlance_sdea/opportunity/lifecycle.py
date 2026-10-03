"""Opportunity lifecycle transitions."""

from ..domain.models import LifecycleState

_ALLOWED: dict[LifecycleState, frozenset[LifecycleState]] = {
    LifecycleState.ACTIVE: frozenset(
        {LifecycleState.STALE, LifecycleState.RESOLVED, LifecycleState.EXPIRED}
    ),
    LifecycleState.STALE: frozenset(
        {LifecycleState.ACTIVE, LifecycleState.RESOLVED, LifecycleState.EXPIRED}
    ),
    LifecycleState.RESOLVED: frozenset({LifecycleState.SUPERSEDED}),
    LifecycleState.EXPIRED: frozenset({LifecycleState.SUPERSEDED}),
    LifecycleState.SUPERSEDED: frozenset(),
    LifecycleState.RETRACTED: frozenset(),
}


def transition(current: LifecycleState, target: LifecycleState) -> LifecycleState:
    if target == current or target in _ALLOWED[current]:
        return target
    raise ValueError(f"invalid opportunity transition: {current} -> {target}")
