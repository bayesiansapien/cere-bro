---
source: farmer/huggingface
farmed: 2026-05-28T03:40:35Z
arxiv_id: 2605.28763
url: https://huggingface.co/papers/2605.28763
arxiv_url: https://arxiv.org/abs/2605.28763
date: 2026-05-28
---

# CubePart: An Open-Vocabulary Part-Controllable 3D Generator

Interactive 3D assets used in games and simulation are typically decomposed into specific semantic parts to support animation, physics, and scripted behaviors, yet most generative 3D models produce either monolithic meshes or arbitrary part decompositions that cannot be aligned with application-specific requirements. We present CubePart, a generative framework for open-vocabulary, part-controllable 3D mesh generation that exposes part structure as an explicit inference-time control signal. Given a global text prompt and a user-defined parts schema expressed as an open-ended list of part names, our method generates a set of meshes - one per schema element - that assemble into a coherent object while respecting the specified semantic structure. To enable this capability, we introduce a scalable data pipeline to construct a large open-vocabulary, part-labeled 3D dataset, along with a two-stage generative architecture that separates global shape synthesis from part-level decoding. We demonstrate that the resulting assets can be directly integrated into game engines and driven by animation and behavior scripts without manual post-processing. Project Page: https://cubepart.github.io/
