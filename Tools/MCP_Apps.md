---
type: technology
status: active
linked_hubs:
  - [[Hubs/ChatGPT_Apps]]
  - [[Hubs/Model_Context_Protocol]]
---

## Definition
- MCP extension that lets tools declare `ui://` resources so hosts render interactive HTML apps in-chat, communicating via a postMessage-based MCP dialect.

## Capabilities
- `_meta.ui.resourceUri` metadata enables UI preload and sandboxed iframe rendering.
- Resource handlers serve bundled HTML/CSS/JS, with optional CSP/permissions for external assets and capabilities.
- Apps can receive tool results and call server tools via the App bridge/postMessage RPC.

## Integration Patterns
- Always declare `ui://` resource URIs and return HTML as `RESOURCE_MIME_TYPE` to drive host rendering. *Source:* [[Resources/Processed_Transcripts/MCP_Apps_Official_Guide#^mcpapps-resource-flow]]
- Use iframe sandbox + postMessage (App class) to keep security boundaries while enabling bidirectional tool calls. *Source:* [[Resources/Processed_Transcripts/MCP_Apps_Official_Guide#^mcpapps-security]]
- Tunnel local servers (cloudflared/ngrok) and test with basic-host or supported clients before production connectors. *Source:* [[Resources/Processed_Transcripts/MCP_Apps_Official_Guide#^mcpapps-testing]]

## Source Transcripts
- [[Resources/Processed_Transcripts/MCP_Apps_Official_Guide#^mcpapps-resource-flow]]
- [[Resources/Processed_Transcripts/MCP_Apps_Official_Guide#^mcpapps-security]]
- [[Resources/Processed_Transcripts/MCP_Apps_Official_Guide#^mcpapps-testing]]

## Related Concepts
- [[Concepts/MCP_Apps_Use_Cases]]
- [[Concepts/ChatGPT_Apps_MCP_Architecture]]

## Linked Hubs
- [[Hubs/ChatGPT_Apps]]
- [[Hubs/Model_Context_Protocol]]
