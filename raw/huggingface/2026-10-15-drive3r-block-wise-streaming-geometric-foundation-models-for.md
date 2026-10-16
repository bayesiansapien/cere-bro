---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.235062+05:30
arxiv_id: 2610.15112
url: https://huggingface.co/papers/2610.15112
arxiv_url: https://arxiv.org/abs/2610.15112
date: 2026-10-15
---

# Drive3R: Block-wise Streaming Geometric Foundation Models for Autonomous Driving

High-fidelity closed-loop simulation for autonomous driving increasingly relies on dense multi-view 3D reconstruction. While recent feed-forward geometric foundation models have revolutionized per-scene optimization, applying them to continuous, long-horizon driving sequences is computationally intractable due to GPU memory limits and the quadratic complexity of global attention. Existing scaling strategies are fundamentally limited, as causal streaming suffers from compounding scale drift and trajectory deviation, while rigid "chunk-then-align" heuristics fragment global context and produce trajectory discontinuities. To address these limitations, we introduce Drive3R, a block-wise streaming geometric foundation model. Its block-wise causal attention resolves the scalability bottleneck of fully bidirectional attention while avoiding the loss of local future context in purely causal streaming. Its confidence-aware re-anchoring further mitigates long-range drift by detecting unreliable streaming states, re-initializing the KV cache, and stitching refreshed segments through SE(3) alignment. Extensive experiments demonstrate that Drive3R establishes a new state-of-the-art on nuScenes, KITTI, and Waymo. Specifically, on nuScenes, it improves over the recent DVGT-2 baseline from 0.1806 to 0.1081 in AbsRel, from 0.6750 to 0.5344 in point-cloud Accuracy, and from 1.5812 to 0.9092 in ATE.
