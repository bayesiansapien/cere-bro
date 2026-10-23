---
source: farmer/huggingface
farmed: 2026-10-23T08:19:34.197015+00:00
arxiv_id: 2610.22659
url: https://huggingface.co/papers/2610.22659
arxiv_url: https://arxiv.org/abs/2610.22659
date: 2026-10-22
---

# Exploring The Empirical Privacy Landscape of Synthetic Data

Methods for training language models on sensitive data differ in how they balance capability gains against the risk of leaking private information. In this paper, we present a controlled comparison of data-level and training-level interventions for navigating the capability-privacy tradeoff on synthetic medical records with canaries to probe for leakage. Direct finetuning performs best on capability metrics but leads to the most privacy leakage, while DP-SGD reduces leakage at substantial cost to capabilities. Generating synthetic data from these records offers a more favorable balance, particularly when guided by a uniqueness-aware instruction to replace private details. Relative to naive paraphrasing, privacy-aware rewriting improves privacy protection across a variety of different rewriting models. We also find that more capable rewriting models generally reduce the risks of downstream privacy leakage, although held-out fit does not improve monotonically and increased test-time compute yields inconsistent gains. Overall, these results highlight privacy-aware rewriting as a promising direction for achieving a more favorable trade-off between capabilities and empirical privacy compared to other training-level methods, and our evaluation framework supports comparisons of future models and methods.
