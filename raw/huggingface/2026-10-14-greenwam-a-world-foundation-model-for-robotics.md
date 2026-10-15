---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.500067+00:00
arxiv_id: 2610.18774
url: https://huggingface.co/papers/2610.18774
arxiv_url: https://arxiv.org/abs/2610.18774
date: 2026-10-14
---

# GreenWAM: A World Foundation Model for Robotics

A robot needs a world model that predicts how its actions will change the scene and a policy that chooses those actions. Models are usually built and evaluated for only one of these roles, and every robot records its actions in its own format. We ask whether one robot world model can serve both roles across different bodies, and what makes this work. We present GreenWAM, a world foundation model for robotics, together with the recipe that produces it: (1) a shared anatomical action space that describes 20 robot families, from bimanual arms to dexterous humanoids, in common joint coordinates; (2) joint training on these families in visual, action-conditioned and world-action modes; and (3) policies that split an action expert off the generator. As a world model, GreenWAM attains top-tier trajectory, depth and 3D accuracy on WorldArena 1.0, ahead of every world-action model and video generator in our comparison. As a policy, it scores among the top entries of the RoboTwin 2.0 leaderboard, reaches the highest zero-shot LIBERO-plus success among the compared methods and is competitive with dedicated vision-language-action and world-action policies on CALVIN and LIBERO. We further adapt GreenWAM to a real humanoid, where it succeeds more often than policies adapted from π_{0.5} and from Cosmos 3 Edge, and distill it into a single-step policy for real-time control. Controlled experiments yield three findings: robot specialization improves world prediction and control together; an action expert helps when split off at the start of adaptation; and keeping world-model modes during policy adaptation preserves robustness to scene changes.
