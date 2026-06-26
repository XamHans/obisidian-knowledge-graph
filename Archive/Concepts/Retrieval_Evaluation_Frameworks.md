---
type: concept
stability: stable
reviewed: 2026-06
hub: RAG
evidence_status: needs_receipts
evidence_backlog:
  - Add transcript or paper receipts for this concept.
---

## Why It Matters
- Without retrieval-specific evaluation, teams misdiagnose whether failures come from search, ranking, or generation.

## Sub-Concept Map
- Ground-truth query-document pairs
- Recall at k and MRR style metrics
- Ablation testing for retrieval stages
- Regression suites for corpus updates

## Playbook Moves
- Build task-aligned retrieval test sets before tuning rerankers.
- Evaluate each retrieval stage independently to isolate bottlenecks.
- Run regression checks whenever index, chunking, or metadata changes.

## Source Receipts
- Pending receipt linkage (`needs_receipts`).

## Connected Projects
- [[START_HERE]]

## Related Concepts
- [[Concepts/Hybrid_Retrieval_And_Ranking]]
- [[Concepts/RAG_Evaluation_And_Groundedness]]
- [[Concepts/Metadata_Filtering_Strategies]]

> Related Hub: [[Hubs/RAG]]
> Core Node: [[START_HERE]]
