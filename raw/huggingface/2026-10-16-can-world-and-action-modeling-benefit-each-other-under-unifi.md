---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.21095
url: https://huggingface.co/papers/2610.21095
arxiv_url: https://arxiv.org/abs/2610.21095
date: 2026-10-16
---

# Can World and Action Modeling Benefit Each Other under Unified Causal Training?

World and action modeling are closely related, yet their reciprocal benefits under unified causal training remain unclear. We introduce OneWM, a simple framework for unified causal training that treats actions as both conditions for world prediction and targets for policy learning within a shared video-action architecture. Using this framework, we investigate whether learning forward dynamics conditioned on specified actions improves action learning, and whether learning to generate actions in turn improves action-conditioned world modeling. We use LIBERO, LIBERO-Plus, and RoboCasa365 as embodied testbeds to evaluate both policy learning and world modeling, complemented by real-world policy experiments. Learning the visual consequences of specified actions improves policy performance and generalization across changing scenes. In turn, action learning improves multi-view world-prediction fidelity under the same architecture. Together, these results answer both questions positively, supporting reciprocal benefits between world modeling and action generation under unified causal training.
