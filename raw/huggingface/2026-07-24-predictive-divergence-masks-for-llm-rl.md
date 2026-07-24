---
source: farmer/huggingface
farmed: 2026-07-24T23:47:01.610703+05:30
arxiv_id: 2607.10848
url: https://huggingface.co/papers/2607.10848
arxiv_url: https://arxiv.org/abs/2607.10848
date: 2026-07-24
---

# Predictive Divergence Masks for LLM RL

Reinforcement learning for large language models (LLMs) typically relies on trust-region masks to stabilize off-policy updates. The dominant PPO-style approach uses the sampled-token importance ratio for two criteria: a proximity criterion, which asks whether the policy has moved too far from the behavior policy, and a direction criterion, which asks whether the update pushes it farther away. Recent work DPPO improves the proximity criterion by replacing PPO's ratio-based test with a probability divergence between the behavior and training policies. However, its direction criterion is still inherited from PPO. A token can be masked only when the sampled-token importance ratio moves away from one. We observe that this ratio-based direction criterion is a single-sample proxy that can disagree in sign with the change of the divergence that defines the proximity criterion. We therefore propose the predictive divergence mask, which asks whether the next policy-gradient step will increase or decrease the same divergence used by the trust region. For the discrete softmax policies used in LLM RL, we derive this prediction in closed form. Because production rollout engines expose only a truncated (top-K) view of the vocabulary, we develop two lightweight top-K estimators for this prediction. Detailed analysis shows the divergence-based direction is better aligned with the realized change of the divergence than the sampled ratio, and the resulting masks improve RL training across model scales and precision settings.
