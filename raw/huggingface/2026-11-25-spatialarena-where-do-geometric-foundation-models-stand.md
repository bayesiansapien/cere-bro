---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.32816
url: https://huggingface.co/papers/2611.32816
arxiv_url: https://arxiv.org/abs/2611.32816
date: 2026-11-25
---

# SpatialArena: Where Do Geometric Foundation Models Stand?

3D perception is shifting from task-specific pipelines to geometric foundation models: monocular depth networks, feed-forward 3D/4D reconstruction models, and vision--language models that predict geometry. However, their progress cannot be measured reliably. Published numbers are not comparable, because every paper samples frames, sets resolutions, and selects test splits differently. They are not robust because the alignment required for every up-to-scale prediction can outweigh the gap between models: fitting depth in the wrong space nearly triples its error, and standard trajectory alignment understates the error of failing methods by up to 2.6times. And they rarely cover long recordings, dynamic scenes, or aerial views. We present SpatialArena, an open arena that scores geometric models with the same metrics and rules, with robust and deterministic alignment. SpatialArena spans five tasks, from monocular depth to SLAM. It covers 23 public datasets with 418,929 images across indoor, outdoor, aerial, object-centric, and dynamic scenes, together with Spatial Arena, our own captures with accurate poses and depth. Evaluating 52 models, we find that single-image depth is close to saturation on public benchmarks but not on large, uncontrolled scenes, and that progress now comes from consistency across frames and views, where feed-forward 3D/4D models match or surpass monocular specialists and overtake video depth models. The benchmark, toolbox, and leaderboard will be publicly released.
