# RAG And Knowledge Systems Experiment Prompts

## Beginner
- Compare fixed-size chunking vs context-aware chunking on the same corpus.
- Evaluate top-k retrieval quality before and after reranking.
- Build a citation-required answering flow and measure unsupported-claim rate.

## Intermediate
- Test hybrid retrieval against vector-only retrieval by query type.
- Measure answer groundedness with retrieval and generation metrics separated.
- Run query rewriting plus multi-query expansion and track recall lift.

## Advanced
- Benchmark long-context-only vs RAG pipeline on identical tasks and budgets.
- Design a freshness pipeline that reindexes changed knowledge without full rebuilds.
- Define RAG access control checks for multi-tenant or sensitive knowledge stores.

## Execution Rule
- For each run, capture retrieval candidates, rerank scores, final citations, and failure class.

> Core Node: [[Projects/AI_Native_Engineer]]
