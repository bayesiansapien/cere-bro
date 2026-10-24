---
source: farmer/huggingface
farmed: 2026-10-24T12:49:20.880472+00:00
arxiv_id: 2610.27598
url: https://huggingface.co/papers/2610.27598
arxiv_url: https://arxiv.org/abs/2610.27598
date: 2026-10-23
---

# Meta Expert: Cross-Layer Expert Sharing for Storage- and Retrieval-Efficient MoE

As model parameters scale up, sparsely activated Mixture-of-Experts (MoE) approaches have become essential for model scaling. However, mainstream models currently adopt hierarchical architectures, where experts in different layers, although topologically independent, exhibit substantial similarity and redundancy in their stored content. Compared to the hierarchically arranged Local Expert in existing mainstream models, we hypothesize that inter-layer shared Meta Expert hold greater potential. To this end, we conduct a multi-dimensional empirical comparison between Local and Meta Experts, and find that models incorporating Meta Experts exhibit lower parameter redundancy, together with lower cross-entropy loss and higher downstream task accuracy. With the activated quantity and the expert granularity held fixed, our model matches the performance of Vanilla MoE using only 70--80\% of the experts, substantially improving the model's scaling potential. Beyond removing inter-layer redundancy among experts and improving information storage efficiency, our theoretical analysis further shows that, compared with Local Experts, Meta Experts provide hidden states with more flexible residual pathways, thereby improving information retrieval efficiency.
