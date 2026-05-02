# Vault Structure Overview

- All vault folders and notes use underscore-separated, TitleCased filenames (no spaces or dashes; keep acronyms uppercase).
- Every note carries `> Core Node: [[Projects/AI_Native_Engineer]]` so the graph centers on the program.
- `Inbox/` – capture zone for new material; `Inbox/Transcripts_to_Process` holds raw subtitle drops awaiting ingestion.
- `Resources/` – canonical references:
  - `Resources/Hubs/` stores map-of-content notes that anchor concept clusters and technology rollups.
  - `Resources/Concepts/` houses evergreen operating patterns with hub backlinks and technology references.
  - `Resources/Technologies/` collects grounded dossiers for protocols, SDKs, transports, and infrastructure layers (not vendor-specific apps).
  - `Resources/Software/` holds vendor or product-specific applications tied to a hub/area (e.g., Phoenix under LLM_Evals); mark `type: software` to avoid technology auto-detection.
  - `Resources/Processed_Transcripts/` stores processed transcripts keyed by descriptive names, and `Resources/Script_Frameworks/` tracks messaging systems ready for reuse.
- `Projects/` – active deliverables such as `Projects/Short_Form_Scripts`, `Projects/YT_Long_Form_Scripts`, and `Projects/AI_Native_Engineer` that pull from transcript insights.
- `Areas/` – long-running responsibilities and ongoing research themes.
- `Archives/` – retired or raw assets kept for historical reference (e.g., archived video transcripts, legacy drafts).
- `Excalidraw/` – visual thinking boards tied back to notes through embeds.
- `Agents/` – operating manuals for autonomous helpers, including processing and connectivity agents.

- Hubs can be nested—use `parent_hub`/`child_hubs` fields in front matter to make relationships explicit (e.g., Model_Context_Protocol → ChatGPT_Apps) and keep detection accurate.

> Core Node: [[Projects/AI_Native_Engineer]]
