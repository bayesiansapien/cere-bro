---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.995552+05:30
arxiv_id: 2610.37585
url: https://huggingface.co/papers/2610.37585
arxiv_url: https://arxiv.org/abs/2610.37585
date: 2026-10-28
---

# Timestral

We introduce Timestral, a family of four time series foundation models for probabilistic forecasting, with 5M, 28M, 123M, and 209M parameters. Timestral sets a new state of the art on GIFT-Eval, TIME, and fev-bench, where Timestral-209M and Timestral-123M take the top two places on every metric. We achieve this with three ingredients: Decoupled Horizon Forecasting (DHF), which separates prediction tokens from the causally encoded context, so that longer horizons are trained without masking context and each observed value is both a forecast target and context for later forecasts; a covariate framework that natively supports known-future covariates within a causal architecture; and a two-stage pipeline that pretrains exclusively on a diverse, large-scale synthetic corpus before post-training on a mix of real and synthetic data with extended context. This report describes the model design and its benchmark results. Weights for all four models are available on Hugging Face and inference code on GitHub.
