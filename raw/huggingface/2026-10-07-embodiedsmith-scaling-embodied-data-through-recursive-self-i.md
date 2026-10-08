---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.07969
url: https://huggingface.co/papers/2610.07969
arxiv_url: https://arxiv.org/abs/2610.07969
date: 2026-10-07
---

# EmbodiedSmith: Scaling Embodied Data through Recursive Self-Improvement Flywheel in Simulation

Scaling robotic foundation models requires diverse training data and reliable evaluation environments. Simulation offers a scalable solution, yet existing generation pipelines remain constrained by predefined assets and skills, a disconnect between scene generation and task generation, and limited support for complex embodiments and physics. We introduce EmbodiedSmith, a framework for scalable embodied data generation through recursive self-improvement (RSI). EmbodiedSmith unifies asset, scene, and task generation in a pipeline that supports autonomous creation and language-driven customization. Its core is an agentic refinement loop: scene generation anticipates downstream task requirements, while task generation guides targeted scene edits, allowing scenes and tasks to iteratively improve one another. This joint refinement improves task generation success, including for long-horizon tasks. The framework further supports mobile manipulators, humanoids, and dexterous hands, as well as interactions involving deformable objects and fluids, broadening the range of behaviors and physical phenomena represented in generated data. Together, these capabilities provide a flexible simulation engine for both robot pretraining and evaluation. Extensive experiments validate the quality, diversity, and generation efficiency of the resulting data, while downstream policy experiments demonstrate that increased data diversity improves generalization.
