---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13991
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13991
published: 2026-04-16
authors: Aleksandr Rubashevskii, Dzianis Piatrashyn, Preslav Nakov
---

# Adaptive Conformal Prediction for Improving Factuality of Generations by Large Language Models

**arXiv:** https://arxiv.org/abs/2604.13991
**Authors:** Aleksandr Rubashevskii, Dzianis Piatrashyn, Preslav Nakov

## Abstract

arXiv:2604.13991v1 Announce Type: cross  Abstract: Large language models (LLMs) are prone to generating factually incorrect outputs. Recent work has applied conformal prediction to provide uncertainty estimates and statistical guarantees for the factuality of LLM generations. However, existing approaches are typically not prompt-adaptive, limiting their ability to capture input-dependent variability. As a result, they may filter out too few items (leading to over-coverage) or too many (under-coverage) for a given task or prompt. We propose an adaptive conformal prediction approach that extends conformal score transformation methods to LLMs, with applications to long-form generation and multiple-choice question answering. This enables prompt-dependent calibration, retaining marginal coverage guarantees while improving conditional coverage. In addition, the approach naturally supports selective prediction, allowing unreliable claims or answer choices to be filtered out in downstream applications. We evaluate our approach on multiple white-box models across diverse domains and show that it significantly outperforms existing baselines in terms of conditional coverage.
