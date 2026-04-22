---
source: farmer/huggingface
farmed: 2026-04-22T00:00:00
arxiv_id: 2604.17472
url: https://huggingface.co/papers/2604.17472
arxiv_url: https://arxiv.org/abs/2604.17472
date: 2026-04-22
---

# UniMesh: Unifying 3D Mesh Understanding and Generation

Recent advances in 3D vision have led to specialized models for either 3D understanding (e.g., shape classification, segmentation, reconstruction) or 3D generation (e.g., synthesis, completion, and editing). However, these tasks are often tackled in isolation, resulting in fragmented architectures and representations that hinder knowledge transfer and holistic scene modeling. To address these challenges, we propose UniMesh, a unified framework that jointly learns 3D generation and understanding within a single architecture. First, we introduce a novel Mesh Head that acts as a cross-model interface, bridging diffusion-based image generation with implicit shape decoders. Second, we develop Chain-of-Mesh (CoM), a geometric instantiation of iterative reasoning that enables user-driven semantic mesh editing through a closed-loop latent, prompting, and re-generation cycle. Third, we incorporate a self-reflection mechanism based on an Actor-Evaluator-Self-reflection triad to diagnose and correct failures in high-level tasks like 3D captioning. Experimental results demonstrate that UniMesh not only achieves competitive performance on standard benchmarks but also unlocks novel capabilities in iterative editing and mutual enhancement between generation and understanding.
