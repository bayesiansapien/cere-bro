---
source: farmer/huggingface
farmed: 2026-06-15T06:21:28Z
arxiv_id: 2606.13872
url: https://huggingface.co/papers/2606.13872
arxiv_url: https://arxiv.org/abs/2606.13872
date: 2026-06-15
---

# Avatar V: Scaling Video-Reference Avatar Video Generation

Generating avatar videos that are not merely visually similar to a target individual but behaviorally recognizable, faithfully reproducing their talking rhythm, gestural tendencies, and expression dynamics, remains an open challenge. Existing methods predominantly condition on single static images, which provide insufficient identity information and cannot capture dynamic motion traits, while standard pixel-level objectives underserve the perceptually critical facial regions that determine avatar fidelity. We present Avatar V, a production-scale framework that addresses these limitations through video-reference-conditioned identity modeling. Rather than compressing identity into fixed-size embeddings, the model conditions directly on the full token sequence of a reference video, learning to reproduce both static identity attributes (facial geometry, skin texture) and dynamic behavioral patterns (talking rhythm, micro-expressions) through attention over the reference context. We introduce Sparse Reference Attention, an asymmetric mechanism achieving linear-complexity conditioning on arbitrarily long references; a motion representation stream enabling closed-loop talking style transfer; and an identity-aware super-resolution refiner inheriting the full reference conditioning. These are supported by a data engine curating 100M+ training clips from 50M raw videos, and a five-stage training pipeline with flow matching pre-training, personality fine-tuning, two-phase distillation (>10x acceleration), and RLHF alignment, deployed across thousands of GPUs. Avatar V generates 1080p videos of unlimited duration, achieving state-of-the-art identity preservation, lip synchronization, and generation quality on our cross-scene benchmark, consistently outperforming leading systems including Seedance 2.0, Kling O3 Pro, Veo 3.1, and OmniHuman 1.5 in both automated metrics and human evaluation.
