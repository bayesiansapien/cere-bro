---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.506302+00:00
arxiv_id: 2610.14293
url: https://huggingface.co/papers/2610.14293
arxiv_url: https://arxiv.org/abs/2610.14293
date: 2026-10-14
---

# GeoFix: Geometry Fixing for 4D Consistent Generation

Video diffusion models increasingly serve as priors for 4D generation, but the generated videos often lack geometric consistency. Recent approaches address this through post-training by designing geometric rewards, yet this can degrade texture and fine detail, requiring auxiliary appearance rewards and careful reward balancing. To address this challenge, we propose GeoFix, a unified framework that improves geometric consistency and visual quality with a single geometric reward, applicable to both training and inference-time reward alignment. Our reward measures cross-view depth consistency in static scene regions, targeting structural inconsistencies without directly constraining appearance or penalizing valid object motion. Crucially, depth agreement increases with camera field-of-view overlap even in real videos and 4D datasets, allowing a smaller camera movement to be mistaken for better geometry. We account for this effect by calibrating the reward against the overlap-dependent trend. GeoFix achieves a 39% improvement in WorldScore 3D consistency and a 4% increase in VBench Quality Score.
