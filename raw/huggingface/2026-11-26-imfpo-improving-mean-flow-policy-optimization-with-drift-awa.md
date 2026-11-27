---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.906244+00:00
arxiv_id: 2611.33922
url: https://huggingface.co/papers/2611.33922
arxiv_url: https://arxiv.org/abs/2611.33922
date: 2026-11-26
---

# iMFPO: Improving Mean Flow Policy Optimization with Drift-Aware Velocity Alignment for Embodied Control

Flow-based generative policies offer expressive action modeling for embodied control, yet achieving efficient one-step generation under reward-driven policy optimization remains challenging. In particular, evolving action distributions during online reinforcement learning may introduce inconsistencies between instantaneous-velocity learning and interval-averaged action generation. To address this challenge, we propose iMFPO, a one-step generative policy optimization framework with decoupled velocity learning and drift-aware velocity alignment. A shared interval-conditioned actor supports instantaneous-velocity supervision and interval-averaged action generation. JVP-corrected velocity regression is jointly optimized with reward-driven policy objectives, with action-level guidance from a frozen PPO teacher during training. At inference, iMFPO directly generates actions through interval-averaged velocity prediction, achieving one-step control without iterative flow integration. Across Go2, G1, H1, and Spot, zero-latent evaluation yields mean returns of 35.69, 34.44, 416.23, and 29.86. On Go2, action-generation latency drops from 15.57 ms to 0.41 ms relative to 64-step RFPO. Code: https://github.com/AIGeeksGroup/iMFPO. Website: https://aigeeksgroup.github.io/iMFPO.
