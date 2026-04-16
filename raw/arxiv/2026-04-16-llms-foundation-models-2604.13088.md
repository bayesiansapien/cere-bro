---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13088
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13088
published: 2026-04-16
authors: Fei Ding, Yongkang Zhang, youwei wang
---

# Design Conditions for Intra-Group Learning of Sequence-Level Rewards: Token Gradient Cancellation

**arXiv:** https://arxiv.org/abs/2604.13088
**Authors:** Fei Ding, Yongkang Zhang, youwei wang

## Abstract

arXiv:2604.13088v1 Announce Type: cross  Abstract: In sparse termination rewards, intra-group comparisons have become the dominant paradigm for fine-tuning reasoning models via reinforcement learning. However, long-term training often leads to issues like ineffective update accumulation (learning tax), solution probability drift, and entropy collapse. This paper presents a necessary condition for algorithm design from a token-level credit assignment perspective: to prevent reward-irrelevant drift, intra-group objectives must maintain gradient exchangeability across token updates, enabling gradient cancellation on weak-credit/high-frequency tokens. We show that two common mechanisms disrupting exchangeability make "non-cancellation" a structural norm. Based on this, we propose minimal intra-group transformations to restore or approximate the cancellation structure in the shared token space. Experimental results demonstrate that these transformations stabilize training, improve sample efficiency, and enhance final performance, validating the value of this design condition.
