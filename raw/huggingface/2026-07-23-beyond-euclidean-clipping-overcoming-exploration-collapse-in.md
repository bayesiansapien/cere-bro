---
source: farmer/huggingface
farmed: 2026-07-24T23:47:01.610703+05:30
arxiv_id: 2607.10169
url: https://huggingface.co/papers/2607.10169
arxiv_url: https://arxiv.org/abs/2607.10169
date: 2026-07-23
---

# Beyond Euclidean Clipping: Overcoming Exploration Collapse in LLM RL via Riemannian Isometric Policy Optimization

Reinforcement learning (RL) has become a dominant paradigm for enhancing LLMs' reasoning capabilities. However, RL algorithms with PPO-Clip are inherently limited by exploration collapse. Subsequent works remain primarily heuristic and fail to identify the essential cause of PPO-Clip's failure. This work reveals the fundamental flaw of PPO-Clip: it implicitly measures policy discrepancy using Euclidean metric, which is theoretically inconsistent with the intrinsic geometry on the policy Riemannian manifold. This geometric mismatch results in overly conservative updates in low-probability regions while aggressive in high-probability regions, ultimately collapsing exploration. To correct this geometric flaw, we propose Riemannian Isometric Policy Optimization (RIPO), which guarantees isometric policy updates on the Riemannian manifold, effectively balancing exploration and exploitation. We further show that RIPO achieves a favorable bias-variance trade-off, which stabilizes optimization. Extensive experiments demonstrate that RIPO significantly surpasses existing LLM RL algorithms across seven competition-level benchmarks (up to 60% improvement over GRPO on AIME24).
