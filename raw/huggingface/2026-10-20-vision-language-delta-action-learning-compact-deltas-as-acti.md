---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.25874
url: https://huggingface.co/papers/2610.25874
arxiv_url: https://arxiv.org/abs/2610.25874
date: 2026-10-20
---

# Vision-Language-Delta-Action: Learning Compact Deltas as Actionable Transition Interfaces for Robotic Manipulation

Robotic manipulation is not merely observation-to-action generation, but the realization of task-specified state changes in the physical world. Existing vision-language-action (VLA) methods directly learn observation-to-action mappings, imposing a substantial learning burden due to the gap between semantic understanding and action execution. Although world-action models (WAMs) improve control through future prediction, modeling complete future states wastes capacity on static appearance and action-irrelevant changes. We propose Vision-Language-Delta-Action (VLDA), a paradigm that reformulates full future prediction as compact actionable transition modeling. Its core is a compact Delta variable that captures latent world-state changes, serving as an interface between vision-language understanding and action generation. VLDA learns Delta through a unified objective composed of the Local Transition Filter (LT-Filter) and Global Transition Anchor (GT-Anchor). LT-Filter captures task-relevant manipulation-centric changes while suppressing static reconstruction biases. GT-Anchor provides coarse future-level regularization to preserve the overall direction of state changes. Delta-Driven Action Refinement (DDAR) further grounds Delta in the action manifold and injects it as a structured seed to guide action denoising. We implement VLDA within LoongForge, an open-source training framework for large-scale foundation and embodied models, using its modular and distributed infrastructure for unified two-stage optimization. Experiments show that VLDA improves long-horizon consistency, robustness, and generalization, validating actionable Delta as an alternative to direct action prediction and full future-state modeling.
