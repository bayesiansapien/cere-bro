---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.33079
url: https://huggingface.co/papers/2610.33079
arxiv_url: https://arxiv.org/abs/2610.33079
date: 2026-10-27
---

# Rethinking Video Storage for AI Training: Breaking Cross-Frame Dependencies for Efficient Random Access

Large-scale AI training increasingly relies on massive video datasets with random temporal sampling patterns. However, existing video storage paradigms are optimized for sequential playback and employ sophisticated inter-frame reference structures to maximize compression efficiency. When applied to the random-sampling workloads of AI training, these paradigms face substantial decoding-efficiency bottlenecks. Workarounds such as independent JPEG frames and short groups of pictures (GOPs) reduce decoding work at the cost of larger storage and transfer volumes. In this paper, we identify two sources of decode amplification: sequential reconstruction of unrelated frames and reconstruction of the reference chains required by sampled targets. We address both sources by co-designing the decoding schedule and video reference structure. Dependency-aware sparse decoding reconstructs only requested frames and their required references, skipping unrelated reconstruction without transcoding the source videos. Optional offline Dependency-Decoupled Random Access (DDRA) encoding further reduces reference reconstruction by restricting each interior frame to two bounding intra-coded anchors. Together, sparse decoding and DDRA retain inter-frame prediction while bounding reconstruction to at most three frames per requested target, independent of the intra period. Experiments on a large-scale robotics corpus show that, at comparable reconstruction quality, our method achieves 1.45times the loading throughput of LeRobot v3 with 58.7% less media payload.
