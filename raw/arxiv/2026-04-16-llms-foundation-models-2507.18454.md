---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2507.18454
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2507.18454
published: 2026-04-16
authors: Juntao Zhao, Jiuru Li, Chuan Wu
---

# Sandwich: Joint Configuration Search and Hot-Switching for Efficient CPU LLM Serving

**arXiv:** https://arxiv.org/abs/2507.18454
**Authors:** Juntao Zhao, Jiuru Li, Chuan Wu

## Abstract

arXiv:2507.18454v2 Announce Type: replace-cross  Abstract: CPUs are critical for LLM serving due to their availability, cost efficiency, and edge applicability. However, efficient CPU serving is hindered by conflicting prefill/decode resource demands under non-disaggregated deployment constraints--existing solutions fail to avoid cross-phase interference, ignore sub-NUMA hardware structures, and deliver suboptimal dynamic-shape kernel performance. We propose Sandwich, a full-stack CPU LLM serving system with three core innovations addressing these challenges: (1) seamless phase-wise plan switching to eliminate cross-phase interference; (2) TopoTree, a tree-based hardware abstraction for automated substructure-aware (e.g., LLC slices) partial core allocation; (3) fast-start-then-finetune dynamic-shape tensor program generation. Across five x86/ARM CPU platforms, Sandwich achieves an average 2.01x end-to-end speedup and up to 3.40x latency reduction over state-of-the-art systems. Its kernels match static compiler performance with three orders of magnitude lower tuning cost.
