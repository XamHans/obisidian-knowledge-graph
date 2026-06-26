# Frontmatter Conventions

The schema for every note in this AI knowledge graph. Source of truth — templates in `Templates/` and `scripts/okf-build.py` follow it.

## The principle: make decay legible

This wiki captures **AI / software knowledge**, which has a **differential decay rate**:

- **Concepts** (RAG strategies, agent memory, eval engineering) stay true for years.
- **Tools** (SDKs, model APIs, pricing) can be wrong in months.

Frontmatter's job is not to describe *what* a note is — that's the body — but to answer **"can I still trust this, and how fast does it rot?"** That needs two separate time axes:

| Field | Answers | Maintained |
|---|---|---|
| `updated` | Was the text touched? | automatic (git) |
| `reviewed` | Was the content last **confirmed true**? | manual — the trust signal |

A `stable` concept may have `reviewed` a year old and still be fine. A `volatile` tool with `reviewed` older than 3 months is suspect. That makes staleness **computable** instead of guesswork.

## Structure & abstraction

What OKF actually prescribes is minimal: only `type` is required (producer-defined, no controlled vocabulary), and the sole reserved structural files are `index.md` (navigation) and `log.md` (history). OKF explicitly relies on **links to carry the graph, beyond the parent/child folder tree.**

So the abstraction here is:

```
KNOWLEDGE (the graph):  concept (durable "why")  ·  tool (volatile "what")
NAVIGATION:             hub  = the index.md / map-of-content layer (an entry point, NOT a knowledge node)
PRIVATE:                source · applied
```

- **Two knowledge types only** — `concept` and `tool`. They map to the decay split above. No `pattern` type (that's the `stability` axis); don't split `tool`.
- **Hubs are navigation, not a third kind of knowledge.** They are this vault's expression of OKF's `index.md` — curated role/topic maps that link into the graph.
- **Type-first folders + links — do NOT cluster by topic.** ~91% of concepts belong to ≥2 topics (e.g. `Prompt_Injection_And_Defenses` lives under RAG, Agents, Evals, Security). A topic-first tree would force a single home and break multi-membership; the links carry the real graph, exactly as OKF intends.

## Universal fields (every note)

| Field | Question | Values / format | Default |
|---|---|---|---|
| `type` | Node kind | `concept` · `tool` · `hub` | **required (OKF)** |
| `title` | Display name | string | derived from filename |
| `description` | One-line summary for **progressive disclosure** | string | authored; build derives as fallback |
| `tags` | Topical retrieval | `[list]` | — |
| `stability` | **How fast does it rot?** | `stable` · `evolving` · `volatile` | **inferred from `type`** |
| `reviewed` | Last confirmed true | `YYYY-MM` | set on write/review |
| `updated` | Last edited | ISO date | git |

You hand-write `type`, `description`, `tags`, and `reviewed` (and `stability` only when it differs from the default). `title` / `updated` are derived — don't bother unless overriding.

### Progressive disclosure (write `description` like a skill)
`description` is the **scan layer**. Just as an agent reads a skill's `description` to decide whether to load the whole skill, it reads a note's `description` (and the generated `index.md`, which lists every note's description) to decide whether to open the note. So write a crisp one-liner — 12–20 words, what + why — not a derived first sentence. It is the difference between an agent loading the right 3 notes vs. all 150.

## Type-specific fields

**Concept** — provenance / grounding:
- `evidence_status`: `has_receipts` · `needs_receipts`
- `evidence_backlog`: `[list of missing receipts]`

**Tool** — the fast-moving layer:
- `as_of`: `YYYY-MM` — which point-in-time the description reflects
- `resource`: `<official-docs-url>` (OKF reserved field)
- `lifecycle` *(optional)*: `experimental` · `ga` · `deprecated` — the tool's own maturity

**Hub** — navigation:
- `parent_hub` / `child_hubs`: `[[wikilinks]]`

## `stability`: default by type, override on reality

Authoring stays cheap — set it only when the note breaks the default:

```
concept → stable      tool → volatile      hub → stable
```

The overrides are where the value shows:

| Note | Default | Reality | Set |
|---|---|---|---|
| `Transformer_Architecture` | stable | bedrock | — (default) |
| `Agentic_RAG` | stable | moves fast | `stability: evolving` |
| `PGVector` | volatile | stable Postgres ext | `stability: evolving` |
| some new MCP SDK | volatile | churns | — (default) |

### Review tolerances (how staleness is computed)

| `stability` | "fresh" while `reviewed` is younger than |
|---|---|
| `stable` | ~12 months |
| `evolving` | ~6 months |
| `volatile` | ~3 months |

An agent can then warn: *"PGVector not reviewed since 2026-01, classified `evolving` → verify before relying."*

## Dropped fields (and why)

| Removed | Reason |
|---|---|
| `persona` | 108× the same constant value → zero information |
| `status` | 128/131 were `active` → near-constant; trust is now carried by `evidence_status` + `stability` |
| `last_enriched` | a one-off batch date → replaced by per-note `reviewed` |
| `technology` / `software` / `framework` (as `type` values) | all mean "tool" → unified to `type: tool` |

## Worked examples

```yaml
# Concept
type: concept
tags: [rag, retrieval]
stability: stable          # = default for concepts, may be omitted
reviewed: 2026-06
evidence_status: has_receipts
```
```yaml
# Tool
type: tool
tags: [rag, vector-db]
resource: https://github.com/pgvector/pgvector
stability: evolving        # override: more stable than the tool default
as_of: 2026-06
reviewed: 2026-06
```

## Flow into OKF

`okf-build` derives the OKF reserved set (`type/title/description/tags/timestamp`) **and carries `stability`, `reviewed`, `as_of`, `lifecycle`, `evidence_status` through** into the bundle (OKF allows custom fields), so consuming agents see the freshness signal too.

See also: `CONTRIBUTING.md`, `AGENTS.md`, `Templates/`.
