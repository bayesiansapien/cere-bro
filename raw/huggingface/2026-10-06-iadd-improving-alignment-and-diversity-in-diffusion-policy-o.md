---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.01789
url: https://huggingface.co/papers/2610.01789
arxiv_url: https://arxiv.org/abs/2610.01789
date: 2026-10-06
---

# iADD: Improving Alignment and Diversity in Diffusion Policy Optimization

Reinforcement learning based post training of diffusion models, such as Denoising Diffusion Policy Optimization (DDPO), optimizes a reverse diffusion process under a reward function. However, current approaches to reward optimizations do so at the cost of diversity and quality. In this paper, we provide better tradeoffs through careful theoretical considerations and method design. We analyze the theoretical framework and mathematically demonstrate that only-latter timestep updates of diffusion model may be harmful for diversity contrary to the conclusions presented in a previous work. Additionally, we propose an incremental Feynman-Kac training based on strong theoretical foundations in order to achieve the best-yet alignment-diversity tradeoffs. We perform extensive experiments and compare our method against related diffusion policy optimization approaches in three different tasks and also provide strong ablations for each component, thus validating strong performance gains in both alignment and diversity.
