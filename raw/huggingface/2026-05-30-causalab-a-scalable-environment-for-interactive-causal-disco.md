---
source: farmer/huggingface
farmed: 2026-05-30T09:33:08Z
arxiv_id: 2605.26029
url: https://huggingface.co/papers/2605.26029
arxiv_url: https://arxiv.org/abs/2605.26029
date: 2026-05-30
---

# CausaLab: A Scalable Environment for Interactive Causal Discovery Toward AI Scientists

We introduce CausaLab, a scalable environment for evaluating interactive causal discovery by LLM agents. Unlike prior evaluations, CausaLab evaluates both whether an agent can solve a problem using causal evidence and whether its answer is grounded in a faithful recovered causal mechanism. Each episode places an agent in a synthetic laboratory: it receives prior measurement records, intervenes on a manipulator crystal, and predicts the resonance frequency of a held-out reactor crystal governed by the same mechanism. The hidden data-generating process is a randomly sampled structural causal model (SCM), so success requires recovering both a causal graph and structural equations rather than recalling prior knowledge.
  Experiments show a persistent gap between prediction and mechanism recovery: in the purely observational 6-node setting, GPT-5.2-high reaches 92% task accuracy but only 0.471 all-edge F_1. Mixed observation-intervention strategies improve structural fidelity, while pure intervention remains difficult even for strong agents. We identify premature stopping as a major weakness and show that consistency verification mitigates it. CausaLab therefore separates predictive success from causal understanding and exposes current LLM agents' limits as experimental causal reasoners.
