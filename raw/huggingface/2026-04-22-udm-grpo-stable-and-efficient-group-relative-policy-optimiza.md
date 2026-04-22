---
source: farmer/huggingface
farmed: 2026-04-22T00:00:00
arxiv_id: 2604.18518
url: https://huggingface.co/papers/2604.18518
arxiv_url: https://arxiv.org/abs/2604.18518
date: 2026-04-22
---

# UDM-GRPO: Stable and Efficient Group Relative Policy Optimization for Uniform Discrete Diffusion Models

Uniform Discrete Diffusion Model (UDM) has recently emerged as a promising paradigm for discrete generative modeling; however, its integration with reinforcement learning remains largely unexplored. We observe that naively applying GRPO to UDM leads to training instability and marginal performance gains. To address this, we propose UDM-GRPO, the first framework to integrate UDM with RL. Our method is guided by two key insights: (i) treating the final clean sample as the action provides more accurate and stable optimization signals; and (ii) reconstructing trajectories via the diffusion forward process better aligns probability paths with the pretraining distribution. Additionally, we introduce two strategies, Reduced-Step and CFG-Free, to further improve training efficiency. UDM-GRPO significantly improves base model performance across multiple T2I tasks. Notably, GenEval accuracy improves from 69% to 96% and PickScore increases from 20.46 to 23.81, achieving state-of-the-art performance in both continuous and discrete settings.
