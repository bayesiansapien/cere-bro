---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13123
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13123
published: 2026-04-16
authors: Truong Xuan Khanh, Truong Quynh Hoa, Luu Duc Trung
---

# Spectral Entropy Collapse as an Empirical Signature of Delayed Generalisation in Grokking

**arXiv:** https://arxiv.org/abs/2604.13123
**Authors:** Truong Xuan Khanh, Truong Quynh Hoa, Luu Duc Trung

## Abstract

arXiv:2604.13123v1 Announce Type: cross  Abstract: Grokking -- delayed generalisation long after memorisation -- lacks a predictive mechanistic explanation. We identify the normalised spectral entropy $\tilde{H}(t)$ of the representation covariance as a scalar order parameter for this transition, validated on 1-layer Transformers on group-theoretic tasks. Five contributions: (i) Grokking follows a two-phase pattern: norm expansion then entropy collapse. (ii) $\tilde{H}$ crosses a stable threshold $\tilde{H}^* \approx 0.61$ before generalisation in 100% of runs (mean lead: 1,020 steps). (iii) A causal intervention preventing collapse delays grokking by +5,020 steps ($p=0.044$); a norm-matched control ($n=30$, $p=5\times10^{-5}$) confirms entropy -- not norm -- drives the transition. (iv) A power-law $\Delta T = C_1(\tilde{H}-\tilde{H}^*)^\gamma+C_2$ ($R^2=0.543$) predicts grokking onset with 4.1% error. (v) The mechanism holds across abelian ($\mathbb{Z}/97\mathbb{Z}$) and non-abelian ($S_5$) groups. Crucially, MLPs show entropy collapse without grokking, proving collapse is necessary but not sufficient -- architecture matters. Code: https://anonymous.4open.science/r/grokking-entropy
