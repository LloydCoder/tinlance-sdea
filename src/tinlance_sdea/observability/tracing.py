"""Trace context contracts."""

from dataclasses import dataclass


@dataclass(frozen=True)
class TraceContext:
    trace_id: str
    span_id: str

    def child(self, span_id: str) -> "TraceContext":
        return TraceContext(trace_id=self.trace_id, span_id=span_id)
