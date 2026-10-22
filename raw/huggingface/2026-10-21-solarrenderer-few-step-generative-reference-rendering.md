---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.639760
arxiv_id: 2610.28630
url: https://huggingface.co/papers/2610.28630
arxiv_url: https://arxiv.org/abs/2610.28630
date: 2026-10-21
---

# SolarRenderer: Few-Step Generative Reference Rendering

Game engines and coding agents can specify the layout, motion, and camera of a scene, yet turning such coarse structure into realistic video requires a renderer that follows the structure and completes the appearance it leaves open. Existing renderers are tied to the representation of one engine, need tens of denoising steps or a costly distillation of their own, and learn from conditions that are not aligned with their target videos. We present SolarRenderer, a structure-conditioned video renderer that adapts a frozen MiniMax-H3 33B backbone with two lightweight LoRAs. Structural videos enter the native reference pathway of the backbone at the positions of the frames they describe, without a type identifier and described only in plain text, so that a single control LoRA follows arbitrary structural representations. Starting from a pretrained four-step LoRA, structure-guided distribution matching renders in four steps, 12.3 times faster than 50-step sampling, while preserving the learned control. A block-causal variant extends the same design to streaming and renders 768p video in real time. To train the model, we build a frame-aligned corpus of 136K clips from game engines, simulators, and YouTube videos. Experiments on an in-distribution test set and a generalization benchmark of 16 structural representations show that SolarRenderer achieves state-of-the-art results across both, and generalizes to 11 unseen representations, including pose skeletons, drawings, and point clouds.
