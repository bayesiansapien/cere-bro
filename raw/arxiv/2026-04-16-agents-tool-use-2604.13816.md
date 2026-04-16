---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13816
category: cs.LG
concept: agents-tool-use
url: https://arxiv.org/abs/2604.13816
published: 2026-04-16
authors: Aggelos Semoglou, Aristidis Likas, John Pavlopoulos
---

# Composite Silhouette: A Subsampling-based Aggregation Strategy

**arXiv:** https://arxiv.org/abs/2604.13816
**Authors:** Aggelos Semoglou, Aristidis Likas, John Pavlopoulos

## Abstract

arXiv:2604.13816v1 Announce Type: new  Abstract: Determining the number of clusters is a central challenge in unsupervised learning, where ground-truth labels are unavailable. The Silhouette coefficient is a widely used internal validation metric for this task, yet its standard micro-averaged form tends to favor larger clusters under size imbalance. Macro-averaging mitigates this bias by weighting clusters equally, but may overemphasize noise from under-represented groups. We introduce Composite Silhouette, an internal criterion for cluster-count selection that aggregates evidence across repeated subsampled clusterings rather than relying on a single partition. For each subsample, micro- and macro-averaged Silhouette scores are combined through an adaptive convex weight determined by their normalized discrepancy and smoothed by a bounded nonlinearity; the final score is then obtained by averaging these subsample-level composites. We establish key properties of the criterion and derive finite-sample concentration guarantees for its subsampling estimate. Experiments on synthetic and real-world datasets show that Composite Silhouette effectively reconciles the strengths of micro- and macro-averaging, yielding more accurate recovery of the ground-truth number of clusters.
