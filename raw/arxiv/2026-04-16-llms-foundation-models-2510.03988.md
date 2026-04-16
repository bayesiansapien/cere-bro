---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2510.03988
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2510.03988
published: 2026-04-16
authors: Hoang Anh Just, Myeongseob Ko, Ruoxi Jia
---

# The Signal is in the Steps: Local Scoring for Reasoning Data Selection

**arXiv:** https://arxiv.org/abs/2510.03988
**Authors:** Hoang Anh Just, Myeongseob Ko, Ruoxi Jia

## Abstract

arXiv:2510.03988v2 Announce Type: replace-cross  Abstract: Distilling long-form reasoning from teacher models into smaller students requires selecting which candidate solutions to train on. Recent work argues that one should select responses the student model assigns highest probability, i.e., favoring solutions ``natural'' to the student. However, we find that this approach works within a single teacher but fails when scaling to long reasoning traces from multiple diverse teachers. We identify a key cause: this approach scores entire solutions, but students generalize by recombining familiar reasoning steps, not by memorizing complete solutions. Full-trajectory scoring optimizes the wrong target; it rewards global fluency while the transferable signal lies in local step transitions. We propose Local Average Log Probability (LALP), which scores each reasoning step using only a small window of preceding context, measuring whether each step is justified by its immediate premises rather than whether the full response looks natural to the student. LALP enables two practical use cases: selecting the best teacher before fine-tuning and curating training data from diverse teacher pools. Across math, coding, and science reasoning tasks, LALP consistently improves accuracy when selecting the most natural solutions by a large margin.
