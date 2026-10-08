---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.05949
url: https://huggingface.co/papers/2610.05949
arxiv_url: https://arxiv.org/abs/2610.05949
date: 2026-10-07
---

# Technical Report on the Turba Fertilizer Machine Learning Stack in Morocco

Site-specific fertilizer recommendation systems adapt nutrient advice to location, soil properties, crop type, and production targets, but scientific reuse is constrained when recommendation functions remain accessible mainly through interactive interfaces, outputs are not versioned, and trained approximations cannot be independently loaded or benchmarked. This technical report presents the Turba fertilizer machine learning stack, a three-layer open-source implementation for reproducible site-specific fertilizer recommendation in Morocco. turba-client provides programmatic access to publicly accessible site profiles, crop-specific target-yield spaces, and N, P_2O_5, and K_2O recommendation workflows; turba-data distributes analysis-ready snapshots; and turba-models packages crop-specific machine learning surrogates of recommendation outputs. The architecture links upstream retrieval, versioned analytical snapshots, reproducible cross-model benchmarking, and loadable offline surrogates while preserving the distinction between recommendation-system outputs, observed agricultural data, and model-generated predictions. The first dataset was constructed from 44,096 unique ESA WorldCereal locations. Scenario expansion across supported cereal workflows generated 132,017 crop-location recommendation requests under a medium target-yield setting. The resulting 22-variable dataset spans 10 regions, 66 provinces, and 1,149 communes. Nine regression families were evaluated under a fixed deterministic 80/20 protocol, and the current release packages five best-performing crop-specific models. The machine learning task is recommendation-function emulation rather than prediction of observed crop response. The stack provides a reproducible basis for spatial and temporal validation, uncertainty estimation, field-trial comparison, and future integration with additional data.
