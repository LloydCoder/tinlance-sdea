from datetime import UTC, datetime
from uuid import uuid4

import pytest

from tinlance_sdea.evaluation import (
    Adjudication,
    RegressionResult,
    benchmark_cases,
    brier,
    precision,
    recall,
)
from tinlance_sdea.outcomes import (
    OutcomeAttribution,
    attribute,
    feedback_label,
    improvement_delta,
    outcome_rate,
    record_event,
)


def test_outcome_event_attribution_and_feedback() -> None:
    opportunity_id = uuid4()
    event = record_event(
        opportunity_id, "accepted", datetime(2026, 10, 1, tzinfo=UTC)
    )
    assert event.opportunity_id == opportunity_id
    attribution = attribute(
        opportunity_id,
        event.id,
        0.9,
        "explicit customer acceptance",
    )
    assert isinstance(attribution, OutcomeAttribution)
    assert feedback_label(accepted=True, useful=True) == "positive"
    assert feedback_label(accepted=True, useful=False) == "accepted"
    assert feedback_label(accepted=False, useful=True) == "useful"
    assert feedback_label(accepted=False, useful=False) == "negative"


def test_outcome_learning() -> None:
    assert improvement_delta(0.4, 0.7) == pytest.approx(0.3)
    assert outcome_rate((True, False, True)) == pytest.approx(2 / 3)
    assert outcome_rate(()) == 0.0


def test_evaluation_metrics_and_calibration() -> None:
    predicted = (True, True, False, False)
    actual = (True, False, True, False)
    assert precision(predicted, actual) == pytest.approx(0.5)
    assert recall(predicted, actual) == pytest.approx(0.5)
    assert brier((0.8, 0.2), (True, False)) == pytest.approx(0.04)
    assert precision((), ()) == 0.0
    assert recall((), ()) == 0.0
    with pytest.raises(ValueError):
        precision((True,), (True, False))


def test_benchmark_and_adjudication_contracts() -> None:
    cases = benchmark_cases()
    assert cases[0].case_id == "SDEA-001"
    result = RegressionResult(case_id="SDEA-001", passed=True, score=1.0)
    assert result.passed
    adjudication = Adjudication(
        case_id="SDEA-001",
        decision="confirmed",
        reviewer="human",
        confidence=1.0,
    )
    assert adjudication.reviewer == "human"
