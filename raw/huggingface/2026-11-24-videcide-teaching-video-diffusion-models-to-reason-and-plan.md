---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.919241+00:00
arxiv_id: 2611.26389
url: https://huggingface.co/papers/2611.26389
arxiv_url: https://arxiv.org/abs/2611.26389
date: 2026-11-24
---

# ViDecide: Teaching Video Diffusion Models to Reason and Plan Step by Step

Current leading video generation models can synthesize highly realistic videos, while still frequently violating physical and logical constraints in multi-step reasoning and planning, even after training with large-scale reasoning data or existing diffusion RL methods. We attribute these failures to the conventional video training paradigm, which treats a solution as a fixed-length clip rather than a chain of decisions. We present ViDecide, a decision-centric framework that trains video diffusion models to predict state transitions causally and decide when to stop, with a decision-focused training schedule. We further propose Corrective Fine-tuning (CFT), which corrects failed decisions by mapping their noise to the model's own successful continuations, achieving stable improvement without policy-gradient optimization. Across abstract games, planning tasks, and a new benchmark of multi-step robot planning, ViDecide achieves an average strict success rate of 83.8%, far above 23.3% for standard fine-tuning and 67.8% for the strongest prior method, and generalizes to larger puzzles and unseen layouts. Our framework therefore unlocks greater potential for video generation models as reliable reasoners and planners in the visual world. Project page: https://kevin-thu.github.io/ViDecide.
