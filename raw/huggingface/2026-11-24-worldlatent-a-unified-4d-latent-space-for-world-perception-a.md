---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.925392+00:00
arxiv_id: 2611.31209
url: https://huggingface.co/papers/2611.31209
arxiv_url: https://arxiv.org/abs/2611.31209
date: 2026-11-24
---

# WorldLatent: A Unified 4D Latent Space for World Perception and Generation

Generative Pre-Training (GPT) represents a profound milestone in natural language processing, serving as the foundation for most of today's state-of-the-art large language models. By casting diverse understanding and generation problems into a shared token representation, GPT enables a single architecture and unified optimization loop to master heterogeneous tasks across massive corpora, giving rise to powerful foundation models for natural language. In contrast, 4D spatiotemporal vision lacks a common representational protocol: perception (such as depth and camera estimation) and generation are either handled by separate one-way pipelines or bolted together from unaligned single-modality spaces. In this work, we introduce WorldLatent, a framework that formulates a unified 4D latent space as a common protocol for both world perception and generation. Rather than relying on fragmented, task-specific models or stacked single-modality representations, our framework proposes a multimodal VAE architecture that compresses and fuses complex 4D visual appearance, geometry, and dynamics into a single structured latent representation. Within this formulation, perception and generation operate as complementary denoising processes over the same latent space, enabling one generative model to learn both capabilities simultaneously within a single training loop. Experiments across representative 4D benchmarks verify that our fused latent protocol achieves specialist-level zero-shot 4D perception, coherent 4D generation, and controllable editing from a single model. By demonstrating that diverse 4D tasks can be seamlessly unified under a shared representational protocol, our work provides a scalable foundation for general-purpose 4D spatial intelligence.
