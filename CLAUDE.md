# CLAUDE.md

An **Open Knowledge Format (OKF)** knowledge graph for production AI engineering. You author wikilink-native Markdown notes; `scripts/okf-build.py` generates the standards-compliant `okf/` bundle (published as an interactive graph on GitHub Pages). See `AGENTS.md` and `CONVENTIONS.md` for detail.

## Structure (type-first; links carry the graph)
- `Concepts/` — durable theory (the "why")
- `Tools/` — volatile concrete primitives (the "what")
- `Hubs/` — the `index.md` navigation / map-of-content layer
- **Private, gitignored:** `Sources/`, `Applied/`, `Daily_Notes/`, `Archive/` (pre-OKF corpus, reworked incrementally)

A note can belong to many topics — express that with links, not nested folders.

## Frontmatter (see `CONVENTIONS.md`)
Required `type`; authored `description` (one-line, progressive disclosure); `tags`; `stability` (`stable`/`evolving`/`volatile`) + `reviewed` (YYYY-MM); `evidence_status` for concepts. Start new notes from `Templates/`.

## Skills
- **`kg-ingest`** — ingest a URL/transcript/paper → a private `Sources/` receipt.
- **`kg-contribute`** — promote general knowledge → a public Concept/Tool and open a PR (runs a privacy gate).
- **`knowledge-graph-advisor`** — answer questions grounded in the graph.
- **`/teach`** — turn notes into interactive lessons.

## Commands
- `python3 scripts/okf-build.py` — build the OKF bundle
- `python3 scripts/okf-validate.py` — validate (OKF compliance + privacy); the CI gate
- `python3 scripts/okf-graph.py` — build the interactive `okf/graph.html`

## Rules
- **Public vs private:** collaborate on Concepts & Tools (objective, no project specifics). Never commit `Sources/`, `Applied/`, or `Daily_Notes/`.
- **Never hand-edit `okf/`** — it is generated. Members open PRs; CI validates; merge publishes.
- Keep links resolvable; broken forward-refs are OK (they mark rework candidates and degrade to plain text in the bundle).
