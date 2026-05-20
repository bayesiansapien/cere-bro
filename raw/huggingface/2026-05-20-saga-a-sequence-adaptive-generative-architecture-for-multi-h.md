---
source: farmer/huggingface
farmed: 2026-05-20T09:54:57.029248+00:00
arxiv_id: 2605.19014
url: https://huggingface.co/papers/2605.19014
arxiv_url: https://arxiv.org/abs/2605.19014
date: 2026-05-20
---

# SAGA: A Sequence-Adaptive Generative Architecture for Multi-Horizon Probabilistic Forecasting with Adaptive Temporal Conformal Prediction

Microsimulation models used by ministries of finance and central banks rely on parametric processes for lifetime earnings that capture only first and second moments of the conditional distribution and miss long-range nonlinear structure. We propose SAGA, a decoder-only transformer for irregular tabular panel sequences, paired with a split conformal calibration wrapper that delivers individual-level prediction intervals with finite-sample marginal coverage guarantees. Trained on the longitudinal Swedish LISA register over 1990 to 2022, comprising 2,143,817 individuals and 61,284,903 person-years, the model forecasts annual labor earnings at horizons of one to thirty years and aggregates them by Monte Carlo into present-discounted lifetime earnings distributions. Against the canonical Guvenen, Karahan, Ozkan, and Song parametric process and tabular and recurrent baselines, SAGA reduces continuous ranked probability score by 31.9 percent at the ten-year horizon and mean absolute error by 37.7 percent at the twenty-year horizon. Conformal intervals achieve nominal coverage to within 0.4 percentage points marginally and within 2.4 percentage points on the worst-case demographic subgroup. The reconstructed lifetime earnings Gini coefficient is 0.327 against the partially observed truth of 0.341 and the GKOS estimate of 0.378. Model weights, calibration tables, and a synthetic equivalent dataset are released for replication outside the protected SCB MONA environment.
