from datetime import UTC, datetime, timedelta
from uuid import uuid4

import pytest

from tinlance_sdea.epistemics import (
    Contradiction,
    EpistemicAssessment,
    Uncertainty,
    assess,
    brier_score,
    combine_confidence,
    uncertainty_score,
)
from tinlance_sdea.fusion import (
    FusionExplanation,
    SignalGraph,
    build_graph,
    cluster_signals,
    correlate_signals,
    explain_cluster,
    find_contradictions,
    source_diversity,
    weight_signal,
)
from tinlance_sdea.signals import SignalType, normalize_signal
from tinlance_sdea.temporal import (
    TemporalRelation,
    TimeInterval,
    acceleration_ratio,
    decay_score,
    derive_window,
    persistence_count,
    persistence_span,
    recency_score,
    relate,
)


def signal(
    *,
    when: datetime,
    direction: str | None = None,
    entity: str = "org:example",
):
    attributes = {} if direction is None else {"direction": direction}
    return normalize_signal(
        entity_id=entity,
        signal_type=SignalType.HIRING,
        source_event_id=str(uuid4()),
        occurred_at=when,
        observed_at=when + timedelta(hours=1),
        evidence_ids=(uuid4(),),
        attributes=attributes,
    )


def test_temporal_primitives_and_relations() -> None:
    start = datetime(2026, 10, 1, tzinfo=UTC)
    end = datetime(2026, 10, 3, tzinfo=UTC)
    interval = TimeInterval(start=start, end=end)
    assert persistence_span((start, end)) == 172800.0
    assert persistence_count((start, end)) == 2
    assert acceleration_ratio(recent_count=4, prior_count=2) == 2.0
    assert acceleration_ratio(recent_count=2, prior_count=0) == 1.0
    assert decay_score(age_days=0, half_life_days=7) == pytest.approx(1.0)
    assert recency_score(observed_at=start, now=start, half_life_days=7) == pytest.approx(1.0)
    assert relate(interval, TimeInterval(start=end, end=end)) is TemporalRelation.CONTAINS
    assert derive_window(anchor=start, horizon_days=7).end == start + timedelta(days=7)
    with pytest.raises(ValueError):
        TimeInterval(start=end, end=start)


def test_fusion_correlates_clusters_and_builds_graph() -> None:
    base = datetime(2026, 10, 1, tzinfo=UTC)
    signals = (
        signal(when=base),
        signal(when=base + timedelta(days=1)),
        signal(when=base + timedelta(days=10)),
        signal(when=base, entity="org:other"),
    )
    pairs = correlate_signals(signals, timedelta(days=2))
    assert len(pairs) == 1
    clusters = cluster_signals(signals, timedelta(days=2))
    assert len(clusters) == 3
    graph = build_graph(signals, timedelta(days=2))
    assert isinstance(graph, SignalGraph)
    assert len(graph.nodes) == 4


def test_fusion_weight_diversity_contradiction_and_explanation() -> None:
    base = datetime(2026, 10, 1, tzinfo=UTC)
    up = signal(when=base, direction="increase")
    down = signal(when=base + timedelta(days=1), direction="decrease")
    assert find_contradictions((up, down)) == ((str(up.id), str(down.id)),)
    assert weight_signal(up, source_reliability=0.8) == pytest.approx(0.5333333333)
    assert source_diversity(["a", "b", "a", "c"]) == 1.0
    explanation = explain_cluster((str(up.id),), reasons=("same entity",))
    assert isinstance(explanation, FusionExplanation)
    with pytest.raises(ValueError):
        weight_signal(up, source_reliability=2.0)


def test_epistemic_contracts_and_calibration() -> None:
    assessment = assess(
        state=up_state(),
        confidence=0.75,
        rationale="two independent observations",
    )
    assert isinstance(assessment, EpistemicAssessment)
    uncertainty = Uncertainty(
        evidence_coverage=1.0,
        source_agreement=0.5,
        temporal_stability=0.5,
    )
    assert uncertainty_score(uncertainty) == pytest.approx(2 / 3)
    assert combine_confidence((0.5, 1.0)) == 0.75
    assert combine_confidence(()) == 0.0
    assert brier_score((0.8, 0.2), (True, False)) == pytest.approx(0.04)
    assert Contradiction(left_id="a", right_id="b", reason="opposite", severity=0.5).severity == 0.5
    with pytest.raises(ValueError):
        combine_confidence((1.1,))


def up_state():
    from tinlance_sdea.domain.models import EpistemicState

    return EpistemicState.CORROBORATED


def test_validation_errors_are_explicit() -> None:
    with pytest.raises(ValueError):
        brier_score((0.5,), ())
    with pytest.raises(ValueError):
        brier_score((1.2,), (True,))
    with pytest.raises(ValueError):
        acceleration_ratio(recent_count=-1, prior_count=1)
    with pytest.raises(ValueError):
        decay_score(age_days=-1, half_life_days=7)
