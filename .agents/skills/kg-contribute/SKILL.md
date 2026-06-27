---
name: kg-contribute
description: Use when a member wants to contribute general AI knowledge back to the shared graph — turn a private Source/insight into a clean, objective, well-researched Concept or Tool note and open a pull request. Enforces the public/private firewall so no project-specific or proprietary detail leaks. Triggers on "contribute this", "add a concept/tool", "push this back to the graph", "share this knowledge".
---

# kg-contribute

Turn what a member learned into a **public, objective, reference-grade** Concept or Tool note and open a PR — without ever leaking private project context.

This is the write-side counterpart to `knowledge-graph-advisor` (read side). The graph collaborates on the **physics** of AI engineering (Concepts & Tools) and keeps **execution** (Applied & Sources) private — see `CONTRIBUTING.md`.

## When to use
- A member processed a transcript/paper/repo into `Sources/` and it surfaced a general concept or tool the public graph is missing.
- A member asks to add or update a Concept/Tool, or to **rework an old/thin note** (e.g. migrating `Archive/`) up to standard.

Do **not** use it to write `Applied/` or `Sources/` notes — those stay local.

## Quality bar
Every contributed note must clear the **Sourcing & quality bar in `CONVENTIONS.md`** (the canonical standard): researched not recalled, **every source URL opened and verified** (no fabricated citations), concrete + correct, in the standard note shape. A note without a `## Sources` block of working links is not done; if a draft reads like boilerplate (generic "Sub-Concept Map / Playbook Moves" with no specifics), it fails the bar — research and rewrite.

## Workflow

1. **Pick the contribution & its CAST bucket.** Decide `Concept` (abstract theory, paradigm, method) vs `Tool` (concrete model, library, DB, framework). Only these two are public. Project execution → stop; it belongs in private `Applied/`.

2. **Dedup before drafting.** Search the public layer so you update rather than duplicate:
   ```bash
   rg -li "<topic>" Concepts/ Tools/
   ```
   If a note exists, propose an **update** (refresh `reviewed`, add a capability/section) instead of a new file.

3. **⛔ RESEARCH & VERIFY SOURCES — do not skip.** This is what produces the quality bar above.
   - Do real web research on the topic. Target **4–6 authoritative sources**: canonical papers (arXiv), official docs, respected explainers (Distill, Lilian Weng's Lil'Log, Stanford CS notes, vendor docs).
   - **Verify every URL before citing it:** find via WebSearch, then **WebFetch to confirm it returns HTTP 200 and actually covers the claim.** Never invent, guess, or cite a URL you did not open. If you can't confirm a source, drop it.
   - Use the research to extract concrete facts (numbers, method names, tradeoffs) **and to catch inaccuracies/folklore** in the draft.
   - For a multi-note batch (e.g. migrating a whole domain), fan out **parallel research subagents — one per note** — each returning verified sources + technical corrections; then you author the notes for consistent house style. (Tell subagents explicitly: research only, **do not create or edit files** — they tend to leave stray stubs otherwise.)

4. **Draft from the template + schema.** Copy `Templates/Concept.md` or `Templates/Tool.md`; follow `CONVENTIONS.md` for the **frontmatter schema, note body shape, and `evidence_status` flip** (see Format below). Use **underscore_TitleCased** filenames. Write objective, technical prose — **no** company/project names or "we/our system" framing. Add 2–4 `[[wikilinks]]` and the note to the relevant `Hubs/<Hub>.md`.

5. **⛔ PRIVACY GATE — run before writing files or committing.** Non-negotiable:
   - **Never** stage or commit anything under `Applied/`, `Sources/`, `Daily_Notes/`, `Technical_Knowledge_Graph/`, `Archive/`. Stage only the specific `Concepts/`, `Tools/`, `Hubs/` files you authored.
   - Scan the **draft text** for leak markers and remove/redact: employer/client/company names, internal project/product codenames, customer data, names, emails, internal URLs or file paths, secrets/keys; rewrite "we/our system does X" → objective ("X is done by …").
   - If a fact only makes sense with private context, **leave it out**. When unsure, ask the member.

6. **Write the note(s) + update the Hub.** Create the file(s); add the wikilink to the Hub's Map of Content. If the domain has no Hub yet, create one from `Templates/Hub.md`.

7. **Verify integration (required, not optional).**
   ```bash
   python3 scripts/okf-build.py && python3 scripts/okf-validate.py
   ```
   Validate must report `broken_links=0` and `private_links=0` (privacy clean). Then confirm `git status` shows **only** the public files you intended — no stray stubs (e.g. an accidental `START_HERE.md`).

8. **Branch, commit (public files only), PR.**
   ```bash
   git checkout -b add-<type>-<name>
   git add Concepts/<Name>.md Hubs/<Hub>.md   # explicit paths only — never `git add -A`
   git commit -m "Add Concept: <Name>"         # or "Update Tool: <Name>"
   git push -u origin add-<type>-<name>
   gh pr create --title "Add Concept: <Name>" --body "<why this is valuable to the team>"
   ```

## Format (canonical: `CONVENTIONS.md`)
`CONVENTIONS.md` is the single source of truth for the full **frontmatter schema** (our added attributes — `description`, `tags`, `stability`, `reviewed`, `evidence_status`; Tool extras `resource`/`as_of`/`lifecycle`), the **note body shape**, and the **`evidence_status` flip**. Don't restate it here — follow it. Skill-time reminders:
- `description` = a 12–20-word what+why scan line; omit `stability` when it equals the type default.
- Set `evidence_status: has_receipts` **only** with a verified `## Sources` block; else `needs_receipts` + `evidence_backlog`.
- Forward-refs to not-yet-written notes are fine — they mark the rework backlog and degrade to plain text in the bundle.

## Output shape
- The created/updated note path(s) + the Hub MoC line added.
- The privacy-gate result (what was scanned, what was redacted).
- The build/validate result (`broken_links` / `private_links`).
- The PR URL.

Keep the note tight and objective — a senior engineer should read it as reference, not as someone's project writeup.
