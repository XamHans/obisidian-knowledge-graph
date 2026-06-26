---
type: concept
stability: stable
reviewed: 2026-06
hub: AI_Agents
evidence_status: needs_receipts
evidence_backlog:
  - Add transcript or paper receipts for this concept.
---

## Why It Matters
- Long-running agents fail when context grows faster than memory and retrieval policy can manage.

## Sub-Concept Map
- Working-memory boundaries
- Compaction and summarization loops
- State synchronization between tools and prompts
- Context freshness and conflict resolution

## Playbook Moves
- Define an explicit context budget and update policy per turn.
- Use rolling compaction plus retrieval checkpoints instead of replaying full history.
- Store durable state outside the prompt and rehydrate only task-relevant slices.

## Source Receipts
- Pending receipt linkage (`needs_receipts`).

## Connected Projects
- [[START_HERE]]

## Related Concepts
- [[Concepts/Agent_Memory_Patterns]]
- [[Concepts/Context_Window_And_Attention_Budget]]
- [[Concepts/Tool_Use_And_Action_Policies]]

> Related Hub: [[Hubs/AI_Agents]]
> Core Node: [[START_HERE]]
