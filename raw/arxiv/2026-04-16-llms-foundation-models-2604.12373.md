---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.12373
category: cs.CL
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.12373
published: 2026-04-16
authors: Tomer Ashuach, Liat Ein-Dor, Shai Gretz
---

# Masked by Consensus: Disentangling Privileged Knowledge in LLM Correctness

**arXiv:** https://arxiv.org/abs/2604.12373
**Authors:** Tomer Ashuach, Liat Ein-Dor, Shai Gretz

## Abstract

arXiv:2604.12373v2 Announce Type: replace  Abstract: Humans use introspection to evaluate their understanding through private internal states inaccessible to external observers. We investigate whether large language models possess similar privileged knowledge about answer correctness, information unavailable through external observation. We train correctness classifiers on question representations from both a model's own hidden states and external models, testing whether self-representations provide a performance advantage. On standard evaluation, we find no advantage: self-probes perform comparably to peer-model probes. We hypothesize this is due to high inter-model agreement of answer correctness. To isolate genuine privileged knowledge, we evaluate on disagreement subsets, where models produce conflicting predictions. Here, we discover domain-specific privileged knowledge: self-representations consistently outperform peer representations in factual knowledge tasks, but show no advantage in math reasoning. We further localize this domain asymmetry across model layers, finding that the factual advantage emerges progressively from early-to-mid layers onward, consistent with model-specific memory retrieval, while math reasoning shows no consistent advantage at any depth.
