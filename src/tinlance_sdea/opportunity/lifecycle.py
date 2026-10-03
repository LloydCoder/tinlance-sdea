"""Opportunity lifecycle transitions."""

from ..domain.models import LifecycleState

_ALLOWED: dict[LifecycleState, frozenset[LifecycleState]] = {
    LifecycleState.ACTIVE: frozenset(
        {
            LifecycleState.STALE,
            LifecycleState.RESOLVED,
            LifecycleState.EXPIRED,
            LifecycleState.SUPERSEDED,
            LifecycleState.RETRACTED,
        }
    ),
    LifecycleState.STALE: frozenset(
        {
            LifecycleState.ACTIVE,
            LifecycleState.RESOLVED,
            LifecycleState.EXPIRED,
            LifecycleState.SUPERSEDED,
            LifecycleState.RETRACTED,
        }
    ),
    LifecycleState.RESOLVED: frozenset({LifecycleState.SUPERSEDED, LifecycleState.RETRACTED}),
    LifecycleState.EXPIRED: frozenset({LifecycleState.SUPERSEDED, LifecycleState.RETRACTED}),
    LifecycleState.SUPERSEDED: frozenset({LifecycleState.RETRACTED}),
    LifecycleState.RETRACTED: frozenset(),
}


def transition(current: LifecycleState, target: LifecycleState) -> LifecycleState:
    """Apply an explicit, auditable opportunity lifecycle transition."""

    if target == current or target in _ALLOWED[current]:
        return target
    raise ValueError(f"invalid opportunity transition: {current} -> {target}")
