# Vault Structure Overview

- All vault folders and notes use underscore-separated, TitleCased filenames (no spaces or dashes; keep acronyms uppercase).
- Every note carries `> Core Node: [[START_HERE]]` so the graph centers on the program.

The vault follows the **CAST taxonomy** with a public/private split (see `AGENTS.md` and `CONTRIBUTING.md`).

## Shared (public, tracked in Git)
- `Concepts/` – abstract theory: paradigms, algorithms, architectures, and methodologies, with hub backlinks and tool references.
- `Tools/` – concrete primitives: models, libraries, databases, and frameworks. Mark vendor/product-specific apps explicitly (e.g. `type: software`) to keep detection accurate.
- `Hubs/` – maps of content (MOCs) that anchor concept clusters and tool rollups per role. Hubs can nest via `parent_hub`/`child_hubs` front matter (e.g. Model_Context_Protocol → ChatGPT_Apps).
- `Assets/` – ready-to-use playbooks and operating manuals for autonomous helpers.

## Private (local only, gitignored)
- `Sources/` – raw ingested summaries and processed transcripts; your local library.
- `Applied/` – project blueprints and proprietary system designs.
- `Daily_Notes/` – working notes and scratch.

> Core Node: [[START_HERE]]
