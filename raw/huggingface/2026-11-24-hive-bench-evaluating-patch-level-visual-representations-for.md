---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.925180+00:00
arxiv_id: 2611.30813
url: https://huggingface.co/papers/2611.30813
arxiv_url: https://arxiv.org/abs/2611.30813
date: 2026-11-24
---

# HIVE-Bench: Evaluating Patch-Level Visual Representations for Egocentric Robot Manipulation

Pretrained vision is a common start for robot learning, but most comparisons still score one pooled vector from a third-person image. Bimanual policies instead read dense patch tokens from cameras on the robot. We introduce HIVE-Bench: one shared flow-matching policy reads 20 encoders from seven families on 24 egocentric bimanual tasks, across adaptation, task sharing, and sweeps of data, model size, and layer. Keeping the patches matters. Averaging each view to one token removes most of the success, adaptation helps every pair we test, and one shared policy keeps most of the success of separate policies at a fraction of the updates. The same tokens are then scored with statistics, state and object readouts, published vision scores, and an inverse-dynamics readout. That readout of the commanded motion is one of the strongest measurements available before a policy is trained. Recognition, depth, and correspondence do not transfer reliably. Fine-tuning can improve the action readout even when other measurements move the other way, and no statistic is stable enough to replace a rollout before any deployment.
