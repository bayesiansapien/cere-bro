---
source: farmer/huggingface
farmed: 2026-11-17T08:29:02.003683+00:00
arxiv_id: 2611.17321
url: https://huggingface.co/papers/2611.17321
arxiv_url: https://arxiv.org/abs/2611.17321
date: 2026-11-16
---

# BrickFlow: Connectivity-Guided Brick Reconstruction

Given a set of LEGO parts and an image of an assembled object, our task is to infer the pose of each part to assemble the object. In contrast with traditional 3D reconstruction, doing so requires satisfying discrete physical constraints, which provide structure but render the problem combinatorial and highly sensitive to small pose errors. To learn a prior over how parts fit together, we train a set-conditioned SE(3) flow model on procedurally generated assemblies. We then finetune this model to inject image conditioning, using 1% as much data. However, while the learned flow captures global structure, it does not enforce connectivity. To address this, we introduce an analytic connectivity-field guidance to pull predictions toward connected assemblies at test time. Through this, we demonstrate improved build quality with model size, pretraining, and guidance. We make our models and data available for research purposes at https://kulits.github.io/BrickFlow/
