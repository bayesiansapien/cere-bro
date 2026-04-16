---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13398
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13398
published: 2026-04-16
authors: Shihao Zhang, Ziwei Wang, Jie Zhou
---

# From Prediction to Justification: Aligning Sentiment Reasoning with Human Rationale via Reinforcement Learning

**arXiv:** https://arxiv.org/abs/2604.13398
**Authors:** Shihao Zhang, Ziwei Wang, Jie Zhou

## Abstract

arXiv:2604.13398v1 Announce Type: cross  Abstract: While Aspect-based Sentiment Analysis (ABSA) systems have achieved high accuracy in identifying sentiment polarities, they often operate as "black boxes," lacking the explicit reasoning capabilities characteristic of human affective cognition. Humans do not merely categorize sentiment; they construct causal explanations for their judgments. To bridge this gap, we propose ABSA-R1, a large language model framework designed to mimic this ``reason-before-predict" cognitive process. By leveraging reinforcement learning (RL), ABSA-R1 learns to articulate the why behind the what, generating natural language justifications that ground its sentiment predictions. We introduce a Cognition-Aligned Reward Model (formerly sentiment-aware reward model) that enforces consistency between the generated reasoning path and the final emotional label. Furthermore, inspired by metacognitive monitoring, we implement a performance-driven rejection sampling strategy that selectively targets hard cases where the model's internal reasoning is uncertain or inconsistent. Experimental results on four benchmarks demonstrate that equipping models with this explicit reasoning capability not only enhances interpretability but also yields superior performance in sentiment classification and triplet extraction compared to non-reasoning baselines.
