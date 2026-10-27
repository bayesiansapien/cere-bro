---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.798587+00:00
arxiv_id: 2610.30932
url: https://huggingface.co/papers/2610.30932
arxiv_url: https://arxiv.org/abs/2610.30932
date: 2026-10-26
---

# UserArena: Benchmarking Interactive User Simulation for Long-Horizon Shopping Agents

Agentic recommendation pursues shopper goals through sequences of context-dependent decisions. Developing and evaluating such policies requires faithful recommendation world models that capture both the interactive shopping environment and users' behavioral responses over long interactions. Existing resources rarely provide long-horizon, fine-grained real-user trajectories or support trajectory-level evaluation and offline validation against production A/B results. We introduce UserArena, a real-world e-commerce interactive benchmark containing 64,729 session trajectories from 11,010 users, spanning 566,102 items and 13 action types. UserArena pairs these trajectories with an interactive environment and supports offline validation against outcomes from a controlled production A/B test, enabling five-level evaluation from output validity and local decisions to sequential behavior, personalization, and outcomes. To improve simulator fidelity over these long-horizon interactions, we further propose On-Policy Trajectory Distillation (OPTD), which uses trajectory-level intent to provide dense teacher targets on student-generated rollouts. Experiments show that OPTD achieves the strongest overall fidelity among the evaluated simulators under UserArena's evaluation protocol and most closely reproduces the production policy effect in offline simulation.
