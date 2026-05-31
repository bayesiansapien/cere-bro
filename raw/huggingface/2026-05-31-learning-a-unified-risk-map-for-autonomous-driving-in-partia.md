---
source: farmer/huggingface
farmed: 2026-05-31T09:25:04Z
arxiv_id: 2605.22189
url: https://huggingface.co/papers/2605.22189
arxiv_url: https://arxiv.org/abs/2605.22189
date: 2026-05-31
---

# Learning A Unified Risk Map for Autonomous Driving in Partially Observable Environments

Occlusion-aware prediction remains a critical challenge in autonomous driving due to the inherent uncertainty of unobserved regions. Existing approaches either overestimate risk based on reachable states or struggle to predict accurate trajectories under high occlusion uncertainty. To address these limitations, we propose a unified risk map modeling and learning framework for partially observable environments. Our method integrates traffic flow risk and collision risk through spatiotemporal modeling, enabling fine-grained assessment of occlusion-induced hazards. To address the scarcity of scenarios involving occluded interactions, we introduce a diffusion-based scenario generation framework that produces realistic yet adversarial scenarios. We integrate the modeling and learning of a unified risk map into a framework that supports risk-aware planning under partial observability. Experiments on the Waymo Open Motion Dataset show that our method significantly outperforms the state-of-the-art occlusion-aware baseline, improving minimum time-to-collision by 0.78 times and average time-to-collision by 1.67 times. The proposed framework offers a comprehensive and practical solution for risk-aware planning in partially observable environments.
