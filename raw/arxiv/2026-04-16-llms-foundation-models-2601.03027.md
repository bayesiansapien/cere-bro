---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2601.03027
category: cs.CL
concept: llms-foundation-models
url: https://arxiv.org/abs/2601.03027
published: 2026-04-16
authors: Sindhuja Chaduvula, Ahmed Y. Radwan, Azib Farooq
---

# Reducing Hallucinations in LLMs via Factuality-Aware Preference Learning

**arXiv:** https://arxiv.org/abs/2601.03027
**Authors:** Sindhuja Chaduvula, Ahmed Y. Radwan, Azib Farooq

## Abstract

arXiv:2601.03027v3 Announce Type: replace  Abstract: Preference alignment methods such as RLHF and Direct Preference Optimization (DPO) improve instruction following, but they can also reinforce hallucinations when preference judgments reward fluency and confidence over factual correctness. We introduce F-DPO (Factuality-aware Direct Preference Optimization), a simple extension of DPO that uses only binary factuality labels. F-DPO (i) applies a label-flipping transformation that corrects misordered preference pairs so the chosen response is never less factual than the rejected one, and (ii) adds a factuality-aware margin that emphasizes pairs with clear correctness differences, while reducing to standard DPO when both responses share the same factuality. We construct factuality-aware preference data by augmenting DPO pairs with binary factuality indicators and synthetic hallucinated variants. Across seven open-weight LLMs (1B-14B), F-DPO consistently improves factuality and reduces hallucination rates relative to both base models and standard DPO. On Qwen3-8B, F-DPO reduces hallucination rates by 5x(from 0.424 to 0.084) while improving factuality scores by 50% (from 5.26 to 7.90). F-DPO also generalizes to out-of-distribution benchmarks: on TruthfulQA, Qwen2.5-14B achieves +17% MC1 accuracy (0.500 to 0.585) and +49% MC2 accuracy (0.357 to 0.531). F-DPO requires no auxiliary reward model, token-level annotations, or multi-stage training.
