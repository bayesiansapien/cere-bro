---
source: farmer/huggingface
farmed: 2026-05-10T03:37:12Z
arxiv_id: 2605.04077
url: https://huggingface.co/papers/2605.04077
arxiv_url: https://arxiv.org/abs/2605.04077
date: 2026-05-10
---

# Balanced Aggregation: Understanding and Fixing Aggregation Bias in GRPO

Reinforcement learning with verifiable rewards (RLVR) has become a central paradigm for improving reasoning and code generation in large language models, and GRPO-style training is widely adopted for its simplicity and effectiveness. We show that token aggregation introduces sign-length coupling, while sequence aggregation implicitly downweights longer responses. We propose Balanced Aggregation (BA), a simple drop-in replacement that computes token-level means separately within the positive and negative subsets and then combines them with sequence-count-based weights. Experiments with Qwen2.5-Math-7B and Qwen3-1.7B show that BA consistently improves training stability and final performance.
