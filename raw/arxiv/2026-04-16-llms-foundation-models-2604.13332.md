---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13332
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13332
published: 2026-04-16
authors: Jingyun Jia, Chandan Singh, Rich Caruana
---

# Selecting Feature Interactions for Generalized Additive Models by Distilling Foundation Models

**arXiv:** https://arxiv.org/abs/2604.13332
**Authors:** Jingyun Jia, Chandan Singh, Rich Caruana

## Abstract

arXiv:2604.13332v1 Announce Type: new  Abstract: Identifying meaningful feature interactions is a central challenge in building accurate and interpretable models for tabular data. Generalized additive models (GAMs) have shown great success at modeling tabular data, but often rely on heuristic procedures to select interactions, potentially missing higher-order or context-dependent effects. To meet this challenge, we propose TabDistill, a method that leverages tabular foundation models and post-hoc distillation methods. Our key intuition is that tabular foundation models implicitly learn rich, adaptive feature dependencies through large-scale representation learning. Given a dataset, TabDistill first fits a tabular foundation model to the dataset, and then applies a post-hoc interaction attribution method to extract salient feature interactions from it. We evaluate these interactions by then using them as terms in a GAM. Across tasks, we find that interactions identified by TabDistill lead to consistent improvements in downstream GAMs' predictive performance. Our results suggest that tabular foundation models can serve as effective, data-driven guides for interaction discovery, bridging high-capacity models and interpretable additive frameworks.
