---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.12737
category: cs.LG
concept: agents-tool-use
url: https://arxiv.org/abs/2604.12737
published: 2026-04-16
authors: Gustavo de Carvalho Bertoli
---

# Evaluating Differential Privacy Against Membership Inference in Federated Learning: Insights from the NIST Genomics Red Team Challenge

**arXiv:** https://arxiv.org/abs/2604.12737
**Authors:** Gustavo de Carvalho Bertoli

## Abstract

arXiv:2604.12737v2 Announce Type: replace-cross  Abstract: While Federated Learning (FL) mitigates direct data exposure, the resulting trained models remain susceptible to membership inference attacks (MIAs). This paper presents an empirical evaluation of Differential Privacy (DP) as a defense mechanism against MIAs in FL, leveraging the environment of the 2025 NIST Genomics Privacy-Preserving Federated Learning (PPFL) Red Teaming Event. To improve inference accuracy, we propose a stacking attack strategy that ensembles seven black-box estimators to train a meta-classifier on prediction probabilities and cross-entropy losses. We evaluate this methodology against target models under three privacy configurations: an unprotected convolutional neural network (CNN, $\epsilon=\infty$), a low-privacy DP model ($\epsilon=200$), and a high-privacy DP model ($\epsilon=10$). The attack outperforms all baselines in the No DP and Low Privacy settings and, critically, maintains measurable membership leakage at $\epsilon=200$ where a single-signal LiRA baseline collapses. Evaluated on an independent third-party benchmark, these results provide an empirical characterisation of how stacking-based inference degrades across calibrated DP tiers in FL.
