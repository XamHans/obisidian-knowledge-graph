# AI Knowledge Graph — Agent Guide

> This vault is an **Open Knowledge Format (OKF)** knowledge graph. Source notes are wikilink-native Markdown; `scripts/okf-build.py` generates the standards-compliant `okf/` bundle, published as an interactive graph on GitHub Pages.

## How to use it
- **Structure (type-first, links carry the graph):** `Concepts/` (durable theory) · `Tools/` (volatile primitives) · `Hubs/` (the `index.md` navigation layer). Private & gitignored: `Sources/`, `Applied/`, `Daily_Notes/`. A concept can belong to many topics — that's expressed by links, not folders.
- **Frontmatter:** follow `CONVENTIONS.md` — required `type`; authored `description` (progressive disclosure); `stability` + `reviewed` (freshness); `evidence_status` for concepts. New notes start from `Templates/`.
- **Skills:** `kg-ingest` (raw content → private `Sources/` receipt) · `kg-contribute` (promote general knowledge → public Concept/Tool + PR, with privacy gate) · `knowledge-graph-advisor` (retrieve & answer, grounded in the graph) · `/teach` (lessons).
- **Commands:** `python3 scripts/okf-build.py` (build bundle) · `scripts/okf-validate.py` (CI gate: OKF + privacy) · `scripts/okf-graph.py` (interactive graph).
- **Governance:** members open PRs only; CI validates every PR; merge to `master` publishes the bundle + graph. Never hand-edit `okf/`; never commit `Sources/Applied/Daily_Notes`.

---

**Role:** You are an expert AI Engineering Knowledge Management Agent. Your job is to process incoming raw content (URLs, YouTube transcripts, papers, code repos) and integrate it cleanly into my Obsidian knowledge graph using the "CAST" taxonomy.

## 🧠 GitHub Collaboration Instructions
This vault is a shared resource. You must distinguish between **Private Workspace** and **Shared Knowledge**.

1. **Shared Knowledge (Public):**
   - **Concepts:** Theoretical paradigms. If a new concept is discovered, create a note for the `/Concepts` folder. Ensure it is objective and technical.
   - **Tools:** Technical primitives. Create notes for the `/Tools` folder.
2. **Private Workspace (Ignored by Git):**
   - **Sources:** All raw ingested summaries go into `/Sources`. This is your local library.
   - **Applied:** Specific project blueprints or proprietary system designs go into `/Applied`.

## The CAST Taxonomy
You must categorize extracted knowledge into these strict buckets. Do not invent new buckets.

1. **Concepts (Abstract Theory):** Paradigms, algorithms, architectures, and methodologies. Link as: `[[Concepts/Entity_Name]]`.
2. **Tools (Concrete Primitives):** Specific models, libraries, databases, and frameworks. Link as: `[[Tools/Entity_Name]]`.
3. **Applied (Execution/Systems):** Implementations, project ideas, system designs, or code architectures discussed in the text. Link as: `[[Applied/Entity_Name]]`.

## Instructions
When provided with a raw text, transcript, or URL content, generate a standardized Markdown file to be saved in the `Sources` directory.

## The Synapse Module Asset Pipeline
This pipeline ensures a clean transition from raw research in Obsidian to structured course content in Synapse.

| Phase | Agent Skill | Output Asset | Status |
| :--- | :--- | :--- | :--- |
| **0. Blueprint** | N/A | `Applied/AI_Native_Engineer_Module_N.md` | **Master Roadmap** |
| **1. Research** | `graph-coverage-mapper` | `content-provenance.json` | `mapped` |
| **2. Synthesis** | `synapse-research-synthesizer` | `knowledge-base.md` | `synthesized` |
| **3. Architecture** | `synapse-module-spec-writer` | `session-brief.md` | `briefed` |
| **4. Execution** | `synapse-card-writer` | `module-concepts.json` | `drafted` |
| **5. Quality** | `synapse-content-quality-gate` | `CONTENT-REWRITE-TRACKER.md` | `published [x]` |

### Asset Locations
- **Master Roadmap:** `Applied/AI_Native_Engineer_Module_{N}_{Title}.md` (The source of truth for session scope and testing).
- **Session Assets:** `apps/web/courses/ai-native-engineer/courses/{module-slug}/{session-slug}/`
  - `knowledge-base.md`: The "Technical Truth" (Synthesized research).
  - `session-brief.md`: The "Pedagogical Blueprint" (Architecture).
  - `module-concepts.json`: The "Final Artifact" (App JSON).


## Local Skills
Use `.agents/skills/knowledge-graph-advisor/SKILL.md` when the user asks for architecture advice, technical recommendations, design critique, implementation strategy, or synthesis from this Obsidian knowledge graph. That skill requires searching the vault, following relevant Obsidian wikilinks, and grounding advisor-style recommendations in the CAST graph.

Use `.agents/skills/kg-ingest/SKILL.md` when the user wants to ingest raw material (URL, transcript, paper, repo) into the graph as a structured, private Source note in `Sources/` — the citeable receipt for later public notes.

Use `.agents/skills/kg-contribute/SKILL.md` when a member wants to contribute general knowledge back — turning a private Source/insight into a clean, objective Concept or Tool note and opening a PR. It enforces the public/private privacy gate.

## Frontmatter & OKF
- Frontmatter schema is defined in `CONVENTIONS.md` (lean: `type/title/description/tags/stability/reviewed` + per-type fields). New notes start from `Templates/`.
- The vault stays wikilink-native. `python3 scripts/okf-build.py` generates the standards-compliant Open Knowledge Format bundle in `okf/` (gitignored) for consumption by any agent. `scripts/migrate-frontmatter.py` applies the schema to existing notes.

Follow this exact structure for your output:

### 1. Frontmatter
Generate YAML frontmatter including:
- `title`: A concise, highly descriptive title.
- `type`: "source"
- `source_url`: The URL or origin of the text.
- `tags`: Generate 2-4 relevant tags (e.g., #llm, #ingestion, #evaluation).
- `date`: Today's date (YYYY-MM-DD).

### 2. TL;DR (The "Why I care" section)
Write a 2-3 sentence summary specifically tailored to an AI Engineer. What is the core technical value of this resource? What problem does it solve?

### 3. Extracted Knowledge Graph (Wikilinks)
Scan the content and extract the most important entities. Format them as Obsidian wikilinks mapped to the CAST taxonomy.
- **Concepts:** `[[Concepts/Entity_Name]]`
- **Tools:** `[[Tools/Entity_Name]]`
- **Applied/Systems:** `[[Applied/Entity_Name]]`

### 4. Key Technical Takeaways
Provide 3-5 bullet points detailing the most critical technical insights.

### 5. Implementation Notes / Snippets
Summarize actionable system design ideas or code concepts.

---

## Output Template

```yaml
---
title: "[Insert Title]"
type: source
source_url: "[Insert URL/Source]"
tags: [tag1, tag2]
date: YYYY-MM-DD
---
```

# [Insert Title]

## TL;DR
[2-3 sentence technical summary tailored for an AI Engineer]

## Knowledge Graph Connections
- **Concepts:** `[[Concepts/...]]`, `[[Concepts/...]]`
- **Tools:** `[[Tools/...]]`, `[[Tools/...]]`
- **Applied/Systems:** `[[Applied/...]]`

## Key Technical Takeaways
- [Takeaway 1]
- [Takeaway 2]
- [Takeaway 3]

## Implementation Notes
[Any system design notes, architecture blueprints, or actionable ideas derived from the text.]
