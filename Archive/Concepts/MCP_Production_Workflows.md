---
type: concept
stability: stable
reviewed: 2026-06
evidence_status: needs_receipts
linked_hubs:
  - [[Hubs/Model_Context_Protocol]]
---

## Definition
MCP production workflows are the operational patterns for moving an MCP server from local development to a reliable, reachable, observable service used by LLM hosts.

## Workflow Checklist
- Define tools, resources, prompts, and schemas separately.
- Choose transport based on host support and deployment target.
- Add authentication and permission checks before exposing user or customer data.
- Package and deploy the server with reproducible environment configuration.
- Add traces, logs, and eval cases for tool-selection failures and recovery paths.

## Engineering Notes
- Local stdio is useful for development; remote hosts usually need HTTP-based transport.
- Deployment URLs, trailing slashes, and tunnel behavior can become integration failure points.
- Production readiness includes host discovery, versioning, rollback, and secret handling.

## Related
- [[Tools/Model_Context_Protocol]]
- [[Tools/FastMCP]]
- [[Tools/Docker]]
- [[Tools/Google_Cloud_Run]]
- [[Concepts/Agent_Observability_And_Evaluation]]
- [[Concepts/Tool_Calling_Failure_Modes]]

> Related Hub: [[Hubs/Model_Context_Protocol]]
> Core Node: [[START_HERE]]
