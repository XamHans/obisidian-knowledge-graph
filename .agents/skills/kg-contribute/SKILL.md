---
name: kg-contribute
description: Use when a member wants to contribute general AI knowledge back to the shared graph — turn a private Source/insight into a clean, objective Concept or Tool note and open a pull request. Enforces the public/private firewall so no project-specific or proprietary detail leaks. Triggers on "contribute this", "add a concept/tool", "push this back to the graph", "share this knowledge".
---

# kg-contribute

Turn what a member learned (usually a private note in `Sources/`) into a **public, objective** Concept or Tool note and open a PR — without ever leaking private project context.

This is the write-side counterpart to `knowledge-graph-advisor` (read side). The graph collaborates on the **physics** of AI engineering (Concepts & Tools) and keeps **execution** (Applied & Sources) private — see `CONTRIBUTING.md`.

## When to use
- A member processed a transcript/paper/repo into `Sources/` and it surfaced a general concept or tool the public graph is missing.
- A member asks to add or update a Concept/Tool.

Do **not** use it to write `Applied/` or `Sources/` notes — those stay local.

## Workflow

1. **Pick the contribution & its CAST bucket.** Decide if the knowledge is a `Concept` (abstract theory, paradigm, method) or a `Tool` (concrete model, library, DB, framework). Only these two are public. If it's project execution, stop — it belongs in private `Applied/`.

2. **Dedup before drafting.** Search the public layer so you update rather than duplicate:
   ```bash
   rg -li "<topic>" Concepts/ Tools/
   ```
   If a note exists, propose an **update** (e.g. refresh `reviewed`, add a capability) instead of a new file.

3. **Draft from the template + schema.** Copy the matching template and follow `CONVENTIONS.md` exactly:
   - `Templates/Concept.md` → `type: concept`, `tags`, `stability` (default `stable`, set `evolving` if it moves fast), `reviewed: <YYYY-MM>`, `evidence_status`.
   - `Templates/Tool.md` → `type: tool`, `tags`, `resource: <official-docs-url>`, `stability` (default `volatile`), `as_of`, `reviewed`.
   - Use **underscore_TitleCased** filenames. Write objective, technical prose — **no** company names, project names, client data, or "we/our system" framing.
   - Connect the graph: add 2-4 `[[wikilinks]]` to related Concepts/Tools, and add the note to the relevant `Hubs/<Hub>.md` Map of Content.

4. **⛔ PRIVACY GATE — run before writing files or committing.** This is non-negotiable:
   - **Never** stage or commit anything under `Applied/`, `Sources/`, `Daily_Notes/`, `Technical_Knowledge_Graph/`, `Archive/`. Stage only the specific `Concepts/`, `Tools/`, `Hubs/` files you authored.
   - Scan the **draft text** for leak markers and remove/redact any hit:
     - employer/client/company names, internal project or product codenames
     - customer data, names, emails, internal URLs, file paths from the private layer
     - secrets, API keys, credentials
     - "we/our/my system does X" phrasing → rewrite as objective ("X is done by …")
   - If a fact only makes sense with private context, **leave it out**. When unsure, ask the member before proceeding.

5. **Write the note + update its Hub.** Create the file(s) in `Concepts/` or `Tools/`; add the wikilink to the Hub's MoC list.

6. **Branch, commit (public files only), PR.**
   ```bash
   git checkout -b add-<type>-<name>
   git add Concepts/<Name>.md Hubs/<Hub>.md   # explicit paths only — never `git add -A`
   git commit -m "Add Concept: <Name>"         # or "Update Tool: <Name>"
   git push -u origin add-<type>-<name>
   gh pr create --title "Add Concept: <Name>" --body "<why this is valuable to the team>"
   ```
   PR title/body convention per `CONTRIBUTING.md`.

7. **Verify integration (optional).** `python3 scripts/okf-build.py` — confirm the new note lands in the OKF bundle with 0 broken links before/after.

## Output shape
- The created/updated note path(s).
- The Hub MoC line added.
- The privacy-gate result (what was scanned, what was redacted).
- The PR URL.

Keep the note tight and objective — a senior engineer should read it as reference, not as someone's project writeup.
