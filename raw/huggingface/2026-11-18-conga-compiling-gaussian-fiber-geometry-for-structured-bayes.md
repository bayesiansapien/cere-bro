---
source: farmer/huggingface
farmed: 2026-11-19T11:13:13+05:30
arxiv_id: 2611.20995
url: https://huggingface.co/papers/2611.20995
arxiv_url: https://arxiv.org/abs/2611.20995
date: 2026-11-18
---

# CONGA: Compiling Gaussian Fiber Geometry for Structured Bayesian Inference

In structured Bayesian models, a large latent block is often Gaussian conditional on a smaller set of parameters, yet generic inference methods relearn this geometry during warmup. We study how this structure can be used to construct transports for posterior inference. The conditional mean and precision determine exact affine maps, including symmetric Brenier and triangular Knothe-Rosenblatt maps, that separate a standard normal block from the remaining non-Gaussian core. KL and relative Fisher objectives then reduce to objectives on this core. We introduce CONGA, a compiler that identifies candidate Gaussian blocks and selects a temporal, spectral, or sparse implementation according to their structure and computational cost. Marginalization requires an identity established from the model; numerical evidence alone permits only a target-preserving change of variables, and a failed check leaves the model unchanged. On the Stock-Watson inflation model, CONGA improves minimum ESS per second by 12.5x for NUTS. It also restores convergence where the raw target fails: for WALNUTS on the same model, and for NUTS on a 6760-dimensional electricity load model reduced to 34 core coordinates. Experiments on graph-indexed fields show how coloring and fill affect the choice of map, including cases where retaining the original target is preferable.
  Code at https://github.com/vicgalle/conga
