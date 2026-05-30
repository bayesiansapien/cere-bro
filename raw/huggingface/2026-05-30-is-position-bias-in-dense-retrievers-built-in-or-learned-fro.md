---
source: farmer/huggingface
farmed: 2026-05-30T09:33:08Z
arxiv_id: 2605.26578
url: https://huggingface.co/papers/2605.26578
arxiv_url: https://arxiv.org/abs/2605.26578
date: 2026-05-30
---

# Is Position Bias in Dense Retrievers Built In-or Learned from Data?

Dense retrievers exhibit positional bias, favoring documents whose query-relevant information appears near the beginning and degrading retrieval performance when the information appears later. While prior work on positional bias in dense retrievers has largely focused on architectural explanations, we study how the positional distribution of evidence in training data affects retrieval-level bias direction. To test this, we construct synthetic position-targeted training sets in which query-relevant evidence appears at the beginning, middle, or end of documents, and fine-tune eight architecturally diverse pretrained models under position-skewed and balanced training distributions. At the ranking level, we observe a strong directional pattern across the examined models: skewed training distributions favor evidence at the corresponding positions. Position-balanced training reduces positional sensitivity by 57--87\% on position-aware benchmarks, with competitive mean retrieval performance in our controlled setting. Representation-level analyses further suggest that fine-tuning often reshapes learned positional preferences, although pre-existing architectural or pretraining-specific tendencies persist in some models. These results identify training-position distribution as a major controllable factor in retrieval-level position bias and suggest balanced data curation as a practical mitigation strategy.
