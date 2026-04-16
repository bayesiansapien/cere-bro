---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13253
category: cs.LG
concept: agents-tool-use
url: https://arxiv.org/abs/2604.13253
published: 2026-04-16
authors: Ankit Lade, Sai Krishna J., Indar Kumar
---

# Bias-Corrected Adaptive Conformal Inference for Multi-Horizon Time Series Forecasting

**arXiv:** https://arxiv.org/abs/2604.13253
**Authors:** Ankit Lade, Sai Krishna J., Indar Kumar

## Abstract

arXiv:2604.13253v1 Announce Type: new  Abstract: Adaptive Conformal Inference (ACI) provides distribution-free prediction intervals with asymptotic coverage guarantees for time series under distribution shift. However, ACI only adapts the quantile threshold -- it cannot shift the interval center. When a base forecaster develops persistent bias after a regime change, ACI compensates by widening intervals symmetrically, producing unnecessarily conservative bands. We propose Bias-Corrected ACI (BC-ACI), which augments standard ACI with an online exponentially weighted moving average (EWM) estimate of forecast bias. BC-ACI corrects nonconformity scores before quantile computation and re-centers prediction intervals, addressing the root cause of miscalibration rather than its symptom. An adaptive dead-zone threshold suppresses corrections when estimated bias is indistinguishable from noise, ensuring no degradation on well-calibrated data. In controlled experiments across 688 runs spanning two base models, four synthetic regimes, and three real datasets, BC-ACI reduces Winkler interval scores by 13--17% under mean and compound distribution shifts (Wilcoxon p < 0.001) while maintaining equivalent performance on stationary data (ratio 1.002x). We provide finite-sample analysis showing that coverage guarantees degrade gracefully with bias estimation error.
