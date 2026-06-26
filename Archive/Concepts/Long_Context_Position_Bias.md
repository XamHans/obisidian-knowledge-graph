---
type: concept
stability: stable
reviewed: 2026-06
hub: Generative_AI
evidence_status: needs_receipts
evidence_backlog:
  - Add transcript or paper receipts for this concept.
---

## Why It Matters
- Models often overweight beginning and ending spans, causing key evidence in the middle of long prompts to be ignored.

## Sub-Concept Map
- Lost-in-the-middle effects
- Evidence placement strategy
- Retrieval ordering and salience marking
- Context compaction for central facts

## Playbook Moves
- Place critical evidence near prompt regions with highest attention utility.
- Use salience markers and explicit citation requirements.
- Reduce prompt bloat so key facts are not buried in long context.

## Source Receipts
- Pending receipt linkage (`needs_receipts`).

## Connected Projects
- [[START_HERE]]

## Related Concepts
- [[Concepts/Context_Window_And_Attention_Budget]]
- [[Concepts/Context_Engineering_For_Long_Running_Agents]]
- [[Concepts/Long_Context_Vs_RAG_Decisions]]

> Related Hub: [[Hubs/Generative_AI]]
> Core Node: [[START_HERE]]
