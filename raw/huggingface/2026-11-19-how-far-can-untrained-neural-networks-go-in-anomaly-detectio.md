---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.144516+00:00
arxiv_id: 2611.08136
url: https://huggingface.co/papers/2611.08136
arxiv_url: https://arxiv.org/abs/2611.08136
date: 2026-11-19
---

# How Far Can Untrained Neural Networks Go in Anomaly Detection? From Tables to Pixels

Anomaly detection (AD) is often framed as a representation-learning problem, where strong performance is expected to require learned features or AD-specific optimization. However, this view can overlook the intrinsic separability of anomalies from normal references, even in the absence of learned representations. We therefore investigate how far untrained neural networks can go in anomaly detection. To this end, we propose PRISM, a framework combining fixed random nonlinear features with normal-reference Mahalanobis scoring for tabular detection and dense visual localization. Across 47 tabular datasets in ADBench, PRISM-T achieves the highest mean AUROC (86.4%) and the second-highest mean AUPRC (65.9%) among the compared methods. On MVTec AD and VisA, covering 27 visual categories, PRISM-V achieves mean image-level and pixel-level AUROCs of 90.4% and 96.4%, respectively. Notably, both models achieve these results without neural weight optimization or pretrained representations. A theoretical analysis further characterizes how nonlinear transformations affect the mean and covariance contributions to the Mahalanobis score gap, while empirical analyses examine the resulting score separability. These findings establish PRISM as both a competitive anomaly detector and a prior-to-learning baseline for assessing the added value of learned representations in anomaly detection.
