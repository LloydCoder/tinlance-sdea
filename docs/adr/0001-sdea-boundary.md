# ADR 0001 — SDEA Permanent Boundary

- **Status:** Accepted
- **Date:** 2026-09-30
- **Decision:** SDEA is a permanent first-class Tinlance repository and shared intelligence layer.

## Context

Tinlance needs a durable system that can reason from observable organizational change to capability demand and commercial opportunity.

The capability overlaps with TADS, ReconOS, FadeReach, FDSE/FDE and the Tinlance Agent Platform/OS, but none of those systems should absorb the responsibility by duplication.

Because SDEA semantics are expected to be reused across multiple products and acquisition channels, placing them permanently inside a single consumer would make the domain harder to evolve and would encourage product-specific coupling.

## Decision

SDEA remains a dedicated repository:

`LloydCoder/tinlance-sdea`

SDEA owns:

- signal semantics and normalization
- evidence and provenance semantics
- signal fusion and correlation
- temporal reasoning
- demand hypotheses
- capability ontology and inference
- opportunity intelligence
- buying-window semantics
- acquisition-mode recommendations
- evaluation and calibration
- integration contracts

TADS is a primary consumer and product/workflow layer, not the parent of SDEA.

## Permanent boundaries

SDEA does not own:

- CRM functionality
- outbound messaging or outreach execution
- generic scraping infrastructure
- deep account reconnaissance
- engineering execution
- agent runtime authority
- identity or authorization
- approvals
- sandbox execution
- production customer changes

Those responsibilities remain with the appropriate Tinlance system.

## Consequences

### Positive

- SDEA semantics can serve multiple Tinlance products.
- TADS can evolve without owning the intelligence core.
- ReconOS can provide reconnaissance without becoming the demand-inference engine.
- FadeReach can consume opportunities without redefining how opportunities are inferred.
- FDSE/FDE can execute delivery without owning acquisition intelligence.
- Agent Platform remains the authoritative governed execution layer.

### Costs

- SDEA requires explicit versioned contracts.
- Cross-repository integration work is unavoidable.
- Domain semantics must be maintained independently from product UI.
- Evaluation becomes a first-class engineering responsibility.

## Alternatives considered

### Keep SDEA permanently inside TADS

Rejected because it couples reusable intelligence semantics to one product and makes other consumers depend on TADS.

### Put SDEA inside ReconOS

Rejected because reconnaissance/enrichment and demand inference are related but distinct responsibilities.

### Put SDEA inside FadeReach

Rejected because engagement should consume qualified intelligence rather than define it.

### Make SDEA a generic scraping/lead-generation repository

Rejected because collection is an input mechanism, not the core domain.

## Architectural test

If a proposed SDEA feature primarily answers:

- "What did we observe?"
- "What does the evidence support?"
- "What capability might be needed?"
- "Why now?"
- "What acquisition path could address it?"

it is likely within SDEA.

If it primarily answers:

- "Who should we contact?"
- "How do we send the message?"
- "How do we execute engineering work?"
- "Who is authorized to perform this action?"

it belongs elsewhere.

## Review rule

Any proposal that changes this boundary should create a new ADR or explicitly supersede this one.
