# AI Engineering Shared Brain

This is an Obsidian-based knowledge graph designed specifically for **AI Engineers**. It uses the **CAST** abstraction to turn raw technical content into a high-density, reusable intelligence layer for humans and AI Agents.

## Start Here

If you are coming from The AI Engineer Skool community, begin with [[START_HERE]].

Core entry points:
- [[Hubs/AI_Concept_Universe]]: full curriculum map.
- [[Hubs/AI_Agents]]: agent architectures, planning, memory, tool use, governance, and evals.
- [[Hubs/RAG]]: retrieval strategies, chunking, reranking, groundedness, and graph-based retrieval.
- [[Hubs/Model_Context_Protocol]]: MCP servers, transports, deployment, and host integration.
- [[Hubs/Agent_Tool_Calling]]: tool schemas, routing reliability, recovery, and guardrails.
- [[Hubs/LLM_Evals]]: eval engineering, LLM judges, agreement metrics, and trace debugging.

## The Core Idea: Physics vs. Execution
Most knowledge bases fail because they mix timeless theory with transient project notes. This vault solves that by splitting knowledge into a **Shared Core** (Theory/Primitives) and a **Private Layer** (Project Execution).

### The CAST Taxonomy
- **[C]oncepts (Theory):** The abstract "physics" of AI (e.g., RAG, LoRA, KV Caching). *Shared/Public.*
- **[A]pplied (Execution):** Where theory meets reality. System designs and specific project blueprints. *Private/Local.*
- **[S]ources (Library):** The permanent home for processed transcripts, papers, and raw data. *Private/Local.*
- **[T]ools (Primitives):** The concrete software and models (e.g., LangChain, vLLM, ChromaDB). *Shared/Public.*

---

## How to Use with Obsidian
1. **Clone & Open:** Clone this repo and open the folder as a "Vault" in [Obsidian](https://obsidian.md/).
2. **The Graph View:** Open the Graph View to see how `Concepts` link to `Tools`.
3. **Dangling Links:** Ingestion creates "dangling links" (wikilinks to files that don't exist yet). Click them to create new canonical notes in `/Concepts` or `/Tools`.

---

## Working with AI Agents (Claude Code / Codex / CLI)
This vault is designed to be **Agent-Native**. It provides a structured context window for your AI tools.

### 1. Ingesting New Data
When you find a YouTube video or research paper:
1. Copy the content/transcript.
2. Feed the prompt in `AGENTS.md` to your agent.
3. The agent will output a standardized Markdown file.
4. Save this file to `/Sources`. It will automatically link to the relevant `Concepts/` and `Tools/` notes.

### 2. Strategic Retrieval
Instead of a blind search, tell your agent to leverage the buckets:
- **Theory:** "Search `/Concepts` to explain the underlying paradigm."
- **Syntax:** "Search `/Tools` to find the correct implementation primitives."
- **Reference:** "Search `/Sources` to find the original transcript context."
- **Architecture:** "Search `/Applied` to see how we've implemented this before."

---

## Collaborative Workflow (GitHub)
- **CONTRIBUTE:** If you learn a new technical concept or tool nuance, submit a **Pull Request** to the `/Concepts` or `/Tools` folders.
- **PRIVATE:** Your `/Applied`, `/Sources`, and `/Daily_Notes` folders are in `.gitignore`. They will never leave your local machine.

## CLI Playbook
Use `grep` or `ripgrep` (rg) for lightning-fast knowledge retrieval from your terminal:
- `rg "Knowledge_Graph_RAG" Applied` — Find private projects where you used graph-based RAG.
- `rg "type: source" Sources | head -n 5` — See your latest ingested materials.

---
> **Core Node:** [[START_HERE]]
