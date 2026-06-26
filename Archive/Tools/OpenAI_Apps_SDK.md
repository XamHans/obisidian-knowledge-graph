---
type: tool
stability: volatile
as_of: 2026-06
reviewed: 2026-06
linked_hubs:
  - [[Hubs/ChatGPT_Apps]]
  - [[Hubs/Model_Context_Protocol]]
---

## Definition
- OpenAI’s Apps SDK for ChatGPT that uses MCP-style servers plus HTML widgets to expose tools and UI inside ChatGPT via connectors.

## Capabilities
- Registers tools with schemas and metadata (including output templates) for ChatGPT to call.
- Serves resources (e.g., HTML widgets) that ChatGPT loads into iframes and hydrates with tool outputs.
- Supports connector configuration to reach local or remote servers over streamable HTTP.

## Integration Patterns
- Include `/mcp` endpoint (with trailing slash when required) in connector URLs; tunnel local dev with `ngrok http <port>`. *Source:* [[Resources/Processed_Transcripts/ChatGPT_Apps_SDK_Todo_Quickstart#^apps-connector-path]]
- Reference widget resources in tool metadata so ChatGPT fetches HTML and injects tool output for rendering. *Source:* [[Resources/Processed_Transcripts/ChatGPT_Apps_SDK_Todo_Quickstart#^apps-widget-resource]]
- Use `window.openai` inside widgets to trigger tools without reloading the iframe, keeping UI static. *Source:* [[Resources/Processed_Transcripts/ChatGPT_Apps_SDK_Todo_Quickstart#^apps-window-openai]]

## Source Transcripts
- [[Resources/Processed_Transcripts/ChatGPT_Apps_SDK_Todo_Quickstart#^apps-widget-resource]]
- [[Resources/Processed_Transcripts/ChatGPT_Apps_SDK_Todo_Quickstart#^apps-connector-path]]

## Related Concepts
- [[Concepts/ChatGPT_Apps_MCP_Architecture]]
- [[Concepts/MCP_Production_Workflows]]

## Linked Hubs
- [[Hubs/ChatGPT_Apps]]
- [[Hubs/Model_Context_Protocol]]
