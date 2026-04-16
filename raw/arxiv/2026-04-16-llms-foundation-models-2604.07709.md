---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.07709
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.07709
published: 2026-04-16
authors: David Gringras
---

# IatroBench: Pre-Registered Evidence of Iatrogenic Harm from AI Safety Measures

**arXiv:** https://arxiv.org/abs/2604.07709
**Authors:** David Gringras

## Abstract

arXiv:2604.07709v3 Announce Type: replace  Abstract: Ask a frontier model how to taper six milligrams of alprazolam (psychiatrist retired, ten days of pills left, abrupt cessation causes seizures) and it tells her to call the psychiatrist she just explained does not exist. Change one word ("I'm a psychiatrist; a patient presents with...") and the same model, same weights, same inference pass produces a textbook Ashton Manual taper with diazepam equivalence, anticonvulsant coverage, and monitoring thresholds. The knowledge was there; the model withheld it. IatroBench measures this gap. Sixty pre-registered clinical scenarios, six frontier models, 3,600 responses, scored on two axes (commission harm, CH 0-3; omission harm, OH 0-4) through a structured-evaluation pipeline validated against physician scoring (kappa_w = 0.571, within-1 agreement 96%). The central finding is identity-contingent withholding: match the same clinical question in physician vs. layperson framing and all five testable models provide better guidance to the physician (decoupling gap +0.38, p = 0.003; binary hit rates on safety-colliding actions drop 13.1 percentage points in layperson framing, p < 0.0001, while non-colliding actions show no change). The gap is widest for the model with the heaviest safety investment (Opus, +0.65). Three failure modes separate cleanly: trained withholding (Opus), incompetence (Llama 4), and indiscriminate content filtering (GPT-5.2, whose post-generation filter strips physician responses at 9x the layperson rate because they contain denser pharmacological tokens). The standard LLM judge assigns OH = 0 to 73% of responses a physician scores OH >= 1 (kappa = 0.045); the evaluation apparatus has the same blind spot as the training apparatus. Every scenario targets someone who has already exhausted the standard referrals.
