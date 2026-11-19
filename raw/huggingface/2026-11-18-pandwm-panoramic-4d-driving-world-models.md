---
source: farmer/huggingface
farmed: 2026-11-19T11:13:13+05:30
arxiv_id: 2611.19857
url: https://huggingface.co/papers/2611.19857
arxiv_url: https://arxiv.org/abs/2611.19857
date: 2026-11-18
---

# PanDWM: Panoramic 4D Driving World Models

Driving world models usually generate videos from six pinhole cameras with separate optical centres and small overlaps, and must learn to keep these views consistent. We present PanDWM, which stitches them into one 360^circ panoramic band. Camera boundaries then fall inside one image, so keeping the views consistent means keeping the image continuous, and each pixel still records its camera ray. Conditioned on layouts, a causal student generates the band window by window in four steps; it is distilled from a causal teacher and trained on its own rollouts. A feed-forward decoder lifts each frame along these rays into 3D Gaussians, and static Gaussians from neighbouring frames complete them into 4D scenes. On nuScenes, scored in one stitched 360^circ view, PanDWM has lower FID and FVD than the multi-camera baselines at 8-46times their speed, and keeps its 50-step teacher's FID while lowering FVD by 22-25%.
