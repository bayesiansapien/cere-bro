---
source: farmer/huggingface
farmed: 2026-04-20T00:00:00
arxiv_id: 2604.16299
url: https://huggingface.co/papers/2604.16299
arxiv_url: https://arxiv.org/abs/2604.16299
date: 2026-04-20
---

# Repurposing 3D Generative Model for Autoregressive Layout Generation

We introduce LaviGen, a framework that repurposes 3D generative models for 3D layout generation. Unlike previous methods that infer object layouts from textual descriptions, LaviGen operates directly in the native 3D space, formulating layout generation as an autoregressive process that explicitly models geometric relations and physical constraints among objects, producing coherent and physically plausible 3D scenes. To further enhance this process, we propose an adapted 3D diffusion model that integrates scene, object, and instruction information and employs a dual-guidance self-rollout distillation mechanism to improve efficiency and spatial accuracy. Extensive experiments on the LayoutVLM benchmark show LaviGen achieves superior 3D layout generation performance, with 19% higher physical plausibility than the state of the art and 65% faster computation. Our code is publicly available at https://github.com/fenghora/LaviGen.
