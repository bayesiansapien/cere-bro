---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13410
category: cs.LG
concept: agents-tool-use
url: https://arxiv.org/abs/2604.13410
published: 2026-04-16
authors: Seok-Jin Kim, Kaizheng Wang
---

# Estimating Continuous Treatment Effects with Two-Stage Kernel Ridge Regression

**arXiv:** https://arxiv.org/abs/2604.13410
**Authors:** Seok-Jin Kim, Kaizheng Wang

## Abstract

arXiv:2604.13410v1 Announce Type: cross  Abstract: We study the problem of estimating the effect function for a continuous treatment, which maps each treatment value to a population-averaged outcome. A central challenge in this setting is confounding: treatment assignment often depends on covariates, creating selection bias that makes direct regression of the response on treatment unreliable. To address this issue, we propose a two-stage kernel ridge regression method. In the first stage, we learn a model for the response as a function of both treatment and covariates; in the second stage, we use this model to construct pseudo-outcomes that correct for distribution shift, and then fit a second model to estimate the treatment effect. Although the response varies with both treatment and covariates, the induced effect function obtained by averaging over covariates is typically much simpler, and our estimator adapts to this structure. Furthermore, we introduce a fully data-driven model selection procedure that achieves provable adaptivity to both the unknown degree of overlap and the regularity (eigenvalue decay) of the underlying kernel.
