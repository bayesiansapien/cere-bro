---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.14141
category: cs.CV
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.14141
published: 2026-04-16
authors: Lin-Zhuo Chen, Jian Gao, Yihang Chen
---

# Geometric Context Transformer for Streaming 3D Reconstruction

**arXiv:** https://arxiv.org/abs/2604.14141
**Authors:** Lin-Zhuo Chen, Jian Gao, Yihang Chen

## Abstract

arXiv:2604.14141v1 Announce Type: new  Abstract: Streaming 3D reconstruction aims to recover 3D information, such as camera poses and point clouds, from a video stream, which necessitates geometric accuracy, temporal   consistency, and computational efficiency. Motivated by the principles of Simultaneous Localization and Mapping (SLAM), we introduce LingBot-Map, a feed-forward 3D foundation   model for reconstructing scenes from streaming data, built upon a geometric context transformer (GCT) architecture. A defining aspect of LingBot-Map lies in its carefully   designed attention mechanism, which integrates an anchor context, a pose-reference window, and a trajectory memory to address coordinate grounding, dense geometric cues, and   long-range drift correction, respectively. This design keeps the streaming state compact while retaining rich geometric context, enabling stable efficient inference at around   20 FPS on 518 x 378 resolution inputs over long sequences exceeding 10,000 frames. Extensive evaluations across a variety of benchmarks demonstrate that our approach   achieves superior performance compared to both existing streaming and iterative optimization-based approaches.
