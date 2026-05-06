---
type: concept
status: seed
evidence_status: needs_receipts
linked_hubs:
  - [[Hubs/ChatGPT_Apps]]
  - [[Hubs/Model_Context_Protocol]]
---

## Definition
ChatGPT Apps MCP architecture is the pattern of exposing tools, structured outputs, and interactive UI resources to ChatGPT through an MCP-compatible server. The app host calls server-side tools and renders declared HTML widgets as the user-facing surface.

## Why It Matters
- It separates model-facing tool contracts from user-facing UI.
- It lets a production app combine natural-language orchestration with deterministic backend APIs.
- It keeps widget rendering, tool schemas, auth, and transport choices as explicit engineering boundaries.

## Engineering Notes
- Treat tool schemas as the contract between the model and backend.
- Treat widget resources as the contract between the backend and host-rendered UI.
- Use transport, auth, and sandbox settings as first-class deployment decisions.

## Related
- [[Tools/OpenAI_Apps_SDK]]
- [[Tools/MCP_Apps]]
- [[Tools/Model_Context_Protocol]]
- [[Concepts/Tool_Schema_Design_For_Agent_Tools]]
- [[Concepts/Structured_Output_Validation]]

> Related Hub: [[Hubs/ChatGPT_Apps]]
> Core Node: [[START_HERE]]
