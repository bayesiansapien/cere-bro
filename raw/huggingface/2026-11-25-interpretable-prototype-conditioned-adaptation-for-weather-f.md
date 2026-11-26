---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.25848
url: https://huggingface.co/papers/2611.25848
arxiv_url: https://arxiv.org/abs/2611.25848
date: 2026-11-25
---

# Interpretable Prototype-Conditioned Adaptation for Weather Forecasting

Data-driven weather forecasting requires distinguishing local states and their temporal evolution. However, learned patterns remain implicit in neural forecasters, making their influence difficult to interpret. Failing to distinguish local evolution can lead to similar forecasts for locations that develop differently, increasing prediction error. This motivates explicit references for distinguishing and interpreting local patterns. Prototypes provide explicit pattern references, but sample- or task-level conditioning leaves open how to adapt to distinct locations and variable groups. To deal with this problem, we design ProtoCast, which uses group-specific prototype banks to adapt local features while accounting for cross-variable dependencies. Specifically, (1) we combine each group's historical features and temporal change with forecast context from cross-variable attention for evolution-aware prototype matching. (2) Sparse mixtures of prototype-specific low-rank operators tailor corrections to each group and location. A gated attention block then exchanges the corrected features across groups before prediction. Each group's correction decomposes into explicit prototype contributions before this fusion. (3) We jointly train the forecasting network and operators from scratch and refit each group's prototypes before every training epoch. Slot tracking preserves prototype-operator associations, making each prototype's contribution to local corrections more interpretable. Experiments on GlobalForecast and TyphoonTracking show improved forecasting accuracy, while prototype deletion links local feature contributions to changes in prediction error. This work advances the development of more accurate and interpretable data-driven weather forecasting models. Project page: https://zhixuanli.github.io/projects/li2026protocast
