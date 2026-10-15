---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.506628+00:00
arxiv_id: 2610.18472
url: https://huggingface.co/papers/2610.18472
arxiv_url: https://arxiv.org/abs/2610.18472
date: 2026-10-14
---

# Simplifying and Improving On-Policy Distillation for Few-Step Diffusion

Few-step distillation reduces the sampling cost of diffusion and flow models, but existing approaches often require auxiliary score models or specialized architectures. We show that simple on-policy velocity regression already provides a strong foundation for 4-NFE generation. To represent teacher velocity variation within each coarse transition, we introduce Pivot, a training-only residual proxy that separates local corrections from the student's interval-mean prediction. We further repel the student from weaker teacher predictions, providing a lightweight mechanism for avoiding undesirable modes. The resulting framework, Simplified Matching Distillation (SMD), remains entirely regression-based, requires neither online score estimation nor adversarial training, and leaves the deployed generator unchanged. We evaluate SMD on image generation and editing, 3D generation, video synthesis, and joint audio--video generation, scaling to 33 billion parameters. At 4-NFE, SMD outperforms strong few-step baselines and surpasses multi-step teachers on several benchmarks. It also supports cross-model, multi-teacher, and causal-video distillation.
