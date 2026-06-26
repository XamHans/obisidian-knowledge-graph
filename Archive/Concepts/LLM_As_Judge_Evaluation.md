---
type: concept
stability: stable
reviewed: 2026-06
hub: Machine_Learning
evidence_status: has_receipts
---

## Why It Matters
- LLM-as-judge enables scalable qualitative evaluation but introduces judge bias, drift, and rubric fragility.

## Sub-Concept Map
- Rubric and scoring design
- Pairwise vs absolute grading
- Judge calibration and agreement checks
- Human-audit sampling
- SME-in-the-loop calibration workflow
- Cohen's Kappa for agreement measurement
- Binary vs scale scoring trade-offs
- Criteria drift and periodic re-validation

## Playbook Moves
- Start with deterministic rubric prompts and frozen evaluation sets.
- Track inter-judge agreement and disagreement hotspots.
- Calibrate with periodic human review on high-impact samples.
- **Use Cohen's Kappa (not raw percent agreement) to measure judge-human alignment** — raw percent inflates on imbalanced datasets; Kappa corrects for chance. *Receipt:* [[Resources/Processed_Transcripts/SME_In_The_Loop_Eval_Engineering_Galileo#^cohens-kappa-over-accuracy]]
- **Start with binary pass/fail scoring to maximize inter-rater agreement** — add scale granularity only when binary plateaus. *Receipt:* [[Resources/Processed_Transcripts/SME_In_The_Loop_Eval_Engineering_Galileo#^binary-vs-scale-scoring]]
- **Treat every SME-judge disagreement as a rubric bug** — cluster disagreements by theme, amend the rubric per cluster, re-evaluate. *Receipt:* [[Resources/Processed_Transcripts/SME_In_The_Loop_Eval_Engineering_Galileo#^rubric-iteration-from-disagreement]]
- **Run the iterative calibration loop: label → measure agreement → analyze disagreements → refine rubric → re-measure** — repeat until Cohen's Kappa >0.80. *Receipt:* [[Resources/Processed_Transcripts/Improving_Agentic_Products_Adam_Lucek#^judge-alignment-iteration]]

## Source Receipts
- [[Resources/Processed_Transcripts/SME_In_The_Loop_Eval_Engineering_Galileo#^sme-loop-workflow]]
- [[Resources/Processed_Transcripts/SME_In_The_Loop_Eval_Engineering_Galileo#^cohens-kappa-over-accuracy]]
- [[Resources/Processed_Transcripts/SME_In_The_Loop_Eval_Engineering_Galileo#^binary-vs-scale-scoring]]
- [[Resources/Processed_Transcripts/SME_In_The_Loop_Eval_Engineering_Galileo#^rubric-iteration-from-disagreement]]
- [[Resources/Processed_Transcripts/Improving_Agentic_Products_Adam_Lucek#^judge-alignment-iteration]]

## Connected Projects
- [[START_HERE]]

## Related Concepts
- [[Concepts/Agent_Observability_And_Evaluation]]
- [[Concepts/Evaluation_Metrics_Classification_Regression]]
- [[Concepts/RAG_Evaluation_And_Groundedness]]
- [[Concepts/LLM_Judge_Meta_Evaluation]]
- [[Concepts/Eval_Engineering_Lifecycle]]

> Related Hub: [[Hubs/LLM_Evals]]
> Core Node: [[START_HERE]]
