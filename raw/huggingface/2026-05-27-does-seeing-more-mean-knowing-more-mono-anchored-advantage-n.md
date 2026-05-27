---
source: farmer/huggingface
farmed: 2026-05-27T07:52:03Z
arxiv_id: 2605.25437
url: https://huggingface.co/papers/2605.25437
arxiv_url: https://arxiv.org/abs/2605.25437
date: 2026-05-27
upvotes: 9
---

# Does Seeing More Mean Knowing More? Mono-Anchored Advantage Normalization for Multi-Source Visual Reasoning

Visual reasoning through reinforcement learning with verifiable rewards (RLVR) has achieved remarkable progress. However, when dealing with multi-source inputs, existing approaches tend to treat them as a mere accumulation of information, lacking explicit mechanisms to distinguish whether integrating additional sources yields information gain or introduces interference. Therefore, they struggle to effectively model dynamic interaction when integrating multiple sources, particularly when they differ significantly in physical properties and semantics, e.g., infrared and depth, leading to inferior performance to mono-source reasoning when a certain source holds the dominant signal. To address this issue, we propose MARS, a novel mono-anchored multi-source reasoning framework that models each visual modality as an independent information source. Specifically, by treating mono-source rewards as dynamic anchors, our method explicitly incorporates the information gain introduced by multi-source fusion into advantage normalization and adaptively emphasizes mutual promotion between sources while suppressing potential noise or conflicts during RLVR. From theoretical analysis, our method effectively quantifies information gain introduced by multi-source integration in gradient estimation, enabling consistent modality regulation. Empirical results also show impressive 3.2% and 4.9% performance gains on GRPO and DAPO across diverse datasets, confirming effectiveness of our method.
