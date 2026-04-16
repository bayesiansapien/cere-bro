---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13279
category: cs.AI
concept: inference-efficiency
url: https://arxiv.org/abs/2604.13279
published: 2026-04-16
authors: Mohammad Saleh, Azadeh Tabatabaei
---

# Explainable Fall Detection for Elderly Care via Temporally Stable SHAP in Skeleton-Based Human Activity Recognition

**arXiv:** https://arxiv.org/abs/2604.13279
**Authors:** Mohammad Saleh, Azadeh Tabatabaei

## Abstract

arXiv:2604.13279v1 Announce Type: cross  Abstract: Fall detection in elderly care requires not only accurate classification but also reliable explanations that clinicians can trust. However, existing post-hoc explainability methods, when applied frame-by-frame to sequential data, produce temporally unstable attribution maps that clinicians cannot reliably act upon. To address this issue, we propose a lightweight and explainable framework for skeleton-based fall detection that combines an efficient LSTM model with T-SHAP, a temporally aware post-hoc aggregation strategy that stabilizes SHAP-based feature attributions over contiguous time windows. Unlike standard SHAP, which treats each frame independently, T-SHAP applies a linear smoothing operator to the attribution sequence, reducing high-frequency variance while preserving the theoretical guarantees of Shapley values, including local accuracy and consistency. Experiments on the NTU RGB+D Dataset demonstrate that the proposed framework achieves 94.3% classification accuracy with an end-to-end inference latency below 25 milliseconds, satisfying real-time constraints on mid-range hardware and indicating strong potential for deployment in clinical monitoring scenarios. Quantitative evaluation using perturbation-based faithfulness metrics shows that T-SHAP improves explanation reliability compared to standard SHAP (AUP: 0.89 vs. 0.91) and Grad-CAM (0.82), with consistent improvements observed across five-fold cross-validation, indicating enhanced explanation reliability. The resulting attributions consistently highlight biomechanically relevant motion patterns, including lower-limb instability and changes in spinal alignment, aligning with established clinical observations of fall dynamics and supporting their use as transparent decision aids in long-term care environments
