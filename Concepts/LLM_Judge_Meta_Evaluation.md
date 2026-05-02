---
type: concept
status: active
hub: LLM_Evals
persona: Professional Seeking AI Mastery
evidence_status: has_receipts
---

## Why It Matters
- Without evaluating the evaluator, judge prompts silently drift, rubrics go stale, and alignment with human SME judgment degrades undetected — making every downstream eval metric unreliable.

## Sub-Concept Map
- Cohen's Kappa and agreement metrics (chance-corrected reliability)
- Confusion matrix analysis for judge calibration (harsh vs lenient diagnosis)
- Dev/test split methodology for judge prompt iteration
- Stochastic rerun variance analysis (ambiguity detection)
- Binary vs scale scoring trade-offs (inter-rater agreement impact)

## Playbook Moves
- **Measure judge-human agreement with Cohen's Kappa, not just percent agreement** — raw percent agreement inflates scores on imbalanced datasets; Kappa corrects for chance. *Receipt:* [[Resources/Processed_Transcripts/SME_In_The_Loop_Eval_Engineering_Galileo#^cohens-kappa-over-accuracy]]
- **Use confusion matrices to diagnose systematic judge bias** — a judge that passes everything looks accurate on a dataset with few failures, but confusion matrices expose the asymmetry. *Receipt:* [[Resources/Processed_Transcripts/SME_In_The_Loop_Eval_Engineering_Galileo#^confusion-matrix-judge]]
- **Split eval datasets into dev/test; iterate prompts on dev, validate on held-out test** — prevents overfitting judge prompts to specific examples while preserving a clean validation signal. *Receipt:* [[Resources/Processed_Transcripts/Improving_Agentic_Products_Adam_Lucek#^dev-test-eval-split]]
- **Prefer binary pass/fail over Likert scales for initial judge calibration** — the difference between a "3" and a "4" is too subjective for both humans and LLMs; start binary, add granularity only when the binary signal plateaus. *Receipt:* [[Resources/Processed_Transcripts/SME_In_The_Loop_Eval_Engineering_Galileo#^binary-vs-scale-scoring]]

## Source Transcripts
- [[Resources/Processed_Transcripts/SME_In_The_Loop_Eval_Engineering_Galileo#^cohens-kappa-over-accuracy]]
- [[Resources/Processed_Transcripts/SME_In_The_Loop_Eval_Engineering_Galileo#^confusion-matrix-judge]]
- [[Resources/Processed_Transcripts/SME_In_The_Loop_Eval_Engineering_Galileo#^binary-vs-scale-scoring]]
- [[Resources/Processed_Transcripts/Improving_Agentic_Products_Adam_Lucek#^dev-test-eval-split]]
- [[Resources/Processed_Transcripts/Improving_Agentic_Products_Adam_Lucek#^judge-alignment-iteration]]

## Connected Projects
- [[Projects/AI_Native_Engineer]]

## Linked Technologies
- [[Resources/Software/Phoenix]]

## Related Concepts
- [[Resources/Concepts/LLM_As_Judge_Evaluation]]
- [[Resources/Concepts/Evaluation_Metrics_Classification_Regression]]
- [[Resources/Concepts/Agent_Observability_And_Evaluation]]

> Related Hub: [[Hubs/LLM_Evals]]
> Core Node: [[Projects/AI_Native_Engineer]]
