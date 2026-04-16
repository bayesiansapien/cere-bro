---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.14128
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.14128
published: 2026-04-16
authors: Louie Hong Yao, Vishesh Anand, Yuan Zhuang
---

# Rhetorical Questions in LLM Representations: A Linear Probing Study

**arXiv:** https://arxiv.org/abs/2604.14128
**Authors:** Louie Hong Yao, Vishesh Anand, Yuan Zhuang

## Abstract

arXiv:2604.14128v1 Announce Type: cross  Abstract: Rhetorical questions are asked not to seek information but to persuade or signal stance. How large language models internally represent them remains unclear. We analyze rhetorical questions in LLM representations using linear probes on two social-media datasets with different discourse contexts, and find that rhetorical signals emerge early and are most stably captured by last-token representations. Rhetorical questions are linearly separable from information-seeking questions within datasets, and remain detectable under cross-dataset transfer, reaching AUROC around 0.7-0.8. However, we demonstrate that transferability does not simply imply a shared representation. Probes trained on different datasets produce different rankings when applied to the same target corpus, with overlap among the top-ranked instances often below 0.2. Qualitative analysis shows that these divergences correspond to distinct rhetorical phenomena: some probes capture discourse-level rhetorical stance embedded in extended argumentation, while others emphasize localized, syntax-driven interrogative acts. Together, these findings suggest that rhetorical questions in LLM representations are encoded by multiple linear directions emphasizing different cues, rather than a single shared direction.
