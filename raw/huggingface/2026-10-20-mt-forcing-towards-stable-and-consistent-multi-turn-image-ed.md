---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.25404
url: https://huggingface.co/papers/2610.25404
arxiv_url: https://arxiv.org/abs/2610.25404
date: 2026-10-20
---

# MT Forcing: Towards Stable and Consistent Multi-Turn Image Editing with Autoregressive Diffusion

Multi-turn image editing aims to modify an image according to a sequence of instructions, enabling more effective interactive visual content creation for users. However, existing methods often exhibit noticeable drift after only a few editing turns, manifesting in two aspects: 1) unstable visual quality, with accumulating artifacts and degraded details; and 2) inconsistent image content, with unintended changes to preserved regions and prior edits. To address these challenges, we propose MT Forcing, a novel training paradigm for multi-turn image editing with unified multimodal models (UMMs) based on autoregressive diffusion. Specifically, we propose Single-Turn Distribution Matching Distillation (Single-Turn DMD), which supervises student self-rollouts with a teacher that applies cumulative edits to the source image in a single turn, providing visual-quality guidance without recursive error accumulation. Additionally, we introduce Teacher-Forcing Guidance, which supervises history-dependent transitions on reference trajectories during warmup and as a regularizer during distillation, encouraging cross-turn content consistency beyond what per-turn distribution matching alone can ensure. Extensive experiments demonstrate that our approach significantly improves the multi-turn image editing capabilities of UMMs, yielding more stable visual quality and stronger cross-turn consistency.
