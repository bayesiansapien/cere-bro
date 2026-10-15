---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.507601+00:00
arxiv_id: 2610.14351
url: https://huggingface.co/papers/2610.14351
arxiv_url: https://arxiv.org/abs/2610.14351
date: 2026-10-14
---

# Learning Transferable World-Action Models from Task-Paired Human Videos

World-action models inherit broad visual and physical priors from video pre-training. However, standard within-video next-frame prediction allows them to rely on appearance shared between the context and future, rather than learning interactions that transfer across scenes and embodiments. We introduce WATCH, a cross-video pre-training that learns from task-paired human demonstrations collected across diverse environments. Conditioned on the video and actions of one demonstration, the model jointly predicts another demonstration's actions and future frames from its current observation. Predicting one demonstration from another encourages the model to learn task-relevant interactions that transfer across scenes and demonstrators. Our pre-training shows that these capabilities can be learned from readily scalable human-human pairs alone, without requiring matched human-robot demonstrations. Analyses before robot post-training show improved motion alignment across embodiments and better action and video prediction on unseen robots, with representations closer to those learned from robot pairs. After robot post-training, WATCH improves MimicDroid in-context success from 40.9% to 68.3% with Cosmos Policy and from 59.8% to 77.7% with Cosmos3, with the largest gains on the unseen levels. Gains persist under context-free post-training across robot embodiments. WATCH outperforms within-video pre-training and co-training baselines, supporting cross-video prediction as a scalable approach to learning transferable world-action representations.
