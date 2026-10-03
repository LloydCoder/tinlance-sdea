# Architecture Decision Records

Architecture Decision Records (ADRs) capture durable decisions that should survive implementation changes and contributor turnover.

## When to create an ADR

Create an ADR when a decision:

- changes a repository or system boundary;
- introduces a durable dependency;
- changes canonical domain semantics;
- creates a new authority boundary;
- changes the integration direction between Tinlance systems;
- introduces a significant security, privacy or governance trade-off;
- would otherwise be likely to be reconsidered repeatedly.

Do **not** use ADRs for routine implementation details.

## Required structure

Each ADR should contain:

1. **Context** — the problem and constraints.
2. **Decision** — the chosen architecture.
3. **Consequences** — what becomes easier, harder or different.
4. **Alternatives considered** — credible alternatives and why they were not selected.
5. **Status** — proposed, accepted, superseded or deprecated.

## Rules

- ADRs describe decisions, not implementation tutorials.
- ADRs should use precise ownership language.
- A superseded ADR remains in the repository for historical traceability.
- New ADRs must not silently contradict an accepted ADR; explicitly supersede it.
- Domain-contract changes should reference the relevant ADR when they alter semantics.
- Boundary changes should be reviewed against `docs/architecture.md` and `README.md`.

## Current ADRs

- [0001 — SDEA permanent boundary](0001-sdea-boundary.md)
