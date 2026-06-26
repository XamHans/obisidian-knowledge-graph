---
type: concept
stability: stable
reviewed: 2026-06
hub: LLM_Evals
evidence_status: has_receipts
---

## Why It Matters
- Eval engineering is the discipline of turning a human expert's gut feeling into a machine-readable set of rules — without this lifecycle, teams iterate blindly on prompts and models with no reliable signal of whether changes actually made things better.

## Sub-Concept Map
- Phase 1: SME annotation and open coding (the human foundation)
- Phase 2: Rubric creation and scoring contracts (the yardstick)
- Phase 3: LLM judge configuration with few-shot examples
- Phase 4: Meta-evaluation and alignment testing (evaluating the evaluator)
- Phase 5: Trace-level debugging for agentic systems
- Phase 6: Continuous monitoring and criteria drift detection

## Playbook Moves

### Phase 1 — The Human Foundation
- **Have an SME label 50-100 model outputs with pass/fail + one-sentence failure reason** — not just thumbs up/down but "why" for every label. These failure reasons become the raw material for rubric creation. *Receipt:* [[Resources/Processed_Transcripts/SME_In_The_Loop_Eval_Engineering_Galileo#^sme-loop-workflow]]
- **Open coding: cluster SME failure reasons into 3-5 themes** — group failures by pattern (e.g., "Hallucination," "Missing Disclaimer," "Tone Violation"). You can't fix "bad quality" in general; you can only fix specific categories. *Receipt:* [[Resources/Processed_Transcripts/SME_In_The_Loop_Eval_Engineering_Galileo#^fix-specific-errors]]

### Phase 2 — Building the Yardstick
- **Draft rubrics as scoring contracts with three parts: dimensions, scale, and score anchors** — dimensions define what you measure, scale defines how (binary preferred), anchors define what each score looks like with concrete examples. Without anchors, two judges interpret the same scale differently. *Receipt:* [[Resources/Processed_Transcripts/SME_In_The_Loop_Eval_Engineering_Galileo#^rubric-three-parts]]
- **Start with binary pass/fail** — maximizes inter-rater agreement and forces definitional clarity. Add granularity only when binary plateaus. *Receipt:* [[Resources/Processed_Transcripts/SME_In_The_Loop_Eval_Engineering_Galileo#^binary-vs-scale-scoring]]

### Phase 3 — Judge Configuration
- **Prompt the LLM judge with rubric + few-shot golden examples (one pass, one fail per dimension)** — LLMs learn best by example; this "clones" the SME's judgment into the automated system.
- **Treat the evaluator prompt like code** — version it, test it, iterate on it until scores consistently match SME scores. *Receipt:* [[Resources/Processed_Transcripts/SME_In_The_Loop_Eval_Engineering_Galileo#^evaluator-prompt-as-code]]

### Phase 4 — Meta-Evaluation (Evaluating the Evaluator)
- **Measure judge-human agreement with Cohen's Kappa, not raw percent agreement** — Kappa corrects for chance, preventing inflated scores on imbalanced datasets. Target: Kappa >0.80. *Receipt:* [[Resources/Processed_Transcripts/SME_In_The_Loop_Eval_Engineering_Galileo#^cohens-kappa-over-accuracy]]
- **Use confusion matrices to diagnose harsh vs lenient judge bias** — reveals systematic directional errors per rubric dimension. *Receipt:* [[Resources/Processed_Transcripts/SME_In_The_Loop_Eval_Engineering_Galileo#^confusion-matrix-judge]]
- **Cluster disagreements and amend the rubric per cluster** — every disagreement is a rubric bug, not noise. *Receipt:* [[Resources/Processed_Transcripts/SME_In_The_Loop_Eval_Engineering_Galileo#^rubric-iteration-from-disagreement]]

### Phase 5 — Trace Debugging (For Agentic Systems)
- **Look at the trace, not just the final answer** — see which tools the agent called, what its reasoning was, where it went off the rails. Aggregate metrics hide whether failures are retrieval or reasoning problems. *Receipt:* [[Resources/Processed_Transcripts/Improving_Agentic_Products_Adam_Lucek#^trace-debug-failure-analysis]]
- **Build failure taxonomies by category: planning, tool use, recovery** — enables targeted improvements instead of shotgun prompt changes. *Receipt:* [[Resources/Processed_Transcripts/Improving_Agentic_Products_Adam_Lucek#^failure-taxonomy-agentic]]

### Phase 6 — Continuous Monitoring
- **Periodically sample production data for SME re-validation** — user behavior changes over time; rubrics that worked at launch stop catching new failure modes. *Receipt:* [[Resources/Processed_Transcripts/Improving_Agentic_Products_Adam_Lucek#^criteria-drift]]
- **Select metrics that match the failure mode you're detecting** — misaligned metrics hide real problems (measuring "helpfulness" when the concern is "compliance"). *Receipt:* [[Resources/Processed_Transcripts/Improving_Agentic_Products_Adam_Lucek#^eval-metric-selection]]

## Source Transcripts
- [[Resources/Processed_Transcripts/SME_In_The_Loop_Eval_Engineering_Galileo#^sme-loop-workflow]]
- [[Resources/Processed_Transcripts/SME_In_The_Loop_Eval_Engineering_Galileo#^rubric-three-parts]]
- [[Resources/Processed_Transcripts/SME_In_The_Loop_Eval_Engineering_Galileo#^cohens-kappa-over-accuracy]]
- [[Resources/Processed_Transcripts/Improving_Agentic_Products_Adam_Lucek#^trace-debug-failure-analysis]]
- [[Resources/Processed_Transcripts/Improving_Agentic_Products_Adam_Lucek#^criteria-drift]]

## Connected Projects
- [[START_HERE]]

## Linked Technologies
- [[Tools/Phoenix]]

## Related Concepts
- [[Concepts/LLM_As_Judge_Evaluation]]
- [[Concepts/LLM_Judge_Meta_Evaluation]]
- [[Concepts/Agent_Observability_And_Evaluation]]
- [[Concepts/Agent_Evaluation_And_Benchmarking]]
- [[Concepts/Evaluation_Metrics_Classification_Regression]]

> Related Hub: [[Hubs/LLM_Evals]]
> Core Node: [[START_HERE]]
