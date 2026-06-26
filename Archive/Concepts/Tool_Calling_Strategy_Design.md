---
type: concept
stability: stable
reviewed: 2026-06
hub: Agent_Tool_Calling
evidence_status: needs_receipts
evidence_backlog:
  - Add transcript or paper receipts for this concept.
---

## Why It Matters
- Tool calling quality is determined as much by routing policy and orchestration as by schema correctness.

## Sub-Concept Map
- Tool selection vs tool execution stages
- Clarification before action for ambiguous intent
- Parallel vs sequential tool orchestration
- Fallback and abstain policies

## Playbook Moves
- Route through explicit intent classes before exposing large tool sets.
- Force clarification when confidence is low or side effects are high.
- Treat abstain as a first-class outcome to avoid unsafe or low-confidence calls.

## Source Receipts
- Pending receipt linkage (`needs_receipts`).

## Connected Projects
- [[START_HERE]]

## Related Concepts
- [[Concepts/Tool_Calling_Failure_Modes]]
- [[Concepts/Tool_Schema_Design_For_Agent_Tools]]
- [[Concepts/Tool_Calling_Guardrails_And_Recovery]]

> Related Hub: [[Hubs/Agent_Tool_Calling]]
> Core Node: [[START_HERE]]
