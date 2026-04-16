---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13508
category: cs.CV
concept: agents-tool-use
url: https://arxiv.org/abs/2604.13508
published: 2026-04-16
authors: Sanghyeok Chu, Pyunghwan Ahn, Gwangmo Song
---

# Enhancing Mixture-of-Experts Specialization via Cluster-Aware Upcycling

**arXiv:** https://arxiv.org/abs/2604.13508
**Authors:** Sanghyeok Chu, Pyunghwan Ahn, Gwangmo Song

## Abstract

arXiv:2604.13508v1 Announce Type: new  Abstract: Sparse Upcycling provides an efficient way to initialize a Mixture-of-Experts (MoE) model from pretrained dense weights instead of training from scratch. However, since all experts start from identical weights and the router is randomly initialized, the model suffers from expert symmetry and limited early specialization. We propose Cluster-aware Upcycling, a strategy that incorporates semantic structure into MoE initialization. Our method first partitions the dense model's input activations into semantic clusters. Each expert is then initialized using the subspace representations of its corresponding cluster via truncated SVD, while setting the router's initial weights to the cluster centroids. This cluster-aware initialization breaks expert symmetry and encourages early specialization aligned with the data distribution. Furthermore, we introduce an expert-ensemble self-distillation loss that stabilizes training by providing reliable routing guidance using an ensemble teacher. When evaluated on CLIP ViT-B/32 and ViT-B/16, Cluster-aware Upcycling consistently outperforms existing methods across both zero-shot and few-shot benchmarks. The proposed method also produces more diverse and disentangled expert representations, reduces inter-expert similarity, and leads to more confident routing behavior.
