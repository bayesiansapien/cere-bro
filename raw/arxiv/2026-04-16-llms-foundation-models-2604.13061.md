---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13061
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13061
published: 2026-04-16
authors: Wael Hafez, Amir Nazeri
---

# Bi-Predictability: A Real-Time Signal for Monitoring LLM Interaction Integrity

**arXiv:** https://arxiv.org/abs/2604.13061
**Authors:** Wael Hafez, Amir Nazeri

## Abstract

arXiv:2604.13061v1 Announce Type: cross  Abstract: Large language models (LLMs) are increasingly deployed in high-stakes autonomous and interactive workflows, where reliability demands continuous, multi-turn coherence. However, current evaluation methods either rely on post-hoc semantic judges, measure unidirectional token confidence (e.g., perplexity), or require compute-intensive repeated sampling (e.g., semantic entropy). Because these techniques focus exclusively on the model's output distribution, they cannot monitor whether the underlying interaction remains structurally coupled in real time, leaving systems vulnerable to gradual, undetected degradation. Here we show that multi-turn interaction integrity can be continuously monitored using bi-predictability (P), a fundamental information theoretic measure computed directly from raw token frequency statistics. We introduce the Information Digital Twin (IDT), a lightweight architecture that estimates P across the context, response, next prompt loop without secondary inference or embeddings. Across 4,500 conversational turns between a student model and three frontier teacher models, the IDT detected injected disruptions with 100% sensitivity. Crucially, we demonstrate that structural coupling and semantic quality are empirically and practically separable: P aligned with structural consistency in 85% of conditions, but with semantic judge scores in only 44%. This reveals a critical regime of "silent uncoupling" where LLMs produce high-scoring outputs despite degrading conversational context. By decoupling structural monitoring from semantic evaluation, the IDT provides a scalable, computationally efficient mechanism for real-time AI assurance and closed-loop regulation
