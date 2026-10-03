# SDEA Architecture

## Mission

SDEA converts externally observable organizational change into evidence-backed capability-demand intelligence and qualified acquisition opportunities.

## Canonical pipeline

Entity/Event → Signal → Evidence → Signal Cluster → Demand Hypothesis → Capability Need → Opportunity → Buying Window → Acquisition Recommendation → Approved Engagement

## Repository boundaries

| System | Owns |
|---|---|
| SDEA | signal semantics, evidence/provenance, fusion, temporal reasoning, demand/capability inference, opportunity intelligence, acquisition recommendations and evaluation |
| TADS | demand-intelligence product experience and workflows |
| ReconOS | account/company reconnaissance and enrichment |
| FadeReach | engagement and outreach execution |
| FDSE/FDE | engineering execution and delivery semantics |
| Agent Platform | authoritative identity, authorization, approval, runtime, tools, sandbox, budgets, evidence, audit and observability |
| Agent OS | higher-level agent/workspace lifecycle and operating environment |

SDEA must consume these systems through explicit interfaces. It must not reimplement their authority.

## Evidence discipline

signal ≠ evidence

evidence ≠ demand

demand ≠ capability

capability ≠ opportunity

opportunity ≠ customer

Every consequential inference should remain traceable to supporting evidence. Uncertainty must be representable; absence of evidence must not silently become evidence of absence.

## Integration direction

TADS / ReconOS / domain adapters → SDEA → Opportunity → FadeReach → FDSE/FDE, AaaS or Product

SDEA is a shared intelligence layer, not a CRM, outreach system, agent runtime, or engineering execution engine.