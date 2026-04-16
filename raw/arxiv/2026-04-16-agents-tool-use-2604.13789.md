---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13789
category: cs.CV
concept: agents-tool-use
url: https://arxiv.org/abs/2604.13789
published: 2026-04-16
authors: Jaejoon Yoo, SuBeen Lee, Yerim Jeon
---

# Temporally Consistent Long-Term Memory for 3D Single Object Tracking

**arXiv:** https://arxiv.org/abs/2604.13789
**Authors:** Jaejoon Yoo, SuBeen Lee, Yerim Jeon

## Abstract

arXiv:2604.13789v1 Announce Type: new  Abstract: 3D Single Object Tracking (3D-SOT) aims to localize a target object across a sequence of LiDAR point clouds, given its 3D bounding box in the first frame. Recent methods have adopted a memory-based approach to utilize previously observed features of the target object, but remain limited to only a few recent frames. This work reveals that their temporal capacity is fundamentally constrained to short-term context due to severe temporal feature inconsistency and excessive memory overhead. To this end, we propose a robust long-term 3D-SOT framework, ChronoTrack, which preserves the temporal feature consistency while efficiently aggregating the diverse target features via long-term memory. Based on a compact set of learnable memory tokens, ChronoTrack leverages long-term information through two complementary objectives: a temporal consistency loss and a memory cycle consistency loss. The former enforces feature alignment across frames, alleviating temporal drift and improving the reliability of proposed long-term memory. In parallel, the latter encourages each token to encode diverse and discriminative target representations observed throughout the sequence via memory-point-memory cyclic walks. As a result, ChronoTrack achieves new state-of-the-art performance on multiple 3D-SOT benchmarks, demonstrating its effectiveness in long-term target modeling with compact memory while running at real-time speed of 42 FPS on a single RTX 4090 GPU. The code is available at https://github.com/ujaejoon/ChronoTrack
