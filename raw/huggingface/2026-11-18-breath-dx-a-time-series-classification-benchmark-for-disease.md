---
source: farmer/huggingface
farmed: 2026-11-19T11:13:13+05:30
arxiv_id: 2611.15348
url: https://huggingface.co/papers/2611.15348
arxiv_url: https://arxiv.org/abs/2611.15348
date: 2026-11-18
---

# Breath-Dx: A Time Series Classification Benchmark for Disease Screening with eNose

Electronic nose (eNose) technology offers a portable, non-invasive route for disease screening via exhaled breath analysis. However, progress in the field is hindered by the lack of systematic benchmarks that compare machine learning methods under realistic conditions, particularly sensor drift, a known but rarely quantified failure mode. Most existing studies rely on small, private datasets with inconsistent protocols, rendering results non-comparable and slowing progress. We introduce Breath-Dx, the first comprehensive benchmark of time series classification methods for breath-based disease screening. Our work leverages the Scent of Health (S-OH) dataset, the largest public clinical eNose collection to date, comprising 1,234 patients across nine diagnostic groups, each providing a 17-channel multivariate time series with explicit temporal train/test splits that account for sensor drift. We systematically evaluate 10 methods spanning four families: feature-based tabular learners, convolution-based models, graph-based, and time series architectures. All methods degrade significantly under temporal validation (0.05-0.12 AUC drop compared to random cross-validation), confirming that drift embeds a strong temporal signal. Under this realistic evaluation, the best methods achieve ROC AUC of 0.74-0.76 for some lung conditions, though others remain near chance. Recurrent architectures show the most consistent performance across diseases, while specialized time series methods achieve the highest peak results. Demographic confounders matter: breath signals provide independent diagnostic value for some conditions but add little beyond age for others. We release the S-OH dataset, all temporal splits, evaluation protocols, and code to enable reproducible research and accelerate progress in clinical breathomics.
