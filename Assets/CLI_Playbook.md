# Obsidian CLI Playbook & Guidelines

## Goal
- Maintain a tightly connected knowledge base that turns raw transcripts and supporting material into reusable insights for AI engineering work, content production, and community assets with consistent linking.

## Structure
![[Assets/Agents/vault_structure_overview]]

## CLI Query Playbook
Run these illustrative commands from the vault root. Treat them as starting points—swap folders, block IDs, or section names to match the note you are auditing. `rg` (ripgrep) handles text searches; `fd` lists files and directories.

- `rg --files -g '*.md' Concepts Applied Sources Tools Hubs Assets` — inventory the core knowledge buckets.
- `fd -t d -d 1` — refresh your mental model of top-level folders prior to a sweep.
- `rg -n "[[START_HERE]]"` — surface every CTA and backlink into the public entry point.
- `rg -n '#^model-compare' Sources` — locate transcripts citing a specific highlight.
- `rg -c '\[\[' Sources | sort -t: -k2n` — rank sources by outbound link count.
- `rg -n '^type: applied' Applied` — list project briefs by front matter.
- `rg -n '^type: hub' Hubs` — confirm every hub note carries canonical front matter.
- `rg -n '^type: tool' Tools` — verify new tool dossiers follow the template.
- `rg -n '^## ' Concepts/RAG.md` — preview a note's section outline.
- `rg -n '[[Concepts/Local_AI_Deployment' Applied` — verify which projects lean on a concept.
- `fd -t f -g '*.md' Applied/AI_Native_Engineer` — group related community assets.

### Multi-step investigations
- **Trace block embeds back to source**: `rg -l '#^latency' Sources | xargs -I{} rg -n '[[Applied/Short_Form_Scripts' {}` — confirm every excerpt feeding scripts resolves.
- **Validate hub ↔ tool links**: `rg -n '\[\[Hubs/' Tools` — ensure every technology profile references its hubs.
- **Check concept coverage across folders**: `rg -l '[[Concepts/Cloud_AI_Integration_Strategy' Sources Applied Hubs` — verify concept appears across transcripts and projects.
- **Audit notes missing outbound links**: `rg -c '\[\[' Applied | awk -F: '$2==0 {print $1}'` — list notes with no wikilinks.
- **Front-matter completeness check**: `rg --files-without-match '^---' Applied Concepts Tools` — flag markdown files missing front matter.

## Guidelines for an AI-Assisted CLI Agent
1. **Enforce naming and metadata:** When creating notes from transcripts, craft descriptive titles and inject standard front matter (category, tags, created date) via templates.
2. **Adopt underscore filenames:** Use underscores (`_`) for every file and directory name.
3. **Anchor to the core node:** Ensure every note includes `> Core Node: [[START_HERE]]`.
4. **Validate links:** Search for `[[` patterns, confirm targets exist, and flag link gaps.
5. **Keep folders aligned:** Apply CAST rules.
6. **Refresh MOCs:** Rebuild hub notes from backlinks or folder scans.
7. **Expose dashboards:** Use query blocks or tables to list open tasks or active projects.
8. **Audit tags and states:** Ensure workflow tags (e.g., #todo, #inprogress) are present and consistent.
9. **Maintain a single vault:** Encourage consolidation.
10. **Reference the style guide:** Keep naming conventions and tag syntax documented.

> Core Node: [[START_HERE]]
