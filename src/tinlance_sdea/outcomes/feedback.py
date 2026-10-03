"""Outcome feedback classification."""


def feedback_label(*, accepted: bool, useful: bool) -> str:
    if accepted and useful:
        return "positive"
    if accepted:
        return "accepted"
    if useful:
        return "useful"
    return "negative"
