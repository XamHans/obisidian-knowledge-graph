---
type: tool
stability: evolving
as_of: 2026-06
reviewed: 2026-06
linked_hubs:
  - [[Hubs/RAG]]
---

## Definition
- Postgres extension that adds vector search to relational schemas for storing and querying embeddings.

## Capabilities
- Supports semantic similarity search over chunk embeddings used in RAG. *Source:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^rerank-stack]]
- Works with reranking by returning wide candidate sets for cross-encoders to filter. *Source:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^rerank-stack]]
- Handles parallel queries for multi-query RAG and expanded queries. *Source:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^multi-query]]

## Integration Patterns
- Store embeddings alongside chunk metadata (parent/child IDs, doc handles) to enable hierarchical pull-ups. *Source:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^hierarchical]]
- Combine with rerankers to control token load to the LLM. *Source:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^rerank-stack]]
- Fan out multi-query requests in parallel and merge results before reranking. *Source:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^multi-query]]

## Source Transcripts
- [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^rerank-stack]]
- [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^multi-query]]
- [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^hierarchical]]

## Related Concepts
- [[Concepts/RAG_Re_Ranking]]
- [[Concepts/Multi_Query_RAG]]
- [[Concepts/Hierarchical_RAG]]

## Linked Hubs
- [[Hubs/RAG]]
