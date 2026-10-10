---
source: farmer/huggingface
farmed: 2026-10-10T05:09:51.412986+00:00
arxiv_id: 2610.02967
url: https://huggingface.co/papers/2610.02967
arxiv_url: https://arxiv.org/abs/2610.02967
date: 2026-10-09
---

# Post-Training Frontier Text-to-Image Models by Composing Preference and Rubric Rewards

Recent text-to-image generation models have achieved remarkable visual quality, but improving them through post-training remains challenging because no single reward signal captures the full range of human preference. In this work, we develop a simple and effective post-training recipe for open-domain text-to-image generation based on the composition of complementary reward signals. Our reward system consists of two main components: a preference reward, trained on large-scale human preference data using a Bradley-Terry objective to capture overall human aesthetic and perceptual preferences, and rubric-based rewards, which explicitly evaluate prompt faithfulness and other desirable properties while providing safeguards against reward hacking. A key challenge is how to combine these heterogeneous reward signals. We show that a naive weighted average leads to suboptimal optimization behavior, and propose a simple reward composition strategy that more effectively balances preference optimization with rubric satisfaction. In the Arena text-to-image leaderboard (https://arena.ai/), our RL-trained Flux2dev achieves an Elo rating 69 points above the base model, and our post-trained Ideogram-4 surpasses every open-source model on the leaderboard, reaching an Elo of 1223.5. (Claims of state-of-the-art performance are based on the Arena leaderboard snapshot as of September 4, 2026.) Our results suggest that effective rewards for frontier generative-model training require broad coverage of user intent and robustness to exploitation under optimization. To support reproducible research, we release Arena-T2I-Training, a 1K subset of training data that recovers some gains of full-scale training, providing a resource that we hope will facilitate future work on post-training for text-to-image models.
