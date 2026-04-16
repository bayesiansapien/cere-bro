---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13938
category: cs.CV
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13938
published: 2026-04-16
authors: Tianze Xia, Zijian Ning, Zonglin Zhao
---

# ASTRA: Enhancing Multi-Subject Generation with Retrieval-Augmented Pose Guidance and Disentangled Position Embedding

**arXiv:** https://arxiv.org/abs/2604.13938
**Authors:** Tianze Xia, Zijian Ning, Zonglin Zhao

## Abstract

arXiv:2604.13938v1 Announce Type: new  Abstract: Subject-driven image generation has shown great success in creating personalized content, but its capabilities are largely confined to single subjects in common poses. Current approaches face a fundamental conflict when handling multiple subjects with complex, distinct actions: preserving individual identities while enforcing precise pose structures. This challenge often leads to identity fusion and pose distortion, as appearance and structure signals become entangled within the model's architecture. To resolve this conflict, we introduce ASTRA(Adaptive Synthesis through Targeted Retrieval Augmentation), a novel framework that architecturally disentangles subject appearance from pose structure within a unified Diffusion Transformer. ASTRA achieves this through a dual-pronged strategy. It first employs a Retrieval-Augmented Pose (RAG-Pose) pipeline to provide a clean, explicit structural prior from a curated database. Then, its core generative model learns to process these dual visual conditions using our Enhanced Universal Rotary Position Embedding (EURoPE), an asymmetric encoding mechanism that decouples identity tokens from spatial locations while binding pose tokens to the canvas. Concurrently, a Disentangled Semantic Modulation (DSM) adapter offloads the identity preservation task into the text conditioning stream. Extensive experiments demonstrate that our integrated approach achieves superior disentanglement. On our designed COCO-based complex pose benchmark, ASTRA achieves a new state-of-the-art in pose adherence, while maintaining high identity fidelity and text alignment in DreamBench.
