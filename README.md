# The AI Engineer — Knowledge Graph

A free, community-maintained reference vault for engineers building production AI systems. Curated by **Johannes Hayer** for [The AI Engineer](https://www.skool.com/ai-builders-6997/about) Skool community.

**Join the community:** [skool.com/ai-builders-6997/about](https://www.skool.com/ai-builders-6997/about)
**Free Slack:** [Join here](https://join.slack.com/t/j-hayer/shared_invite/zt-40wmmgk82-~j8H6fVycgya21bgsNsyOQ)
**Code boilerplates:** [github.com/XamHans/boilerplates-skool](https://github.com/XamHans/boilerplates-skool)

---

## What is this?

Most people learn AI by bouncing between YouTube videos, blog posts, and docs — and end up with a pile of disconnected notes that don't add up to real engineering skill.

This vault is a **connected map**: concepts link to the tools that implement them, tools link to the architectural patterns they enable, and everything traces back to decisions you make in production. It's not a course. It's the reference layer you keep open while you build.

It's built on the **[Open Knowledge Format (OKF)](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)** — notes are plain Markdown with YAML frontmatter, and a build step publishes them as an **[interactive graph](https://xamhans.github.io/obisidian-knowledge-graph/)** any agent can read.

**What's inside:**
- `Concepts/` — the "why" (durable theory): chunking, embeddings, hybrid retrieval, reranking, RAG evaluation…
- `Tools/` — the "what" (concrete primitives), each mapped to the concepts it implements
- `Hubs/` — the navigation/index layer: curated paths per topic
- `Assets/` — ready-to-use playbooks

> **Status:** the graph is being rebuilt on OKF, one cluster at a time. **RAG is live now**; other domains are archived and reworked note-by-note. Explore what's live in the [interactive graph](https://xamhans.github.io/obisidian-knowledge-graph/).

---

## Who is this for?

### AI App Builder
You want to build ChatGPT-style apps, integrate LLMs into products, and ship fast.

**Start with:** Generative AI Hub *(rework in progress)*
**Key concepts:** Prompt engineering, structured output, function calling
**Key tools:** OpenAI Apps SDK, ChatGPT Apps

### RAG Engineer
You want to build search and retrieval systems that ground LLM answers in real data.

**Start with:** [RAG Hub](Hubs/RAG.md)
**Key concepts:** Chunking strategies, hybrid retrieval, reranking, knowledge graph RAG, RAG evaluation
**Key tools:** PGVector, Neon Postgres, Azure AI Search

### Agent Engineer
You want to build autonomous agents that use tools, maintain memory, and run multi-step workflows.

**Start with:** AI Agents Hub *(rework in progress)*
**Key concepts:** Agent architecture patterns, tool schema design, guardrails, state machines, memory patterns
**Key tools:** Model Context Protocol, FastMCP, MCP Apps

### Production AI Engineer
You want to ship reliable, observable, cost-efficient AI systems at scale.

**Start with:** LLM Evals Hub *(rework in progress)*
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

## Learn with the `/teach` skill

The knowledge graph pairs with the **`/teach`** Claude Code skill — created by [Matt Pocock](https://www.mattpocock.com/) — to turn static notes into interactive, stateful lessons.

Instead of reading concept files passively, you open your terminal, point Claude at the knowledge graph, and get a personalised lesson grounded in the vault's content.

### What it does

- Generates **beautiful HTML lessons** tailored to your level and goal
- Tracks your **learning history** across sessions so it never repeats itself
- Produces **reference cheat sheets** you can print or revisit later
- Stays grounded in high-trust sources — not just LLM memory

### Install the skill

```bash
claude install-skill mattpocock/teach
```

Or check the [Matt Pocock skills page](https://www.mattpocock.com/) for the latest install instructions.

### How to use it with this knowledge graph

Open Claude Code inside the knowledge graph folder and run:

```
/teach Use content from the knowledge graph and teach me how RAG works
```

Other examples:

```
/teach Use content from Concepts/ and teach me agent memory patterns
/teach Use the RAG hub and teach me how to build a reranking pipeline
/teach Use Concepts/ and teach me the difference between chunking strategies
```

Claude will read the relevant concept files, build a lesson from them, and save your progress so the next session picks up where you left off.

### The teaching workspace

When you run `/teach` inside this vault, it uses the `teach/` folder as its workspace:

| File / Folder | Purpose |
|---|---|
| `teach/MISSION.md` | Why you're learning this — grounds every lesson to a real goal |
| `teach/lessons/*.html` | Generated lessons, one per session |
| `teach/reference/*.html` | Compressed cheat sheets for quick lookup |
| `teach/learning-records/*.md` | What you've learned — used to calculate what to teach next |
| `teach/RESOURCES.md` | Trusted sources the skill draws from |

---

## Contributing

Found a concept missing? Know a better tool for a pattern? Open a pull request adding a note to `Concepts/` or `Tools/` — keep it objective and technical (no project specifics).

The repo ships **Claude Code skills** to make this easy:
- **`kg-ingest`** — turn a URL/transcript/paper into a private `Sources/` note (your local library)
- **`kg-contribute`** — promote general knowledge into a public Concept/Tool and open the PR for you, with a privacy gate

Notes follow the schema in [CONVENTIONS.md](CONVENTIONS.md) (start from `Templates/`). Every PR is validated by CI (OKF compliance + 0 broken links + privacy); on merge, the bundle and [interactive graph](https://xamhans.github.io/obisidian-knowledge-graph/) republish automatically. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full flow.
