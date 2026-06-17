---
source: farmer/huggingface
farmed: 2026-06-17T10:05:49Z
arxiv_id: 2606.16154
url: https://huggingface.co/papers/2606.16154
arxiv_url: https://arxiv.org/abs/2606.16154
date: 2026-06-17
---

# A Gradient Perspective on RLVR Stability and Winner Advantage Policy Optimization

Reinforcement learning with verifiable rewards (RLVR) improves language-model reasoning, but GRPO-style optimization remains prone to collapse. We analyse this instability through token-level gradient dynamics, deriving a taxonomy that predicts how updates affect next-token probabilities and entropy. The taxonomy shows that stability depends jointly on the advantage sign and token distribution under the current policy. Motivated by this finding, we propose Winner Advantage Policy Optimization (WAPO), a simple online clipped policy-gradient objective that updates only on positive-advantage completions. Across mathematical reasoning and multi-hop QA benchmarks, WAPO improves training stability and matches or outperforms baselines across multiple model families. Full code can be found at https://github.com/layer6ai-labs/wapo.
