---
source: farmer/huggingface
farmed: 2026-08-03T12:36:11.005337+05:30
arxiv_id: 2607.18082
url: https://huggingface.co/papers/2607.18082
arxiv_url: https://arxiv.org/abs/2607.18082
date: 2026-08-03
---

# Enhancing Rubric-based RL via Self-Distillation

Rubric-based RL has recently shown promise in improving LLMs on open-ended tasks. A widely recognized limitation of rubric-based RL is limited exploration: criteria that no rollout manages to satisfy (Unexplored Criteria, UC) receive no optimization signal. Recent methods address this by incorporating rubric information as external guidance during rollout, yet they introduce a train-inference mismatch: the policy is optimized on rollouts produced under external guidance while this guidance is absent at inference time, causing error accumulation through autoregressive decoding. Moreover, these exploration-focused approaches overlook a fundamentally different failure mode that we term Suppressed Criteria (SC) -- criteria that are satisfied by some rollouts yet whose learning signals are lost during optimization because scalar reward aggregation assigns them non-positive aggregate advantages. Our analysis reveals that SC are remarkably prevalent: over 57% of samples exhibit this failure mode throughout training, with an average of 1.8 SC per sample. To simultaneously address both UC and SC without introducing training-inference mismatch, we propose Criterion-Distilled Policy Optimization (CriPO), which enhances rubric-based RL via on-policy self-distillation. For UC, CriPO constructs a criterion-injection self-teacher and computes a localized forward-KL loss to inject missing behaviors into the policy. For SC, CriPO employs a counterfactual self-teacher to locate criterion-relevant tokens in negative-advantage rollouts and flips their token-level advantages to positive values, preserving useful patterns that would otherwise be suppressed. Experiments on medicine and science benchmarks demonstrate that CriPO consistently outperforms rubric-based RL, achieving stronger final performance with approximately 2times fewer optimization steps.
