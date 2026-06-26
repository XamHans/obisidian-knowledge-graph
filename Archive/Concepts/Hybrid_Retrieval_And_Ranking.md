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
- Combining lexical and semantic retrieval with reranking improves robustness across exact-match and conceptual queries.

## Sub-Concept Map
- BM25 plus dense-vector retrieval
- Candidate fusion strategies
- Cross-encoder or LLM reranking
- Recall-precision tradeoff tuning

## Playbook Moves
- Generate a broad candidate set with hybrid retrieval before aggressive reranking.
- Tune candidate width and rerank thresholds with offline evals.
- Audit failures by query type to prevent one-size-fits-all settings.

## Source Receipts
- Pending receipt linkage (`needs_receipts`).

## Connected Projects
- [[START_HERE]]

## Related Concepts
- [[Concepts/RAG_Re_Ranking]]
- [[Concepts/Contextual_Retrieval]]
- [[Concepts/Query_Expansion_RAG]]

> Related Hub: [[Hubs/RAG]]
> Core Node: [[START_HERE]]
