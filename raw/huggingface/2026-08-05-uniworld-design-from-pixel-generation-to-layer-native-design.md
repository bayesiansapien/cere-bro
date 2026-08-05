---
source: farmer/huggingface
farmed: 2026-08-05T09:04:08.705882+00:00
arxiv_id: 2608.03971
url: https://huggingface.co/papers/2608.03971
arxiv_url: https://arxiv.org/abs/2608.03971
date: 2026-08-05
---

# UniWorld-Design: From Pixel Generation to Layer-Native Design

We introduce UniWorld-Design, a framework that redefines image generation from flat pixel synthesis to structured visual composition, with semantic RGBA layers as the atomic units of generation, understanding, and editing. Our key insight is that pixels define how an image is rendered, whereas layers define how an image is created, understood, and edited. Just as human designers create and manipulate visual content through layers rather than raw pixels, UniWorld-Design equips multimodal generative models with a layer-native design space. UniWorld-Design comprises two models. The Text-to-RGBA (T2RGBA) model generates standalone RGBA assets directly from text. The Image-to-Layer (I2L) model conditions on a finished image, a global instruction and per-layer prompts, and jointly produces ordered, complete semantic RGBA layers. Its instruction interface supports top-level decomposition, recursive decomposition and targeted extraction, making layering an instruction-addressable operation for agentic editing. Because I2L learns complete semantic objects rather than visible-pixel partitions, its layers stay usable when moved or removed. On the Crello benchmark, I2L reduces per-layer RGB L1 error by 37% and achieves a 34% relative improvement in Alpha Soft IoU over Qwen-Image-Layered. Separately, T2RGBA achieves the highest CLIP Score, outperforming LayerDiffuse and OmniAlpha.
