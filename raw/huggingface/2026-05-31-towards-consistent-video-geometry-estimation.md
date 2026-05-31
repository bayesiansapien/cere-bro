---
source: farmer/huggingface
farmed: 2026-05-31T09:25:04Z
arxiv_id: 2605.30060
url: https://huggingface.co/papers/2605.30060
arxiv_url: https://arxiv.org/abs/2605.30060
date: 2026-05-31
---

# Towards Consistent Video Geometry Estimation

This work presents ViGeo, a feed-forward foundation model for recovering spatially dense and temporally consistent geometry from video sequences. Built upon a plain transformer architecture without task-specific architectural modifications, ViGeo supports streaming, full-sequence, and long-video inference within a unified model. The key design is dynamic chunking attention, which exposes the model to both bidirectional and causal temporal contexts during training and allows it to adapt its attention pattern at test time without retraining. To improve supervision quality, we further introduce a completion-based data refinement framework. This framework trains a video depth completion teacher that conditions on sparse and noisy annotations and exploits video/multi-view context to produce dense, temporally coherent, and geometrically reliable training targets. Beyond depth and point maps, ViGeo also predicts surface normals within the same framework. Trained solely on public datasets, ViGeo achieves state-of-the-art performance across online, offline, and long-video depth estimation, surface normal estimation, and video point map estimation.
