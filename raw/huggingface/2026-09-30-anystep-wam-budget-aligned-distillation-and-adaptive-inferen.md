---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.33748
url: https://huggingface.co/papers/2609.33748
arxiv_url: https://arxiv.org/abs/2609.33748
date: 2026-09-30
---

# AnyStep-WAM: Budget-Aligned Distillation and Adaptive Inference for World Action Models

World-action models (WAMs) couple predictive visual modeling with action generation, typically relying on iterative denoising with a fixed denoising steps. However, manipulation tasks contain actions chunks with varying sensitivity to generation errors: critical actions require precision, while less sensitive actions allow faster generation with fewer denoising steps. Here we introduce AnyStep World Action Model, a general framework for tunable-budget prediction and scene-dependent computation allocation. Our budget-aligned teacher-trajectory distillation trains interval-conditioned flow maps using explicit frozen-teacher transitions and shared low-rank adapters, supporting action generation from one-step prediction to multi-step refinement. Building on this capability, a lightweight risk-benefit scheduler predicts teacher-curvature-based difficulty and budget-specific student-teacher fidelity from a single one-step preview, selecting the smallest budget predicted to satisfy risk-adaptive fidelity requirements. We evaluate our framework on three widely used WAMs Motus, FastWAM, and LingBotVA using RoboTwin 2.0. Our method reduces average denoising steps by 60.2%, 49.8%, and 85.28%, respectively, while maintaining baseline task success rates. In particular, our AnyStep training substantially improves model performance under a one-step denoising budget, increasing task success rates by 7.07%, 12.08%, and 8.94% on Motus, FastWAM, and LingBotVA, respectively. Experiments on six real-world manipulation tasks further validate its effectiveness.
