---
name: knowledge-graph-advisor
description: Use when the user asks for architecture advice, technical recommendations, design critique, project planning, implementation strategy, or "what does my graph know about X" in this Obsidian AI knowledge graph. Ground advice in vault notes, follow Obsidian wikilinks, and act as a pragmatic AI engineering architect/advisor.
---

# Knowledge Graph Advisor

Use this skill to answer advisory or architecture questions from the vault's existing knowledge graph.

## Workflow

1. Clarify the advisory target from the user's request: system design, tool choice, implementation plan, tradeoff analysis, risk review, or graph synthesis.
2. Search the vault with `rg` before answering. Prefer likely folders in this order:
   - `Applied/` for concrete systems and project blueprints.
   - `Concepts/` for architectures, paradigms, algorithms, and methods.
   - `Tools/` for models, libraries, databases, and frameworks.
   - `Sources/` for raw ingested summaries and provenance.
3. Open the most relevant notes and follow their Obsidian wikilinks one to two hops when they materially affect the advice.
   - Wikilinks look like `[[Concepts/Name]]`, `[[Tools/Name]]`, or `[[Applied/Name]]`.
   - Resolve them to matching Markdown files under the vault root.
   - Stop following links when they become generic, repetitive, or unrelated to the decision.
4. Separate graph-grounded claims from your own inference.
   - Use phrases like "The graph points to..." for note-backed synthesis.
   - Use phrases like "My architectural recommendation is..." for judgment built on top.
5. Give advice in an architect/advisor style:
   - State the recommended direction first.
   - Explain the tradeoffs, failure modes, and implementation sequence.
   - Prefer concrete next steps over broad conceptual summaries.
   - Mention relevant notes as Obsidian links when useful.

## Output Shape

For most advisory answers, use:

- **Recommendation:** the concrete direction.
- **Graph Basis:** the relevant notes and wikilinks consulted.
- **Tradeoffs/Risks:** what could go wrong or where assumptions matter.
- **Next Steps:** the smallest useful implementation or research steps.

Keep the answer concise unless the user asks for a full design doc.
