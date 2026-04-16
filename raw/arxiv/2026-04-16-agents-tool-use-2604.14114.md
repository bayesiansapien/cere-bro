---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.14114
category: cs.LG
concept: agents-tool-use
url: https://arxiv.org/abs/2604.14114
published: 2026-04-16
authors: Xiaofan Zhou, Kyumin Lee
---

# ID and Graph View Contrastive Learning with Multi-View Attention Fusion for Sequential Recommendation

**arXiv:** https://arxiv.org/abs/2604.14114
**Authors:** Xiaofan Zhou, Kyumin Lee

## Abstract

arXiv:2604.14114v1 Announce Type: cross  Abstract: Sequential recommendation has become increasingly prominent in both academia and industry, particularly in e-commerce. The primary goal is to extract user preferences from historical interaction sequences and predict items a user is likely to engage with next. Recent advances have leveraged contrastive learning and graph neural networks to learn more expressive representations from interaction histories -- graphs capture relational structure between nodes, while ID-based representations encode item-specific information. However, few studies have explored multi-view contrastive learning between ID and graph perspectives to jointly improve user and item representations, especially in settings where only interaction data is available without auxiliary information.   To address this gap, we propose Multi-View Contrastive learning for sequential recommendation (MVCrec), a framework that integrates complementary signals from both sequential (ID-based) and graph-based views. MVCrec incorporates three contrastive objectives: within the sequential view, within the graph view, and across views. To effectively fuse the learned representations, we introduce a multi-view attention fusion module that combines global and local attention mechanisms to estimate the likelihood of a target user purchasing a target item. Comprehensive experiments on five real-world benchmark datasets demonstrate that MVCrec consistently outperforms 11 state-of-the-art baselines, achieving improvements of up to 14.44\% in NDCG@10 and 9.22\% in HitRatio@10 over the strongest baseline. Our code and datasets are available at https://github.com/sword-Lz/MMCrec.
