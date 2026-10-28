---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.33135
url: https://huggingface.co/papers/2610.33135
arxiv_url: https://arxiv.org/abs/2610.33135
date: 2026-10-27
---

# WorldCast: World-Consistent Character Video Generation with Large-Angle Camera Control

Precise camera control is essential for cinematic character video generation, yet existing methods struggle to follow large-angle trajectories with combined rotation, translation, and radius variation from arbitrary initial azimuths. Such viewpoint changes also reveal character regions unseen in the initial frame, causing geometric distortions, appearance degradation, and identity drift. To systematically study these coupled challenges, we introduce CLACT, a large-scale Character-centric dataset and benchmark covering diverse Large-Angle Camera Trajectories, with accurate camera geometry and multi-view character observations for training and evaluation. We further propose WorldCast, a framework for world-consistent character video generation under diverse large-angle camera motions. Specifically, we back-project the initial frame into a 3D point cloud using estimated depth, align the point-cloud scale with the target camera trajectory, and render it along the trajectory to obtain explicit geometric guidance and coverage masks. To complement the incomplete character information, we introduce Geometry-Aligned Memory Attention (GAMA). Using relative camera poses estimated jointly from the initial frame and multi-view character anchors, we express anchor and target-view geometry in a common coordinate frame. GAMA uses this geometric alignment to guide the retrieval and injection of view-relevant character features during generation. Evaluations across diverse large-angle camera trajectories demonstrate accurate trajectory following while preserving character geometry, appearance, and identity.
