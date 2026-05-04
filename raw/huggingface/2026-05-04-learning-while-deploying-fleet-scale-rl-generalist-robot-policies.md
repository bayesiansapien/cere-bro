---
source: farmer/huggingface
farmed: 2026-05-04T00:00:00Z
arxiv_id: 2605.00416
url: https://huggingface.co/papers/2605.00416
arxiv_url: https://arxiv.org/abs/2605.00416
date: 2026-05-04
---

# Learning while Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies

Generalist robot policies increasingly benefit from large-scale pretraining, but offline data alone is insufficient for robust real-world deployment. Deployed robots encounter distribution shifts, long-tail failures, task variations, and human correction opportunities that fixed demonstration datasets cannot fully capture. We present Learning While Deploying (LWD), a fleet-scale offline-to-online reinforcement learning framework for continual post-training of generalist Vision-Language-Action (VLA) policies. Starting from a pretrained VLA policy, LWD closes the loop between deployment, shared physical experience, policy improvement, and redeployment by using autonomous rollouts and human interventions collected across a robot fleet. To stabilize learning from heterogeneous, sparse-reward fleet data, LWD combines Distributional Implicit Value Learning (DIVL) for robust value estimation with Q-learning via Adjoint Matching (QAM) for policy extraction in flow-based VLA action generators. We validate LWD on a fleet of 16 dual-arm robots across eight real-world manipulation tasks, including semantic grocery restocking and 3-5 minute long-horizon tasks. A single generalist policy improves as fleet experience accumulates, reaching an average success rate of 95%, with the largest gains on long-horizon tasks.
