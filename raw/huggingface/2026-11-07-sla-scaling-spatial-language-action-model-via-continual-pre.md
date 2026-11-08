---
source: farmer/huggingface
farmed: 2026-11-08T17:18:50.590088+00:00
arxiv_id: 2611.08373
url: https://huggingface.co/papers/2611.08373
arxiv_url: https://arxiv.org/abs/2611.08373
date: 2026-11-07
---

# SLA: Scaling Spatial-Language-Action Model via Continual Pre-training

Reliable robotic manipulation requires both semantic understanding and precise control in three-dimensional space. However, vision-language-action (VLA) foundations largely inherit visual representations from 2D vision-language pre-training, while spatial supervision is often introduced only during task-specific adaptation. Developing spatial understanding as a transferable foundation-model capability therefore calls for learning from broader robot experience. We present SLA, a Spatial-Language-Action Model that scales implicit spatial alignment to continual pre-training and maintains it during downstream post-training. Initialized from a pretrained pi05 policy, SLA jointly optimizes action prediction and alignment between intermediate visual embeddings and spatial representations from a frozen 3D perception model. We curate and unify heterogeneous robot datasets to support spatial learning across diverse embodiments, tasks, and scenes. To accommodate this diversity, we introduce feature-dependent gates that adaptively aggregate visual embeddings from multiple VLA layers for spatial supervision. The teacher further exploits partially available depth and camera calibration alongside RGB observations, enabling effective use of heterogeneous geometric annotations. Probabilistic state dropout encourages reliance on visual cues and mitigates overfitting to demonstration trajectories. All auxiliary components are used only during training, allowing direct reuse of pretrained VLA weights and preserving the original inference architecture.
