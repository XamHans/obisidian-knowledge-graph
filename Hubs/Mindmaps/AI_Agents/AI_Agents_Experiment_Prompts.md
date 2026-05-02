# AI Agents Experiment Prompts

## Beginner
- Implement a simple planner-executor loop and log each step decision.
- Add explicit tool-use policy rules and test against ambiguous prompts.
- Create a basic state-machine model for one multi-step agent task.

## Intermediate
- Compare single-agent vs multi-agent coordination for a constrained workflow.
- Add memory compaction and retrieval strategy, then measure task success over long sessions.
- Build a failure taxonomy for tool-calling mistakes and map each to a guardrail.

## Advanced
- Build an end-to-end agent benchmark suite with fixed tasks and regression gates.
- Design HITL approval checkpoints for high-risk actions and evaluate latency impact.
- Implement rollback strategy for side-effecting tool actions and test recovery scenarios.

## Execution Rule
- Track task success, step quality, latency, and cost on every benchmark run.

> Core Node: [[Projects/AI_Native_Engineer]]
