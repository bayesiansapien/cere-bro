---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2601.03523
category: cs.AI
concept: inference-efficiency
url: https://arxiv.org/abs/2601.03523
published: 2026-04-16
authors: Kengo Nakamura, Masaaki Nishino, Norihito Yasuda
---

# Variance Computation for Weighted Model Counting with Knowledge Compilation Approach

**arXiv:** https://arxiv.org/abs/2601.03523
**Authors:** Kengo Nakamura, Masaaki Nishino, Norihito Yasuda

## Abstract

arXiv:2601.03523v2 Announce Type: replace  Abstract: One of the most important queries in knowledge compilation is weighted model counting (WMC), which has been applied to probabilistic inference on various models, such as Bayesian networks. In practical situations on inference tasks, the model's parameters have uncertainty because they are often learned from data, and thus we want to compute the degree of uncertainty in the inference outcome. One possible approach is to regard the inference outcome as a random variable by introducing distributions for the parameters and evaluate the variance of the outcome. Unfortunately, the tractability of computing such a variance is hardly known. Motivated by this, we consider the problem of computing the variance of WMC and investigate this problem's tractability. First, we derive a polynomial time algorithm to evaluate the WMC variance when the input is given as a structured d-DNNF. Second, we prove the hardness of this problem for structured DNNFs, d-DNNFs, and FBDDs, which is intriguing because the latter two allow polynomial time WMC algorithms. Finally, we show an application that measures the uncertainty in the inference of Bayesian networks. We empirically show that our algorithm can evaluate the variance of the marginal probability on real-world Bayesian networks and analyze the impact of the variances of parameters on the variance of the marginal.
