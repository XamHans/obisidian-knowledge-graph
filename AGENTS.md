# AI Knowledge Graph — Agent Guide

An **Open Knowledge Format (OKF)** knowledge graph for production AI engineering. Source notes are wikilink-native Markdown; `scripts/okf-build.py` generates the standard `okf/` bundle, published as an interactive graph on GitHub Pages. Full schema: `CONVENTIONS.md`.

## Structure (type-first; links carry the graph)
- `Concepts/` — durable theory (the "why")
- `Tools/` — volatile concrete primitives (the "what")
- `Hubs/` — the `index.md` navigation / map-of-content layer
- **Private, gitignored:** `Sources/`, `Applied/`, `Daily_Notes/`, `Archive/`

A note can belong to many topics — express that with links, not nested folders.

## Frontmatter (see `CONVENTIONS.md`)
Required `type`; authored `description` (progressive disclosure); `tags`; `stability` + `reviewed` (freshness); `evidence_status` for concepts. Start new notes from `Templates/`.

## Skills
- `kg-ingest` — raw content (URL/transcript/paper) → private `Sources/` receipt
- `kg-contribute` — promote general knowledge → public Concept/Tool + PR (privacy gate)
- `knowledge-graph-advisor` — answer questions grounded in the graph
- `/teach` — turn notes into interactive lessons

## Commands
- `python3 scripts/okf-build.py` — build the OKF bundle
- `python3 scripts/okf-validate.py` — validate (OKF + privacy); the CI gate
- `python3 scripts/okf-graph.py` — build the interactive graph

## Rules
- **Public vs private:** collaborate on objective Concepts & Tools (no project specifics). Never commit `Sources/`, `Applied/`, or `Daily_Notes/`.
- **Never hand-edit `okf/`** — it is generated. Members open PRs; CI validates; merge publishes.
