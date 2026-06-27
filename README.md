# The AI Engineer — Knowledge Graph

A free, community-maintained reference vault for engineers building production AI systems. Curated by **Johannes Hayer** for [The AI Engineer](https://www.skool.com/ai-builders-6997/about) Skool community.

**Community:** [skool.com/ai-builders-6997](https://www.skool.com/ai-builders-6997/about) · **Slack:** [join](https://join.slack.com/t/j-hayer/shared_invite/zt-40wmmgk82-~j8H6fVycgya21bgsNsyOQ) · **Boilerplates:** [github.com/XamHans/boilerplates-skool](https://github.com/XamHans/boilerplates-skool)
**🔗 Live graph:** https://xamhans.github.io/obisidian-knowledge-graph/

---

## What is this?

A **connected map** of production-AI knowledge — concepts link to the tools that implement them. Not a course; the reference layer you keep open while you build.

It's built on the **[Open Knowledge Format (OKF)](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)** — plain Markdown with YAML frontmatter that publishes to an interactive graph.

**Why OKF?** So **AI agents can use this knowledge as effectively as possible.** Any agent — Claude, Cursor, Codex — reads the same standard bundle without translation and grounds its answers in curated, current, citeable sources, instead of guessing from memory.

## Structure
- `Concepts/` — durable theory (the "why")
- `Tools/` — concrete primitives (the "what")
- `Hubs/` — the navigation / index layer
- Private & local-only: `Sources/`, `Applied/`, `Daily_Notes/`

> **Status:** rebuilding on OKF, one cluster at a time. **RAG is live now**; more domains are being reworked.

## How to use it
- **Browse** on GitHub, **open in Obsidian** (Graph View), or **point an AI agent** at the folder.
- **Explore the [live graph](https://xamhans.github.io/obisidian-knowledge-graph/).**
- **Learn** with the `/teach` Claude Code skill — interactive lessons grounded in the vault.

## Contribute
PR a Concept or Tool — objective and technical, no project specifics. The repo ships Claude Code skills to make it easy:
- **`kg-ingest`** — capture a URL/transcript/paper into your private `Sources/`
- **`kg-contribute`** — promote general knowledge into a public note and open the PR (with a privacy gate)

Notes follow [CONVENTIONS.md](CONVENTIONS.md) (start from `Templates/`). CI validates every PR (OKF + privacy); on merge, the graph republishes. See [CONTRIBUTING.md](CONTRIBUTING.md).
