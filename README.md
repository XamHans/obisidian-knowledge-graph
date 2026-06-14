# AI Engineering Knowledge Graph

A public Obsidian vault and shared brain for AI Engineers — maintained by **Johannes Hayer** as a free resource for [The AI Engineer](https://www.skool.com/ai-builders-6997/about) Skool community.

**Join the community:** [skool.com/ai-builders-6997/about](https://www.skool.com/ai-builders-6997/about)
**Free Slack:** [Join here](https://join.slack.com/t/j-hayer/shared_invite/zt-40wmmgk82-~j8H6fVycgya21bgsNsyOQ)
**Code boilerplates:** [github.com/XamHans/boilerplates-skool](https://github.com/XamHans/boilerplates-skool)

---

## What's in here

A structured knowledge graph of AI engineering concepts, tools, and learning resources. Built around the **CAST** taxonomy to separate timeless theory from transient project notes:

- **[C]oncepts** — The abstract "physics" of AI (RAG, LoRA, KV Caching, agent architectures). *Public — in this repo.*
- **[A]pplied** — Where theory meets your projects. System designs, blueprints. *Private/local only.*
- **[S]ources** — Processed transcripts, papers, raw reference material. *Private/local only.*
- **[T]ools** — Concrete software and models (LangChain, vLLM, ChromaDB, LiveKit). *Public — in this repo.*

Only `Concepts/` and `Tools/` live here. Your `Applied/` and `Sources/` stay on your machine and never get committed.

---

## Entry points

| Hub | What's inside |
|-----|--------------|
| [AI Concept Universe](Hubs/AI_Concept_Universe.md) | Full curriculum map |
| [AI Agents](Hubs/AI_Agents.md) | Agent architectures, planning, memory, tool use, governance, evals |
| [RAG](Hubs/RAG.md) | Retrieval strategies, chunking, reranking, groundedness, graph-based retrieval |
| [Model Context Protocol](Hubs/Model_Context_Protocol.md) | MCP servers, transports, deployment, host integration |
| [Agent Tool Calling](Hubs/Agent_Tool_Calling.md) | Tool schemas, routing reliability, recovery, guardrails |
| [LLM Evals](Hubs/LLM_Evals.md) | Eval engineering, LLM judges, agreement metrics, trace debugging |

Start here if you're new: [START_HERE.md](START_HERE.md)
Skool community pinned guide: [SKOOL_PINNED_START_HERE.md](SKOOL_PINNED_START_HERE.md)

---

## How to use it

### With Obsidian (recommended)

1. Clone the repo
2. Open the folder as a Vault in [Obsidian](https://obsidian.md/)
3. Open **Graph View** to see how Concepts link to Tools
4. Dangling wikilinks = notes not yet written — click to create them in `Concepts/` or `Tools/`

### With an AI coding agent (Claude Code, Cursor, Codex)

The vault is agent-native. Point your agent at the folder and use bucket-specific retrieval:

- "Search `/Concepts` to explain the underlying paradigm."
- "Search `/Tools` to find the correct implementation."
- "Search `/Sources` to find the original reference context." *(local only)*

To ingest a new YouTube video or paper, follow the workflow in [AGENTS.md](AGENTS.md).

### From the terminal

```bash
# Find all notes about a topic
rg "vector search" Concepts/

# List available tools
ls Tools/

# Search across everything
rg "MCP" Hubs/ Concepts/ Tools/
```

---

## Contributing

If you learn a new concept or tool nuance, submit a **Pull Request** to `Concepts/` or `Tools/`. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Your `Applied/`, `Sources/`, and `Daily_Notes/` folders are gitignored — they never leave your machine.
