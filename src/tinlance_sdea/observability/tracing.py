"""Trace context contracts."""

from dataclasses import dataclass


@dataclass(frozen=True)
class TraceContext:
    trace_id: str
    span_id: str

    def __post_init__(self) -> None:
        if not self.trace_id.strip():
            raise ValueError("trace_id must be non-empty")
        if not self.span_id.strip():
            raise ValueError("span_id must be non-empty")

    def child(self, span_id: str) -> "TraceContext":
        return TraceContext(trace_id=self.trace_id, span_id=span_id)
