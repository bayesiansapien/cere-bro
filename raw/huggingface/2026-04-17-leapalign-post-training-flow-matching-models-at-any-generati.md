---
source: farmer/huggingface
farmed: 2026-04-17T07:40:59Z
arxiv_id: 2604.15311
url: https://huggingface.co/papers/2604.15311
arxiv_url: https://arxiv.org/abs/2604.15311
date: 2026-04-17
---

# LeapAlign: Post-Training Flow Matching Models at Any Generation Step by Building Two-Step Trajectories

This paper focuses on the alignment of flow matching models with human preferences. A promising way is fine-tuning by directly backpropagating reward gradients through the differentiable generation process of flow matching. However, backpropagating through long trajectories results in prohibitive memory costs and gradient explosion. Therefore, direct-gradient methods struggle to update early generation steps, which are crucial for determining the global structure of the final image. To address this issue, we introduce LeapAlign, a fine-tuning method that reduces computational cost and enables direct gradient propagation from reward to early generation steps. Specifically, we shorten the long trajectory into only two steps by designing two consecutive leaps, each skipping multiple ODE sampling steps and predicting future latents in a single step. By randomizing the start and end timesteps of the leaps, LeapAlign leads to efficient and stable model updates at any generation step. When fine-tuning the Flux model, LeapAlign consistently outperforms state-of-the-art GRPO-based and direct-gradient methods across various metrics, achieving superior image quality and image-text alignment.
