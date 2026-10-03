# Domain Model

SDEA's canonical concepts are deliberately small and composable.

## Evidence
An externally sourced artifact or observation that can support reasoning. Evidence carries provenance, timestamps, source type, and optional content hashing.

## Signal
A normalized representation of a meaningful change or condition associated with an entity. A signal references evidence; it does not replace it.

## Signal Cluster
A temporally related set of signals that may collectively provide stronger support than any single signal.

## Demand Hypothesis
A falsifiable interpretation of signals describing a possible organizational capability demand. It is not a confirmed customer requirement.

## Capability Need
A normalized capability that may be required to address a demand hypothesis.

## Opportunity
A commercially actionable capability need with evidence, confidence, and potential acquisition paths.

## Buying Window
The estimated temporal interval in which the capability need is most actionable. It preserves uncertainty rather than pretending to know a customer's exact purchase date.

## Acquisition Recommendation
A recommendation for how the capability might be obtained: hire, build, buy, partner, fractional, FDE, project, managed service, AaaS, or product.

Recommendations do not authorize outreach or execution. Human approval and downstream governance remain separate concerns.