---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2609.22332
url: https://huggingface.co/papers/2609.22332
arxiv_url: https://arxiv.org/abs/2609.22332
date: 2026-10-20
---

# AffordanceWAM: Affordance-Aware Joint World-Action Modeling for Robot Manipulation

Generalizable robot manipulation requires predicting how a scene will evolve, identifying where interactions are feasible, and determining how to act. Action-labeled robot videos directly supervise control but are costly and limited in diversity, whereas egocentric human videos capture diverse interactions but lack robot actions and differ in embodiment and appearance. We introduce AffordanceWAM, an affordance-aware generative World Action Model that represents object-centric spatiotemporal affordance through Scalar Affordance and Affordance Heatmap, within the generated future World. This representation grounds visual prediction in task-relevantant objects and interaction regions for action generation, and provides shared interaction targets across human and robot videos. Built on a pretrained video diffusion Transformer, AffordanceWAM uses separately parameterized World and Action Experts, coupled through Masked Joint Self-Attention, to jointly predict future RGB observations, Scalar Affordance fields, Affordance Heatmaps, and continuous robot actions under a unified flow-matching objective. Human videos supervise all three future-World streams, whereas robot trajectories additionally provide action supervision, enabling transfer without human action labels or retargeting. Experiments on RoboCasa, CALVIN ABCrightarrowD, and real-world manipulation demonstrate consistent gains over RGB-only and robot-data-only baselines. Under fixed robot supervision, RoboCasa performance improves monotonically as affordance-annotated human video scales. These results support affordance as an effective interface for both vision-language-action learning and human-to-robot transfer.
