---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2602.23636
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2602.23636
published: 2026-04-16
authors: Zhihao Ding, Jinming Li, Ze Lu
---

# FlexGuard: Continuous Risk Scoring for Strictness-Adaptive LLM Content Moderation

**arXiv:** https://arxiv.org/abs/2602.23636
**Authors:** Zhihao Ding, Jinming Li, Ze Lu

## Abstract

arXiv:2602.23636v3 Announce Type: replace-cross  Abstract: Ensuring the safety of LLM-generated content is essential for real-world deployment. Most existing guardrail models formulate moderation as a fixed binary classification task, implicitly assuming a fixed definition of harmfulness. In practice, enforcement strictness - how conservatively harmfulness is defined and enforced - varies across platforms and evolves over time, making binary moderators brittle under shifting requirements. We first introduce FlexBench, a strictness-adaptive LLM moderation benchmark that enables controlled evaluation under multiple strictness regimes. Experiments on FlexBench reveal substantial cross-strictness inconsistency in existing moderators: models that perform well under one regime can degrade substantially under others, limiting their practical usability. To address this, we propose FlexGuard, an LLM-based moderator that outputs a calibrated continuous risk score reflecting risk severity and supports strictness-specific decisions via thresholding. We train FlexGuard via risk-alignment optimization to improve score-severity consistency and provide practical threshold selection strategies to adapt to target strictness at deployment. Experiments on FlexBench and public benchmarks demonstrate that FlexGuard achieves higher moderation accuracy and substantially improved robustness under varying strictness. We release the source code and data to support reproducibility.
