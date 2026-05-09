---
source: farmer/huggingface
farmed: 2026-05-09T03:37:34Z
arxiv_id: 2605.06200
url: https://huggingface.co/papers/2605.06200
arxiv_url: https://arxiv.org/abs/2605.06200
date: 2026-05-09
---

# A^2TGPO: Agentic Turn-Group Policy Optimization with Adaptive Turn-level Clipping

Reinforcement learning for agentic large language models (LLMs) typically relies on a sparse, trajectory-level outcome reward, making it difficult to evaluate the contribution of individual tool-calls within multi-turn interactions. We propose A2TGPO (Agentic Turn-Group Policy Optimization with Adaptive Turn-level Clipping), which retains Information Gain (IG) as the intrinsic signal but redesigns how it is normalized, accumulated, and consumed: turn-group normalization, variance-rescaled discounted accumulation, and adaptive turn-level clipping. On seven single-hop and multi-hop QA benchmarks across three backbones, A2TGPO consistently outperforms prior strong baselines, improving over existing RL methods by +1.75 on multi-hop and +1.69 on single-hop on average.
