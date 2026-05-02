---
type: concept
status: active
hub: Generative_AI
persona: Professional Seeking AI Mastery
evidence_status: needs_receipts
evidence_backlog:
  - Add transcript receipts on context budgeting and token allocation.
---

## Why It Matters
- Context windows are finite; attention budget decisions determine whether critical evidence is available or silently dropped.

## Sub-Concept Map
- Token budget allocation across instructions, context, and output.
- Retrieval compression and reranking reduce context waste.
- Long-context models still require prioritization.
- Prompt structure impacts effective attention use.
- Cost and latency increase with larger context loads.
- KV cache size scales linearly with context length, creating a hard memory ceiling on concurrent sequences.
- Prefill latency grows with prompt length (quadratic attention computation), making context budget a direct latency lever.

## Playbook Moves
- Define fixed token budgets per workflow stage.
- Add reranking/summarization before context assembly.
- Track truncation and evidence-loss failures in logs.

## Source Transcripts
- Pending receipt linkage (`needs_receipts`).

## Connected Projects
- [[Projects/AI_Native_Engineer]]

## Linked Technologies
- [[Technologies/PGVector]]
- [[Technologies/Neon_Postgres]]

## Related Concepts
- [[Resources/Concepts/Transformer_Architecture]]
- [[Resources/Concepts/RAG_Re_Ranking]]
- [[Resources/Concepts/Hierarchical_RAG]]
- [[Resources/Concepts/KV_Cache_And_Prefill_Decode_Phases]]
- [[Resources/Concepts/LLM_Inference_Lifecycle]]

> Related Hub: [[Hubs/Generative_AI]]
> Core Node: [[Projects/AI_Native_Engineer]]
