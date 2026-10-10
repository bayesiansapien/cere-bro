---
source: farmer/huggingface
farmed: 2026-10-10T05:09:51.419718+00:00
arxiv_id: 2610.12355
url: https://huggingface.co/papers/2610.12355
arxiv_url: https://arxiv.org/abs/2610.12355
date: 2026-10-09
---

# Distilling Routed 3D Privilege for Spatial Reasoning in Vision-Language Models

Spatial reasoning remains a persistent weakness of vision-language models (VLMs), because RGB inputs do not directly provide geometric evidence. Existing remedies either inject 3D into the model at inference, paying architecture and latency costs, or train with outcome rewards that supervise only the final answer. Spatial errors originate in perception: a misjudged depth or direction can be corrected only by the scene's true geometry, which the 3D-scanned sources of spatial training corpora already provide. We propose GPD (Geometry-Privileged Distillation), which makes geometric evidence the privilege in on-policy self-distillation (OPSD). For each question, depth, semantic, and bird's-eye-view (BEV) cues are rendered as compact text and routed to the teacher alongside the reference answer; a privileged KL, applied only to incorrect trajectories, augments GRPO, and the deployed model remains RGB-only. On the 4B backbone, GPD achieves 57.1 on VSI-Bench and 37.6 average across MindCube, SPARBench, MMSI-Bench, and ViewSpatial, outperforming both GRPO and answer-privileged OPSD across spatial reasoning benchmarks. Ablations confirm the complementarity of 3D and answer privilege, the advantage of question-conditioned routing over full-context injection, and the benefit of restricting distillation to incorrect trajectories.
