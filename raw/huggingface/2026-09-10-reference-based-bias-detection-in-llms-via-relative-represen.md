---
source: farmer/huggingface
farmed: 2026-09-11T00:57:36.854415+00:00
arxiv_id: 2609.10060
url: https://huggingface.co/papers/2609.10060
arxiv_url: https://arxiv.org/abs/2609.10060
date: 2026-09-10
---

# Reference-Based Bias Detection in LLMs via Relative Representations of Hidden States

Existing bias auditing methods typically rely on model outputs, requiring costly benchmarks or judge models and potentially missing internal shifts that never appear in generated text. We propose a reference-based method that audits bias in hidden-state representations across related model variants, for example before and after fine-tuning. Because fine-tuning reshapes representation geometry, absolute hidden states are not directly comparable, so we encode each sentence by its similarities to a fixed set of anchor sentences, yielding relative representations in a shared comparison space. There we measure how target groups shift in their association with positive and negative attributes, a quantity we call the Representational Bias Shift ΔB. Across three model families and the WildGuardMix, DecodingTrust and ToxiGen benchmarks, ΔB correlates with output-level bias change in 15 of the 18 settings we test, reaching |r| = 0.84 (p < 0.001) under full fine-tuning and becoming more model-dependent under parameter-efficient adaptation. Thresholding ΔB detects checkpoints whose bias increased with ROC AUC between 0.65 and 0.99, and on WildGuardMix and DecodingTrust it separates them better than a SEAT-based baseline for all three families. ΔB is also stable under changes to the anchor set, attribute sets and target templates. Our method requires no task-specific evaluation data and audits a model in about three minutes, using 3-50times less compute than the output-level benchmarks considered here. We view it as complementary to output-based auditing rather than a replacement for it.
