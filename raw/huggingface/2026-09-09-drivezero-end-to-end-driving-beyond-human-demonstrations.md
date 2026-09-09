---
source: farmer/huggingface
farmed: 2026-09-09T05:28:24.738031+00:00
arxiv_id: 2609.06055
url: https://huggingface.co/papers/2609.06055
arxiv_url: https://arxiv.org/abs/2609.06055
date: 2026-09-09
---

# DriveZero: End-to-End Driving Beyond Human Demonstrations

Most end-to-end autonomous-driving systems learn by imitating human driving logs, leaving their learned behavior constrained by the quality and behavioral coverage of the recorded trajectories. This report presents DriveZero, an end-to-end system that learns driving behavior beyond human demonstrations. It decomposes driving into a perception model and an action model, pretrains each in the regime best suited to it, and combines them into one end-to-end planner. The two models call for different learning recipes: perception must understand the world, and benefits from massive and diverse visual data; action must interact with it, and requires closed-loop feedback. On the action side, we introduce DriveRL, a mixed-agent closed-loop reinforcement-learning framework. It converts real driving logs into interactive worlds, where a privileged teacher policy is trained with PPO through closed-loop rollouts. For the perception model, DriveVFM consolidates multiple frozen vision foundation models, including DINOv3, SigLIP2, SAM and Depth Anything V2, into a single backbone from raw images alone, requiring no task-specific annotations. DriveZero then unifies the two: a camera-only planner that distills the frozen DriveRL teacher through its rolled-out trajectories. The goal-conditioned teacher can moreover be queried under augmented driving intents, yielding diverse, goal-consistent supervision that logged data cannot provide. On nuPlan, DriveRL with value-guided test-time action search achieves a mean score of 93.57 across the Val14, Test14-hard, and Test14-random community splits in both non-reactive and reactive modes, exceeding the Log-Replay expert on all three splits. DriveZero achieves state-of-the-art performance on NAVSIMv1, NAVSIMv2 and the closed-loop HUGSIM benchmark without any human trajectory supervision.
