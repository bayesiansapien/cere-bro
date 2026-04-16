---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13068
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13068
published: 2026-04-16
authors: Dip Roy, Rajiv Misra, Sanjay Kumar Singh
---

# Before the First Token: Scale-Dependent Emergence of Hallucination Signals in Autoregressive Language Models

**arXiv:** https://arxiv.org/abs/2604.13068
**Authors:** Dip Roy, Rajiv Misra, Sanjay Kumar Singh

## Abstract

arXiv:2604.13068v1 Announce Type: cross  Abstract: When do large language models decide to hallucinate? Despite serious consequences in healthcare, law, and finance, few formal answers exist. Recent work shows autoregressive models maintain internal representations distinguishing factual from fictional outputs, but when these representations peak as a function of model scale remains poorly understood.   We study the temporal dynamics of hallucination-indicative internal representations across 7 autoregressive transformers (117M--7B parameters) using three fact-based datasets (TriviaQA, Simple Facts, Biography; 552 labeled examples). We identify a scale-dependent phase transition: models below 400M parameters show chance-level probe accuracy at every generation position (AUC = 0.48--0.67), indicating no reliable factuality signal. Above $\sim$1B parameters, a qualitatively different regime emerges where peak detectability occurs at position zero -- before any tokens are generated -- then declines during generation. This pre-generation signal is statistically significant in both Pythia-1.4B (p = 0.012) and Qwen2.5-7B (p = 0.038), spanning distinct architectures and training corpora.   At the 7B scale, we observe a striking dissociation: Pythia-6.9B (base model, trained on The Pile) produces a flat temporal profile ($\Delta$ = +0.001, p = 0.989), while instruction-tuned Qwen2.5-7B shows a dominant pre-generation effect. This indicates raw scale alone is insufficient -- knowledge organization through instruction tuning or equivalent post-training is required for pre-commitment encoding. Activation steering along probe-derived directions fails to correct hallucinations across all models, confirming the signal is correlational rather than causal. Our findings provide scale-calibrated detection protocols and a concrete hypothesis on instruction tuning's role in developing knowledge circuits supporting factual generation.
