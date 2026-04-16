---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13313
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13313
published: 2026-04-16
authors: Eun Woo Im, Dhruv Madhwal, Vivek Gupta
---

# Concrete Jungle: Towards Concreteness Paved Contrastive Negative Mining for Compositional Understanding

**arXiv:** https://arxiv.org/abs/2604.13313
**Authors:** Eun Woo Im, Dhruv Madhwal, Vivek Gupta

## Abstract

arXiv:2604.13313v1 Announce Type: new  Abstract: Vision-Language Models demonstrate remarkable capabilities but often struggle with compositional reasoning, exhibiting vulnerabilities regarding word order and attribute binding. This limitation arises from a scarcity of informative samples needed to differentiate subtle semantic variations during contrastive pretraining. Although hard negative mining offers a promising remedy, existing methods lack explicit mechanisms to dictate which linguistic elements undergo modification. Instead of engineering generative architectures, this study establishes lexical concreteness as a fundamental determinant of negative sample efficacy. Modifying highly concrete terms generates more pronounced structural and visual discrepancies, providing a substantially stronger learning signal. Leveraging this principle, ConcretePlant is proposed to systematically isolate and manipulate perceptually grounded concepts. Analyses of the InfoNCE further reveals a severe gradient imbalance, where easily distinguishable pairs disproportionately overwhelm the optimization process and restrict the bandwidth available for nuanced learning. To resolve this degradation, the Cement loss is formulated utilizing a margin-based approach. By correlating psycholinguistic scores with sample difficulty, this objective dynamically calibrates the penalization applied to individual training pairs. Comprehensive evaluations substantiate these theoretical claims. The integrated framework, designated as Slipform, achieves state-of-the-art accuracy across diverse compositional evaluation benchmarks, general cross-modal retrieval, single and multi label linear probing.
