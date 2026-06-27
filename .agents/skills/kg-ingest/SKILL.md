---
name: kg-ingest
description: Use when the user wants to ingest raw material (a URL, YouTube transcript, paper, repo, or pasted notes) into the knowledge graph. Produces a structured, private Source note in Sources/ — the citeable receipt that public Concepts/Tools are later grounded in. Triggers on "ingest this", "process this transcript/paper/URL", "add this to my sources", "capture this".
---

# kg-ingest

Turn raw external material into a structured **Source note** in the **private** `Sources/` layer. This is the *input* side of the pipeline; `kg-contribute` is the *output* side (promoting general knowledge to public Concepts/Tools and citing these sources).

```
raw content ── kg-ingest ──▶ Sources/<Title>.md  (private receipt, gitignored)
                                     │ cited by
                                     ▼
                            public Concepts/Tools  ── kg-contribute ──▶ PR
```

## When to use
- The user drops a URL, transcript, paper, repo, or notes and wants it captured into the graph.
- Do **not** write public Concepts/Tools here — that is `kg-contribute`'s job. Ingest only captures the private receipt + flags candidates.

## Quality bar (non-negotiable)
A Source note is a **durable, citeable receipt**. It follows the same *verified-provenance, no-fabrication* principle as the **Sourcing & quality bar in `CONVENTIONS.md`**, applied to a single source — write it so `kg-contribute` can later quote it *without reopening the original*:
- **Verify provenance.** Actually fetch/read the material; confirm it says what you claim. Capture **exact numbers, method names, and quotable lines**. Never fabricate a figure, quote, or URL — if you couldn't open it, say so.
- **Concrete takeaways.** 3–5 sharp, technical bullets with enough specificity to cite later (numbers, tradeoffs, mechanisms) — not a generic summary you'll never reopen.
- **Precise candidates.** Name the Concepts/Tools this grounds, so promotion is a clean hand-off with this note as the verified receipt.

## Workflow

1. **Get the content — for real.** URL → fetch it (WebFetch; don't rely on memory of it). File/transcript/paper → read it. Pasted text → use directly. Skip if it isn't relevant to AI engineering. If the source won't resolve, capture what you have and flag the gap — never invent its contents.

2. **Write the Source note** to `Sources/<Underscore_TitleCased>.md` (private). Follow `CONVENTIONS.md` — note the authored `description` for progressive disclosure:
   ```yaml
   ---
   type: source
   title: <descriptive title that communicates the thesis>
   description: <one line — what this source gives an AI engineer (progressive-disclosure summary)>
   tags: [<2-4 topical tags>]
   resource: <url or origin>
   reviewed: <YYYY-MM>
   ---

   ## TL;DR
   <2-3 sentences: the core technical value — what problem it solves, why it matters>

   ## Knowledge Graph Connections
   - **Concepts**: [[Concepts/<Existing>]] · _candidate_: <NewConcept not yet in the graph>
   - **Tools**: [[Tools/<Existing>]] · _candidate_: <NewTool>

   ## Key Takeaways
   - <3-5 sharp, technical bullets — with the actual numbers/quotes/mechanisms, detailed enough to cite later>

   ## Notes / Snippets
   - <actionable system-design ideas or code concepts, with specifics>
   ```

3. **Link to what exists; flag what doesn't.** `rg -li "<topic>" Concepts/ Tools/` to find existing notes to wikilink. For knowledge the public graph is missing, list it as a **_candidate_** — don't create the public note here.

4. **Privacy is automatic but verify.** `Sources/` is gitignored — the receipt stays local. Never write ingested raw material into `Concepts/`, `Tools/`, or `Hubs/`.

5. **Hand off.** End by naming the candidate Concepts/Tools worth promoting, so the user can run `/kg-contribute` on them. Those public notes then cite this Source via `evidence_status: has_receipts`.

## Output shape
- The Source note path.
- The extracted graph connections (existing links + candidates).
- Suggested `/kg-contribute` targets.

Keep takeaways concrete and quotable — a Source note's job is to be a durable, citeable receipt, not a summary you'll never reopen.
