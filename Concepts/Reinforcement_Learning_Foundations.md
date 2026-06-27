---
type: concept
title: Reinforcement Learning Foundations
description: Learning a policy by trial-and-error to maximize cumulative reward — the MDP framing behind control, and RLHF for LLM alignment.
tags: [machine-learning, reinforcement-learning, rlhf, policy-optimization]
reviewed: 2026-06
evidence_status: has_receipts
---

## Why It Matters
- RL targets **sequential decision-making**, where each action changes future state and reward is often delayed — a regime [[Concepts/Supervised_Learning]] does not cover. It is also no longer niche: via **RLHF/RLAIF** it is the standard way to align LLMs to human preference.

## The MDP Frame
- A Markov Decision Process is `(S, A, P, R, γ)` with the **Markov property**: the next-state distribution `P(s'|s,a)` depends only on the *current* state-action — which is what makes the Bellman recursions valid.
- The agent learns a **policy** `π(a|s)` to maximize expected **cumulative discounted reward**: `π* = arg max_π J(π)`. The defining tension is **exploration vs. exploitation**.

## Method Families
- **Value-based** — learn `Q(s,a)`, act greedily (Q-learning, **DQN**). Deep value-based RL only became stable thanks to two tricks: **experience replay** (decorrelate samples) and a **separate target network** (stabilize the bootstrap target).
- **Policy gradient** — optimize the policy directly. **PPO** maximizes a surrogate over the probability ratio `r_t(θ) = π_θ(a|s)/π_old(a|s)`, **clipped to `[1−ε, 1+ε]`** (default ε≈0.2), taking the min of clipped/unclipped terms — a cheap first-order approximation of TRPO's trust region.
- **Actor–critic** — a critic estimates value (e.g. via GAE) to cut the variance of the policy gradient. Note PPO *is* an actor-critic method; the families overlap rather than being disjoint.

## The Hard Parts
- **Reward hacking** — the agent optimizes the *proxy* you wrote, not what you meant (Goodhart's law); a misspecified reward gets gamed.
- **Sample efficiency, credit assignment** (which earlier action caused a late reward?), and **training stability** are the recurring failure modes.

## Why It Matters for LLMs
- **RLHF is three steps, not two:** (1) **SFT** on demonstrations → (2) train a **reward model** from human *rankings* of outputs → (3) optimize the LLM with **PPO** against it. Crucially the objective is `reward − β·KL(π_θ ‖ π_ref)` — the **KL penalty** to the frozen reference policy is what prevents the model from reward-hacking into gibberish.
- **DPO** uses a closed-form reward↔policy reparameterization to collapse RLHF into a **single classification loss on preference pairs** — no reward model, no sampling/RL loop, so it's more stable and cheaper.
- **GRPO** drops PPO's **critic**: it samples a *group* of outputs per prompt and uses the group's mean/std reward as the advantage baseline (≈halves memory) — the algorithm behind DeepSeekMath / DeepSeek-R1. See _next-wave_ `Preference_Optimization_RLHF_DPO`.

## Related
- [[Concepts/Supervised_Learning]], [[Concepts/Model_Generalization_And_Overfitting]]
- _Next-wave (forward refs):_ [[Concepts/Preference_Optimization_RLHF_DPO]], [[Concepts/Alignment_And_Safety_Tuning]]
- Hub: [[Hubs/Machine_Learning]]

## Sources
- [Spinning Up — Key Concepts in RL (OpenAI)](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html) — states/actions, policy, return, value functions, the RL objective.
- [Playing Atari with Deep Reinforcement Learning (DQN, Mnih et al., arXiv:1312.5602)](https://arxiv.org/abs/1312.5602) — value-based deep RL with experience replay.
- [Proximal Policy Optimization Algorithms (Schulman et al., arXiv:1707.06347)](https://arxiv.org/abs/1707.06347) — the clipped-surrogate policy-gradient workhorse.
- [Training LMs to follow instructions with human feedback (InstructGPT, Ouyang et al., arXiv:2203.02155)](https://arxiv.org/abs/2203.02155) — the canonical 3-step RLHF pipeline.
- [Direct Preference Optimization (Rafailov et al., arXiv:2305.18290)](https://arxiv.org/abs/2305.18290) — RLHF as a single classification loss, no reward model.
- [DeepSeekMath / GRPO (Shao et al., arXiv:2402.03300)](https://arxiv.org/abs/2402.03300) — critic-free, group-relative PPO variant.

> Core Node: [[START_HERE]]
