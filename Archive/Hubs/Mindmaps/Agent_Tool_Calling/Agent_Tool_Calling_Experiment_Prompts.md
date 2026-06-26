# Agent Tool Calling Experiment Prompts

## Beginner
- Create 20 tool-calling cases to measure tool selection accuracy.
- Add strict schema validation and track wrong-parameter rate before/after.
- Test clarification prompts on ambiguous user intents.

## Intermediate
- Build failure-mode labels and tag real traces by class.
- Compare abstain policy vs forced-call policy for high-risk actions.
- Test retry strategy under tool timeouts and partial failures.

## Advanced
- Add a verifier step that checks tool choice and parameter plausibility pre-execution.
- Simulate prompt injection in retrieved context and test tool gating defenses.
- Define rollback and compensation steps for side-effecting tool failures.

## Execution Rule
- Log: user intent, selected tool, payload, validation result, side effect, recovery action, final outcome.

> Core Node: [[START_HERE]]
