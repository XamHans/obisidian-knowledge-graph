---
type: technology
status: active
linked_hubs:
  - [[Hubs/RAG]]
---

## Definition
- Serverless Postgres platform used with PGVector to store chunk tables and document metadata for RAG pipelines.

## Capabilities
- Scales Postgres storage/compute independently while supporting PGVector extensions for semantic search.
- Supports multi-table setups (chunk + document metadata) that agentic routing and hierarchical RAG depend on. *Source:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^agentic-routing]]
- Works with reranking flows by returning wide candidate sets quickly before cross-encoder filtering. *Source:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^rerank-stack]]

## Integration Patterns
- Pair a chunk table (with embeddings, metadata, parent-child IDs) with a document table for whole-file fetches in agentic or hierarchical RAG. *Source:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^hierarchical]]
- Expose both semantic search and full-document read endpoints so agents can switch retrieval modes. *Source:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^agentic-routing]]
- Tune candidate width for reranking to balance recall vs token budget before passing to the LLM. *Source:* [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^rerank-stack]]

## Source Transcripts
- [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^agentic-routing]]
- [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^hierarchical]]
- [[Resources/Processed_Transcripts/RAG_Strategies_Playbook#^rerank-stack]]

## Related Concepts
- [[Concepts/Agentic_RAG]]
- [[Concepts/Hierarchical_RAG]]
- [[Concepts/RAG_Re_Ranking]]

## Linked Hubs
- [[Hubs/RAG]]
