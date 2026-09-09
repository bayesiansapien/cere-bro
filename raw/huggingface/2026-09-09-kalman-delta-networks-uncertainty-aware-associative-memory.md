---
source: farmer/huggingface
farmed: 2026-09-09T05:28:24.738031+00:00
arxiv_id: 2609.07816
url: https://huggingface.co/papers/2609.07816
arxiv_url: https://arxiv.org/abs/2609.07816
date: 2026-09-09
---

# Kalman Delta Networks: Uncertainty-aware Associative Memory

Linear attention is increasingly used in frontier language models for efficient long-context inference and constant-memory decoding. Its fixed-size recurrent memory, however, requires an online decision at each token: what to write and how strongly to overwrite existing associations before knowing which information future queries will require. Delta-rule models learn this strength from the current token embedding but do not track confidence in the memory estimate, preventing each write from adapting to accumulated evidence. To represent this uncertainty explicitly, we reformulate recurrent associative memory as a linear--Gaussian state-space model, for which the Kalman filter is the optimal recursive estimator, and introduce a new family of models, Kalman Delta Networks (KDNs). Within KDNs, the transition propagates both the memory state and its uncertainty, allowing the Kalman gain to weight each residual write by accumulated evidence and observation reliability. Under this formulation, Delta-style updates emerge as a special case that substitutes a token-wise isotropic surrogate for predictive covariance and omits covariance tracking. Exact tracking, however, entails a dense, state-dependent Riccati recursion that is poorly suited to GPU-parallel linear-attention scans. To address this issue, we introduce two scan-compatible KDN approximations. Diagonal KDN projects each one-step posterior onto the diagonal Gaussian family through online mean-field variational inference, whereas Isotropic KDN uses an isotropic approximation with a single uncertainty scalar per head. Their uncertainty recurrences are Mobius maps, enabling associative scans with logarithmic parallel depth. Across controlled pretraining at 750M and 1.3B parameters, KDN variants consistently improve perplexity and mean downstream accuracy over state-of-the-art linear-attention models.
