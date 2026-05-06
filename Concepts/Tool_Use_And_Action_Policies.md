---
type: concept
status: active
hub: AI_Agents
persona: Professional Seeking AI Mastery
evidence_status: needs_receipts
evidence_backlog:
  - Add transcript receipts covering tool routing policy and safety constraints.
---

## Why It Matters
- Action policies decide when agents should call tools, abstain, or escalate, which directly affects safety and reliability.

## Sub-Concept Map
- Tool selection criteria by task intent.
- Preconditions for side-effecting actions.
- Policy boundaries and denied operations.
- Recovery paths for tool failures.
- Human-in-the-loop checkpoints.

## Playbook Moves
- Define per-tool call eligibility and disallowed conditions.
- Require validation before mutating actions.
- Log policy violations as first-class incidents.

## Source Transcripts
- Pending receipt linkage (`needs_receipts`).

## Connected Projects
- [[START_HERE]]

## Linked Technologies
- [[Tools/FastMCP]]
- [[Tools/Model_Context_Protocol]]

## Related Concepts
- [[Concepts/Tool_Calling_Failure_Modes]]
- [[Concepts/Tool_Schema_Design_For_Agent_Tools]]
- [[Concepts/Tool_Calling_Guardrails_And_Recovery]]
- [[Concepts/Multi_Agent_Coordination]]

> Related Hub: [[Hubs/AI_Agents]]
> Core Node: [[START_HERE]]
