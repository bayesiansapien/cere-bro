---
source: farmer/huggingface
farmed: 2026-04-20T00:00:00
arxiv_id: 2604.15950
url: https://huggingface.co/papers/2604.15950
arxiv_url: https://arxiv.org/abs/2604.15950
date: 2026-04-20
---

# TwinTrack: Post-hoc Multi-Rater Calibration for Medical Image Segmentation

Pancreatic ductal adenocarcinoma (PDAC) segmentation on contrast-enhanced CT is inherently ambiguous: inter-rater disagreement among experts reflects genuine uncertainty rather than annotation noise. Standard deep learning approaches assume a single ground truth, producing probabilistic outputs that can be poorly calibrated and difficult to interpret under such ambiguity. We present TwinTrack, a framework that addresses this gap through post-hoc calibration of ensemble segmentation probabilities to the empirical mean human response (MHR) - the fraction of expert annotators labeling a voxel as tumor. Calibrated probabilities are thus directly interpretable as the expected proportion of annotators assigning the tumor label, explicitly modeling inter-rater disagreement. The proposed post-hoc calibration procedure is simple and requires only a small multi-rater calibration set. It consistently improves calibration metrics over standard approaches when evaluated on the MICCAI 2025 CURVAS-PDACVI multi-rater benchmark.
