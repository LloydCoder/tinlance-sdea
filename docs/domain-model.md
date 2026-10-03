# Domain Model

SDEA's canonical domain model deliberately separates **observation, evidence, interpretation, capability, opportunity and action**.

The Python implementation in `src/tinlance_sdea/domain/models.py` is the current source of truth for implemented fields. This document explains the semantics and the intended evolution of those contracts.

## 1. Evidence

**Definition:** An externally sourced artifact or observation that can support reasoning.

Current contract fields include:

- `id`
- `source_type`
- `source_url`
- `observed_at`
- `collected_at`
- `title`
- `excerpt`
- `content_hash`
- `provenance_ref`
- `metadata`

### Rules

- Observation time and collection time are distinct.
- Evidence should identify where it came from when a source reference is available.
- Content hashes may support deduplication and integrity checks.
- Metadata is source-specific context, not a substitute for canonical fields.

## 2. Signal

**Definition:** A normalized representation of a meaningful change or condition associated with an entity.

Current contract fields include:

- `id`
- `entity_id`
- `signal_type`
- `state`
- `occurred_at`
- `observed_at`
- `evidence_ids`
- `attributes`

A signal is an interpretation of one or more observations into a stable semantic event. It must retain links to supporting evidence.

## 3. SignalCluster

**Definition:** A temporally related set of signals that may collectively provide stronger support than any individual signal.

Current contract fields include:

- `id`
- `entity_id`
- `signal_ids`
- `state`
- `first_observed_at`
- `last_observed_at`
- `confidence`

Future fusion work should add explicit provenance and contradiction semantics rather than relying only on confidence.

## 4. DemandHypothesis

**Definition:** A falsifiable interpretation of signals describing a possible organizational capability demand.

Current fields:

- `id`
- `entity_id`
- `statement`
- `state`
- `supporting_signal_ids`
- `confidence`
- `rationale`

A demand hypothesis is **not** a confirmed customer requirement.

Its rationale is mandatory because an inference without an explanation is difficult to audit, calibrate or correct.

## 5. CapabilityNeed

**Definition:** A normalized capability that may be required to address a demand hypothesis.

Current fields:

- `id`
- `entity_id`
- `capability`
- `demand_hypothesis_id`
- `confidence`
- `urgency`
- `why_now`

The capability field is intentionally normalized rather than tied to a job title, vendor or Tinlance service.

Future ontology work should support:

- capability families
- parent/child relationships
- synonyms
- adjacent capabilities
- required prerequisites
- confidence and versioning
- domain-specific overlays

## 6. BuyingWindow

**Definition:** An uncertainty-bearing temporal interval in which a capability need may be most actionable.

Current fields:

- `id`
- `status`
- `starts_at`
- `ends_at`
- `confidence`
- `rationale`

The window must not be presented as a guaranteed purchase date.

Future work should define a controlled status vocabulary and explicit derivation rules.

## 7. Opportunity

**Definition:** A commercially relevant capability need that remains traceable to evidence.

Current fields:

- `id`
- `entity_id`
- `capability_need_id`
- `state`
- `confidence`
- `buying_window_id`
- `acquisition_modes`
- `evidence_ids`
- `rationale`

An opportunity is not:

- a lead record
- a CRM contact
- a confirmed customer
- permission to contact an organization
- permission to execute technical work

The opportunity layer exists to provide a stable intelligence handoff to commercial systems.

## 8. AcquisitionRecommendation

**Definition:** An advisory recommendation for how a capability might be acquired.

Current fields:

- `opportunity_id`
- `mode`
- `confidence`
- `rationale`
- `requires_human_approval`

Supported acquisition modes currently include:

```text
hire
build
buy
partner
fractional
fde
project
managed_service
aaas
product
```

The recommendation does not authorize outreach, contracting, execution or deployment.

## 9. Evidence-state semantics

`EvidenceState` currently contains:

| State | Meaning |
|---|---|
| `observed` | Directly observed or captured |
| `corroborated` | Supported by multiple relevant observations |
| `inferred` | Derived from evidence through reasoning |
| `hypothesized` | Explicit but unconfirmed interpretation |
| `qualified` | Sufficiently supported for the relevant downstream qualification step |
| `confirmed` | Confirmed through an appropriate authoritative source or workflow |

These states describe epistemic status, not business priority.

## 10. Source taxonomy

`SourceType` currently includes:

```text
job_posting
funding
product_change
technology_change
leadership_change
expansion
security_event
regulatory_event
partnership
acquisition
procurement
open_source
other
```

The taxonomy is intentionally extensible. New source types should be introduced only when they represent a meaningful semantic class rather than a single website or provider.

## 11. Invariants

The current domain invariant layer requires:

1. An opportunity remains traceable to at least one evidence item.
2. A demand hypothesis has a non-empty rationale.

The models also enforce:

- immutable canonical objects
- forbidden unexpected fields
- confidence values between 0 and 1
- typed identifiers and timestamps

As the system matures, invariants should expand to cover:

- provenance integrity
- source/evidence deduplication
- temporal consistency
- contradiction representation
- capability ontology validity
- recommendation traceability
- contract-version compatibility

## 12. Canonical signal-intelligence layer

S2 introduces a source-normalized `SignalRecord` alongside the broader domain `Signal` contract.

A `SignalRecord` contains:

- canonical entity identity
- versioned signal type
- source event identifier
- occurrence and observation timestamps
- one or more evidence identifiers
- normalized scalar attributes
- optional deterministic fingerprint

The signal taxonomy is source-agnostic and currently versioned as `1.0.0`. Source adapters must map provider-specific payloads into these canonical types.

Signal identity is derived from stable semantic fields rather than collection UUIDs. Deduplication therefore removes repeated representations of the same normalized source event without deleting the underlying evidence.

## 13. Model boundary

The domain and signal contracts must remain independent of:

- CRM schemas
- outreach providers
- crawler implementations
- LLM provider APIs
- agent runtime APIs
- GitHub execution APIs
- database-specific persistence models

Adapters may map those systems into SDEA contracts, but the canonical domain should remain stable.
