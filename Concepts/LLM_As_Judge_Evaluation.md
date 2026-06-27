---
type: concept
title: LLM-as-Judge Evaluation
description: Using LLMs to grade model outputs — pointwise vs pairwise, the position/verbosity/self-enhancement biases, and human calibration.
tags: [llm, evaluation, llm-as-judge, rag-eval]
stability: evolving
reviewed: 2026-06
evidence_status: has_receipts
---

## Why It Matters
- Most generative outputs have no single ground-truth label, so classic metrics (see [[Concepts/Evaluation_Metrics_Classification_Regression]]) don't apply. LLM-as-judge scales human-like judgment to thousands of outputs — but the judge is itself a model with biases, so it must be evaluated before it gates anything.

## Three Scoring Paradigms
- **Pointwise / direct** — score one output on a rubric. Cheap and scalable, but absolute scores drift and are hard to calibrate.
- **Pairwise** — "is A or B better?" More reliable (relative is easier than absolute); underpins Chatbot Arena Elo, but is O(n²) and order-sensitive.
- **Reference-based** — grade against a gold answer, or in RAG against the retrieved context (faithfulness/groundedness).

## The Biases (name them, mitigate them)
- **Position bias** — favoring a given slot (up to ~75% in some setups) → swap/randomize order, require consistency across both orderings.
- **Verbosity bias** — preferring longer answers regardless of quality → reward conciseness in the rubric or normalize for length.
- **Self-enhancement bias** — preferring its own model family's outputs (~10–25%) → use an independent judge, mask model identities.
- General levers: few-shot exemplars, explicit chain-of-thought, decomposed rubric criteria, and ensembles/juries.

## Calibrate Against Humans
- This is the discipline that makes a judge production-grade: build a small human-labeled set, measure judge↔human agreement (with inter-annotator agreement as the ceiling), and **re-validate whenever the model, prompt, or rubric changes**. Use a small integer scale (1–5), not a float scale.

## G-Eval and Where It Fits
- **G-Eval** adds chain-of-thought "evaluation steps" + form-filling and probability-weighted (logprob) scoring for finer-grained scores that correlate better with humans.
- In RAG/agents it powers reference-free metrics (faithfulness, answer/context relevancy — see [[Concepts/RAG_Evaluation]]) and step/task-completion judging.

## Related
- [[Concepts/RAG_Evaluation]], [[Concepts/Evaluation_Metrics_Classification_Regression]], [[Concepts/Supervised_Learning]], [[Concepts/Retrieval_Augmented_Generation]]
- Hub: [[Hubs/Machine_Learning]]

## Sources
- [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena (Zheng et al., arXiv:2306.05685)](https://arxiv.org/abs/2306.05685) — the foundational paper; biases; GPT-4 >80% human agreement.
- [G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment (Liu et al., arXiv:2303.16634)](https://arxiv.org/abs/2303.16634) — CoT + probability-weighted scoring (Spearman 0.514 on SummEval).
- [LLM-as-a-judge: a complete guide (Evidently AI)](https://www.evidentlyai.com/llm-guide/llm-as-a-judge) — direct/pairwise/reference-based; validating against human labels.
- [Using LLM-as-a-judge for automated evaluation (Hugging Face Cookbook)](https://huggingface.co/learn/cookbook/en/llm_judge) — integer scales, additive rubrics, ~30-example calibration set.
- [LLM-as-a-Judge: techniques and best practices (DeepEval)](https://deepeval.com/guides/guides-llm-as-a-judge) — G-Eval, pairwise, reference-based, CI/CD validation.

> Core Node: [[START_HERE]]
