# The AI Engineer — Knowledge Graph

A free, community-maintained reference vault for engineers building production AI systems. Curated by **Johannes Hayer** for [The AI Engineer](https://www.skool.com/ai-builders-6997/about) Skool community.

**Join the community:** [skool.com/ai-builders-6997/about](https://www.skool.com/ai-builders-6997/about)
**Free Slack:** [Join here](https://join.slack.com/t/j-hayer/shared_invite/zt-40wmmgk82-~j8H6fVycgya21bgsNsyOQ)
**Code boilerplates:** [github.com/XamHans/boilerplates-skool](https://github.com/XamHans/boilerplates-skool)

---

## What is this?

Most people learn AI by bouncing between YouTube videos, blog posts, and docs — and end up with a pile of disconnected notes that don't add up to real engineering skill.

This vault is a **connected map**: concepts link to the tools that implement them, tools link to the architectural patterns they enable, and everything traces back to decisions you make in production. It's not a course. It's the reference layer you keep open while you build.

**What's inside:**
- `Concepts/` — the "why" behind production AI: chunking strategies, agent memory patterns, eval engineering, inference optimization, prompt injection defenses, and 60+ more
- `Tools/` — the "what": PGVector, FastMCP, Phoenix, Google Cloud Run, OpenAI Apps SDK, and more — each mapped to the concepts they implement
- `Hubs/` — curated learning paths that connect concepts and tools into a curriculum per role
- `Assets/` — ready-to-use playbooks (tool-calling experiment lab, CLI search playbook)

---

## Who is this for?

### AI App Builder
You want to build ChatGPT-style apps, integrate LLMs into products, and ship fast.

**Start with:** [Generative AI Hub](Hubs/Generative_AI.md)
**Key concepts:** Prompt engineering, structured output, function calling
**Key tools:** OpenAI Apps SDK, ChatGPT Apps

### RAG Engineer
You want to build search and retrieval systems that ground LLM answers in real data.

**Start with:** [RAG Hub](Hubs/RAG.md)
**Key concepts:** Chunking strategies, hybrid retrieval, reranking, knowledge graph RAG, RAG evaluation
**Key tools:** PGVector, Neon Postgres, Azure AI Search

### Agent Engineer
You want to build autonomous agents that use tools, maintain memory, and run multi-step workflows.

**Start with:** [AI Agents Hub](Hubs/AI_Agents.md) → [Agent Tool Calling Hub](Hubs/Agent_Tool_Calling.md)
**Key concepts:** Agent architecture patterns, tool schema design, guardrails, state machines, memory patterns
**Key tools:** Model Context Protocol, FastMCP, MCP Apps

### Production AI Engineer
You want to ship reliable, observable, cost-efficient AI systems at scale.

**Start with:** [LLM Evals Hub](Hubs/LLM_Evals.md)
**Key concepts:** Eval engineering lifecycle, LLM-as-judge, inference optimization, model routing, prompt injection defenses, RAG security
**Key tools:** Phoenix, Google Cloud Run, MLflow, Azure Application Insights

---

## How to use it

### Option 1 — Browse on GitHub
Just click into `Hubs/`, pick your role path above, and follow the links. No setup needed.

### Option 2 — Open in Obsidian (best experience)
1. Clone the repo: `git clone https://github.com/XamHans/obisidian-knowledge-graph.git`
2. Open [Obsidian](https://obsidian.md/) → "Open folder as vault" → select the cloned folder
3. Open **Graph View** to see the full concept map visually
4. Start at [START_HERE.md](START_HERE.md)

### Option 3 — Use with an AI coding agent
Point Claude Code, Cursor, or Codex at the vault folder. Ask role-specific questions:
- *"Search Concepts/ to explain how hybrid retrieval ranking works"*
- *"Search Tools/ for everything related to vector databases"*
- *"Find all concepts linked to agent memory"*

From the terminal:
```bash
rg "chunking" Concepts/        # find all notes on a topic
rg "type: tool" Tools/         # list available tools
```

---

## What stays private

The `Applied/`, `Sources/`, and `Daily_Notes/` folders are gitignored — they exist only on your machine. Use them for:
- **Applied/** — your own project blueprints and system designs
- **Sources/** — raw transcripts, papers, and reference material you've ingested
- **Daily_Notes/** — working notes and scratch

Only `Concepts/`, `Tools/`, `Hubs/`, and `Assets/` are public and shared here.

---

## Contributing

Found a concept missing? Know a better tool for a pattern? Submit a pull request to `Concepts/` or `Tools/`. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.
