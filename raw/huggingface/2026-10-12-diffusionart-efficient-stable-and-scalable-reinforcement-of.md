---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.215547+05:30
arxiv_id: 2610.12572
url: https://huggingface.co/papers/2610.12572
arxiv_url: https://arxiv.org/abs/2610.12572
date: 2026-10-12
---

# DiffusionART: Efficient, Stable and Scalable Reinforcement of Diffusion Models

Online reinforcement learning (RL) fine-tunes diffusion models with black-box rewards, but reverse-process methods such as Flow-GRPO are limited in efficiency by poor credit assignment, while forward-process methods such as DiffusionNFT are efficient yet unstable without carefully tuned exponential-moving-average (EMA) off-policy training. We show that NFT-style objectives contain a hidden forward--reverse consistency force that joint positive--negative training cancels only partially, and that EMA stabilizes training through restoration rather than off-policy rollouts. We introduce DiffusionART (Diffusion Reinforcement with Aggregation-First Reward Tilting), which aggregates each prompt's rewards into a shared reward-improving direction for reverse-process states, removing the consistency force by construction, and adds a trust-region-masked second update for drift-adaptive restoration without EMA tuning. It requires no differentiable reward model, remains effective with fewer samples per prompt, and supports pairwise reward models (DiffusionART-Pairwise). Across image and video generation, DiffusionART trains efficiently and stably without per-task tuning. In particular, on HunyuanVideo-13B with equally weighted visual and motion quality rewards, DiffusionART reaches the late-stage mean reward levels of DiffusionNFT and Flow-GRPO-Fast with 12.02 and 11.72 times fewer GPU hours, respectively, while achieving 28.8% and 53.0% higher mean training rewards.
