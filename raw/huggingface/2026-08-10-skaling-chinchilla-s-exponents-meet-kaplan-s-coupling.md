---
source: farmer/huggingface
farmed: 2026-08-10T09:04:01.722687
arxiv_id: 2608.07222
url: https://huggingface.co/papers/2608.07222
arxiv_url: https://arxiv.org/abs/2608.07222
date: 2026-08-10
---

# Skaling: Chinchilla's Exponents Meet Kaplan's Coupling

Neural scaling laws are foundational for language model development, yet standard formulations systematically under- and overestimate loss at data-scarce and overtraining extremes. This failure originates in the underlying assumption that model size and training data impact the loss independently. To address this, we introduce the Skaling law, a generalized functional form that couples model capacity and data through a single interaction exponent. This simple extension reduces the Mean Absolute Percentage Error (MAPE) by 1.5-3x across both interpolation and extrapolation regimes. When paired with a sparse grid strategy restricted to low-compute regimes, the Skaling law achieves accurate full-grid extrapolation using approximately 10x less compute than uniform sweeps. By enabling reliable performance prediction from small-scale experiments, the Skaling law provides a more robust and resource-efficient framework for allocating compute budgets in next-generation model training.
