---
source: farmer/huggingface
farmed: 2026-06-12T09:05:40Z
arxiv_id: 2606.12575
url: https://huggingface.co/papers/2606.12575
arxiv_url: https://arxiv.org/abs/2606.12575
date: 2026-06-12
---

# High-Fidelity Two-Step Image Generation via Teacher-Aligned End-to-End Distillation

Few-step diffusion distillation has become increasingly mature for 4-8-step generation, yet pushing further to 2 steps remains challenging. In this work, we introduce Z-Image Turbo++, a high-quality 2-step image generation model distilled from the 8-step Z-Image Turbo teacher. Our method addresses the central bottlenecks of increased task difficulty and limited model capacity in 2-step generation through three simple but effective design choices tailored to this regime. First, we propose Distribution-Aligned Adversarial Learning, which uses teacher-generated images rather than external real images as real samples for GAN training, providing a more attainable and informative adversarial target. Second, we adopt Step-Decoupled Parameterization, assigning independent model parameters to the two denoising steps to better match their distinct capacity demands. Third, we perform End-to-End Training with Iterative Regularization, allowing the first step to receive gradients from final image quality while preserving a meaningful intermediate generation through an explicit step-1 loss. Together, these designs substantially narrow the quality gap between 2-step and 8-step generation in both qualitative and quantitative evaluations, highlighting the potential of carefully tailored distillation strategies for improving the quality-efficiency trade-off in few-step generation.
