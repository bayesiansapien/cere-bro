---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.07332
url: https://huggingface.co/papers/2610.07332
arxiv_url: https://arxiv.org/abs/2610.07332
date: 2026-10-07
---

# Structuring MoE Expert Selection for Agentic Reinforcement Learning

Long-horizon LLM agents are frequently implemented using sparse mixture-of-experts (MoE) models, yet the co-design of agentic behavior and MoE structures remains underexplored. In this work, we comprehensively study the connections between agentic post-training and MoE expert selection. In off-the-shelf MoE models, we observe expert selection exhibits a specialized structure that naturally aligns with agentic trajectories. Specifically, expert routing overlaps more between turns where the agent performs semantically similar operations (e.g., READ, UPDATE) than between turns with differing operations. However, standard RL algorithms ignore this specialization, allowing the MoE routing to go uncontrolled during training, which empirically limit task performance and inference efficiency. To address this, we introduce a hierarchical routing control framework for agentic tasks. We explicitly encourage turn-level expert selections to align with agentic operations while regularizing token-level expert selections to maintain local consistency. To resolve stability issues that arise during post-training with the proposed methods, we further introduce an entropy-gated control mechanism. Overall, our routing control framework achieves over 10-point improvements in success rate on all evaluated benchmarks. These results demonstrate that agentic trajectory structure provides an effective signal for optimizing MoE capacity during RL post-training.
