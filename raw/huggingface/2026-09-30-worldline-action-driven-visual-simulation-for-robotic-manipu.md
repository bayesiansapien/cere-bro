---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.38059
url: https://huggingface.co/papers/2609.38059
arxiv_url: https://arxiv.org/abs/2609.38059
date: 2026-09-30
---

# WorldLine: Action-Driven Visual Simulation for Robotic Manipulation

Real-world robot learning is constrained by the cost of collecting experience and evaluating candidate behaviors. Video generation models offer a scalable foundation for visual simulators that predict action outcomes before physical execution. Yet they often favor visual plausibility over accurate action following and coherent robot--object dynamics, while action-conditioned simulators depend on scarce, embodiment-specific data that are difficult to share across incompatible control spaces. We introduce WorldLine, an action-driven visual simulator that decouples transferable dynamics learning from heterogeneous action grounding. WorldLine learns manipulation dynamics from more than 10,000 hours of action-free robot videos and grounds them using over 2,000 hours of action trajectories across more than ten embodiments. An image-space action representation provides a shared control interface across embodiments, while multi-view and failure-enriched training with relational regularization improves interaction-sensitive prediction. Robot-focused few-step distillation enables efficient causal rollout while preserving action-critical motion. Across held-out and out-of-domain settings, WorldLine maintains strong visual quality and robot-motion agreement; on failed trajectories, it improves robot-mask IoU by 0.1626 over the strongest baseline. It predicts trajectory success with 74% mean accuracy across RoboTwin and AgiBot, one percentage point above the strongest baseline. Without RoboTwin training or adaptation, its rollouts improve task success by up to 21.4 percentage points over direct policy execution. Together, these capabilities make WorldLine a scalable and efficient visual simulator for policy evaluation and embodied planning. More results are available at https://zhengsh123.github.io/WorldLine/{project page}.
