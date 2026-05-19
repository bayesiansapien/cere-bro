---
source: farmer/huggingface
farmed: 2026-05-19T09:55:00.432604+00:00
arxiv_id: 2605.17842
url: https://huggingface.co/papers/2605.17842
arxiv_url: https://arxiv.org/abs/2605.17842
date: 2026-05-19
---

# SNLP: Layer-Parallel Inference via Structured Newton Corrections

Autoregressive language models execute Transformer layers sequentially, creating a latency bottleneck that is not removed by conventional tensor or pipeline parallelism. We study whether this layerwise dependency can be relaxed by treating the hidden-state trace across layers as the solution of a nonlinear residual equation and solving it with parallel Newton-style updates. While this view is principled, exact Newton corrections require expensive Jacobian-vector products and naive fixed-point iterations are unstable on trained Transformers. We introduce Structured Newton Layer Parallelism (SNLP), a training and inference framework that replaces exact layer Jacobians with cheap architecture-induced surrogate dynamics. In residual Transformers, this yields Identity Newton (IDN), where the correction reduces to a prefix-sum-like update; in mHC-style architectures, HC Newton (HCN) uses the model's residual mixing matrix. We further introduce SNLP-aware regularization, which trains models to make one or a few structured Newton iterations accurately approximate the sequential forward. Experiments on nanochat-scale Transformers show that SNLP regularization improves layer-parallel compatibility and can also improve standard sequential perplexity, reducing baseline PPL by 4.7%-23.4%. At inference time, SNLP combined with layer fusion and chunkwise decomposition achieves practical wall-clock speedups: on a 0.5B Nanochat model, it reaches 2.3x speedup while still improving PPL by 6.1%. These results suggest that layer-parallel inference is not merely a numerical approximation to sequential execution, but can act as a useful solver-induced inference bias. We also characterize limitations: off-the-shelf pretrained models are less amenable to this procedure, and exact convergence recovers the sequential computation rather than providing monotonic inference-time scaling.
