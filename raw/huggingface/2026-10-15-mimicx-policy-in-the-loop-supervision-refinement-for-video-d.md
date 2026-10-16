---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.233100+05:30
arxiv_id: 2610.09055
url: https://huggingface.co/papers/2610.09055
arxiv_url: https://arxiv.org/abs/2610.09055
date: 2026-10-15
---

# MimicX: Policy-in-the-Loop Supervision Refinement for Video-Driven Humanoid Motion Tracking

Human videos provide rich motion targets for humanoid learning, yet visually plausible references can still produce persistent failures under physics-based execution. These failures reveal where training supervision should change. We present MimicX, a policy-in-the-loop framework that uses execution feedback to refine video-driven humanoid motion tracking. Starting from reconstructed and retargeted motion, MimicX localizes difficult transitions and affected body regions, then jointly adapts tracking objectives and the reset curriculum for policy continuation. Repeated rollout verification selects execution-priority improvements subject to tracking guards. Across four core video tasks, MimicX consistently improves tracking accuracy and Robust Execution Horizon relative to the Fixed Reference baseline. Task-averaged results show a 25.7% reduction in body-tracking error and a 255.6% increase in execution horizon. Additional video, motion-reference, and collision-scene studies evaluate the method beyond the core tasks, while MimicX-HLoop accelerates feedback through heterogeneous execution. Overall, MimicX turns policy failure into actionable supervision for deciding what to refine and which refinement to retain.
