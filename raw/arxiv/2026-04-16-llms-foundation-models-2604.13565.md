---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13565
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13565
published: 2026-04-16
authors: Yunkai Dang, Minxin Dai, Yuekun Yang
---

# UHR-BAT: Budget-Aware Token Compression Vision-Language model for Ultra-High-Resolution Remote Sensing

**arXiv:** https://arxiv.org/abs/2604.13565
**Authors:** Yunkai Dang, Minxin Dai, Yuekun Yang

## Abstract

arXiv:2604.13565v1 Announce Type: cross  Abstract: Ultra-high-resolution (UHR) remote sensing imagery couples kilometer-scale context with query-critical evidence that may occupy only a few pixels. Such vast spatial scale leads to a quadratic explosion of visual tokens and hinders the extraction of information from small objects. Previous works utilize direct downsampling, dense tiling, or global top-k pruning, which either compromise query-critical image details or incur unpredictable compute. In this paper, we propose UHR-BAT, a query-guided and region-faithful token compression framework to efficiently select visual tokens under a strict context budget. Specifically, we leverage text-guided, multi-scale importance estimation for visual tokens, effectively tackling the challenge of achieving precise yet low-cost feature extraction. Furthermore, by introducing region-wise preserve and merge strategies, we mitigate visual token redundancy, further driving down the computational budget. Experimental results show that UHR-BAT achieves state-of-the-art performance across various benchmarks. Code will be available at https://github.com/Yunkaidang/UHR.
