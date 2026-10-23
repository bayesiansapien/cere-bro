---
source: farmer/huggingface
farmed: 2026-10-23T08:19:34.188330+00:00
arxiv_id: 2610.21114
url: https://huggingface.co/papers/2610.21114
arxiv_url: https://arxiv.org/abs/2610.21114
date: 2026-10-22
---

# Spectral-Spatial Interpretation

Post-hoc image explanations usually show where a model looks using spatial heatmaps or indicate which channels matter using global channel scores. These separate views are limiting for multispectral data because channel relevance is often spatially localized and physically meaningful. We introduce Spectral-Spatial Interpretation (SSI), a full-grid attribution method over position-channel players (g,c). For each spatial position, SSI fixes the observed surrounding context, defines a conditional game over the channels at that position, and applies the Shapley value to this local game. The result is a full spectral-spatial attribution matrix rather than a single heatmap or a global channel ranking. SSI has a clear local interpretation. It satisfies Shapley fairness within each position, and aggregating its channel attributions exactly recovers the position-level contextual contrast obtained by replacing that position with the baseline. SSI also differs from context-averaged Owen-style hierarchical accounting, which uses the same position-channel grouping but averages over external spatial coalitions. On HLS Burn Scar, SSI outperforms an MC-Owen estimator across retained attribution metrics while using only about 6% of its evaluation budget. Across CUB-200, EuroSAT, and HLS Burn Scar under both per-channel mean and zero baselines, SSI achieves the best joint deletion and insertion AUC over dense, flat, and rank-1 baselines, yields the strongest spectral hit rates and channel deletion, and leads spatial localization on both annotated datasets. Code is available at https://github.com/AtheavenMa/Spectral-Spatial-Interpretation.
