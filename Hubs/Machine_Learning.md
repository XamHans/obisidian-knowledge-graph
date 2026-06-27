---
type: hub
title: Machine Learning
description: Entry point to ML foundations — learning paradigms, generalization, training workflow, and evaluation under modern AI systems.
tags: [machine-learning, foundations]
reviewed: 2026-06
---

## Overview
- The "why" layer beneath GenAI, RAG, and Agents: how models learn from data, what makes that learning generalize, and how you train and evaluate honestly.
- Read top to bottom: pick a learning paradigm → understand generalization → run the training workflow → evaluate and monitor.

## Map of Content
- **Learning paradigms**
  - [[Concepts/Supervised_Learning]] — labeled input→output, the production default
  - [[Concepts/Unsupervised_Learning]] — structure from unlabeled data
  - [[Concepts/Self_Supervised_Learning]] — supervision from the data itself; the pretraining paradigm
  - [[Concepts/Reinforcement_Learning_Foundations]] — policies, reward, and RLHF
- **Generalization & theory**
  - [[Concepts/Model_Generalization_And_Overfitting]] — bias–variance and what actually ships
  - [[Concepts/Bias_Variance_Tradeoff]] — the error decomposition + double descent
- **Data & features**
  - [[Concepts/Feature_Engineering]] — model-ready features and the leakage traps
  - [[Concepts/Data_Centric_AI]] — improving the data as the highest-ROI lever
- **Training workflow**
  - [[Concepts/Training_Validation_Test_Splits]] — honest splits and leakage-safe CV
  - [[Concepts/Hyperparameter_Optimization]] — efficient search + nested validation
  - [[Concepts/ML_Experiment_Tracking]] — reproducible, comparable, promotable runs
- **Evaluation & reliability**
  - [[Concepts/Evaluation_Metrics_Classification_Regression]] — picking the right metric
  - [[Concepts/Model_Calibration]] — probabilities you can trust
  - [[Concepts/LLM_As_Judge_Evaluation]] — scaling judgment to generative outputs
  - [[Concepts/Concept_Drift_And_Data_Drift]] — why production models decay
- **Related Hubs**: [[Hubs/RAG]]

> Core Node: [[START_HERE]]
