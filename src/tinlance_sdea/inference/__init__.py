"""Demand and capability inference contracts."""

from .calibration import calibration_error
from .capability import infer_capability
from .demand import infer_demand
from .explanations import InferenceExplanation
from .hypotheses import validate_hypothesis
from .model_gateway import InferenceModel
from .rules import rule_match
from .uncertainty import inference_uncertainty

__all__ = [
    "InferenceExplanation",
    "InferenceModel",
    "calibration_error",
    "infer_capability",
    "infer_demand",
    "inference_uncertainty",
    "rule_match",
    "validate_hypothesis",
]
