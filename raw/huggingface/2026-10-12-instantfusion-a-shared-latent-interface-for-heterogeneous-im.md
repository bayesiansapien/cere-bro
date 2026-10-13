---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.218742+05:30
arxiv_id: 2610.13944
url: https://huggingface.co/papers/2610.13944
arxiv_url: https://arxiv.org/abs/2610.13944
date: 2026-10-12
---

# InstantFusion: A Shared Latent Interface for Heterogeneous Image Generators

Diffusion/flow models have emerged as the de facto paradigms for image generation, giving rise to a diverse family of modern generators with increasingly heterogeneous architectures and representations. Despite their remarkable generation capabilities, the cross-model alignment of latent representations and the consistency of their underlying denoising dynamics remain underexplored. In this work, we uncover an intriguing cross-model compatibility: independently trained generators exhibit similar latent spatial organization, while directly handing off intermediate states between unaligned models can still preserve coarse visual content. Motivated by these observations, we propose InstantFusion, a lightweight shared latent interface that connects the denoising trajectories of heterogeneous image generators. Specifically, to enable flexible cross-model state translation, model-specific Latent AutoEncoders (LAEs) are introduced to project intermediate states from different generators into a shared latent space and decode them into the latent space of a target generator. This shared space is constrained by two complementary objectives: aligning intermediate states derived from the same image at matched noise levels and synchronizing their corresponding local denoising velocities. Once trained, InstantFusion allows denoising to seamlessly transition across frozen generators without requiring a dedicated mapping for every model pair. The versatility of InstantFusion is demonstrated across acceleration, multi-preference composition, cross-architecture on-policy distillation, and cross-model composition, achieving competitive performance across these diverse settings.
