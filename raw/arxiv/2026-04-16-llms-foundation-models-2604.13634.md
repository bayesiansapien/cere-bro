---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13634
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13634
published: 2026-04-16
authors: Xuwen Zhou, Fangxin Liu, Chao Wang
---

# Calibrated Speculative Decoding: Frequency-Guided Candidate Selection for Efficient Inference

**arXiv:** https://arxiv.org/abs/2604.13634
**Authors:** Xuwen Zhou, Fangxin Liu, Chao Wang

## Abstract

arXiv:2604.13634v1 Announce Type: cross  Abstract: Speculative decoding accelerates autoregressive generation by letting draft tokens bypass full verification, but conventional frameworks suffer from frequent false rejections, particularly when draft models produce semantically correct but lexically divergent outputs. In this paper, we present Calibrated Speculative Decoding (CSD), a training-free framework that recovers valid tokens discarded by standard verification. Guided by the principle of "Frequency-Guided Candidate Selection and Probability-Guarded Acceptance," CSD incorporates two lightweight modules: Online Correction Memory, which aggregates historical rejections to propose recurring divergence patterns as rescue candidates, and Semantic Consistency Gating, which verifies candidate admissibility using probability ratios instead of exact token matching. Our evaluation across diverse large language models demonstrates that CSD outperforms existing methods, achieving a peak throughput speedup of 2.33x. CSD preserves model accuracy across all tasks while further boosting performance on complex reasoning datasets. These results establish CSD as a highly effective, lightweight solution for practical LLM deployments.
