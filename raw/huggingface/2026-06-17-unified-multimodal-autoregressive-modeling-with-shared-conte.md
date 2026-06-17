---
source: farmer/huggingface
farmed: 2026-06-17T10:05:49Z
arxiv_id: 2606.18249
url: https://huggingface.co/papers/2606.18249
arxiv_url: https://arxiv.org/abs/2606.18249
date: 2026-06-17
---

# Unified Multimodal Autoregressive Modeling with Shared Context-Visual Tokenizer is Key to Unification

Unified Multimodal Modeling aims to integrate visual understanding and generation within a single system. However, existing approaches typically rely on two disparate visual tokenizers, which splits the representation space and hinders truly unified modeling. We propose UniAR, a unified autoregressive framework where a single discrete visual tokenizer serves as the key bridge between understanding and generation, enabling a shared context in which the model can directly interpret its own generated visual tokens without additional re-encoding. UniAR adapts a pretrained vision encoder with multi-level feature fusion and a lookup-free bitwise quantization scheme, preserving both high-level semantics and low-level details while scaling the effective visual vocabulary at minimal cost. Building on this, the unified autoregressive model adopts parallel-bitwise-prediction to jointly predict spatially grouped, multi-level visual codes, substantially reducing visual sequence length and accelerating generation. Finally, a diffusion-based visual decoder operates on discrete visual tokens to decode high-fidelity images. Through large-scale pre-training, followed by supervised fine-tuning and reinforcement learning, UniAR achieves state-of-the-art performance on image generation and image editing while remaining competitive on multimodal understanding benchmarks. The project page is available at https://sharelab-sii.github.io/uniar-web.
