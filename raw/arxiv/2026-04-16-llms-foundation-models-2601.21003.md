---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2601.21003
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2601.21003
published: 2026-04-16
authors: Moule Lin, Shuhao Guan, Andrea Patane
---

# Bayesian-LoRA: Probabilistic Low-Rank Adaptation of Large Language Models

**arXiv:** https://arxiv.org/abs/2601.21003
**Authors:** Moule Lin, Shuhao Guan, Andrea Patane

## Abstract

arXiv:2601.21003v2 Announce Type: replace  Abstract: Large Language Models usually put more emphasis on accuracy and therefore, will guess even when not certain about the prediction, which is especially severe when fine-tuned on small datasets due to the inherent tendency toward miscalibration. In this work, we introduce Bayesian-LoRA, which reformulates the deterministic LoRA update as a probabilistic low-rank representation inspired by Sparse Gaussian Processes. We identify a structural isomorphism between LoRA's factorization and Kronecker-factored SGP posteriors, and show that LoRA emerges as a limiting case when posterior uncertainty collapses. We conduct extensive experiments on various LLM architectures across commonsense reasoning benchmarks. With only approximately 0.42M additional parameters and ${\approx}1.2{\times}$ training cost relative to standard LoRA, Bayesian-LoRA significantly improves calibration across models up to 30B, achieving up to 84% ECE reduction and 76% NLL reduction while maintaining competitive accuracy for both in-distribution and out-of-distribution (OoD) evaluations.
