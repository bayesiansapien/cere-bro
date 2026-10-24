---
source: farmer/huggingface
farmed: 2026-10-24T12:49:20.886623+00:00
arxiv_id: 2610.30340
url: https://huggingface.co/papers/2610.30340
arxiv_url: https://arxiv.org/abs/2610.30340
date: 2026-10-23
---

# Foundation4D: Towards a unified perception and reconstruction model for autonomous vehicles

We introduce Foundation4D, a unified feed-forward model for geometry estimation, 3D detection, semantic occupancy, and Gaussian reconstruction from multi-camera driving video. A shared backbone uses factorized spatiotemporal attention to efficiently combine observations across cameras and time. Our video inference pipeline uses pose graph optimization to refine camera trajectories and assembles object tracks across input windows. We also develop a data annotation pipeline and release PAI-Foundation4D, a benchmark with dense depth and semantic occupancy labels for 1,253 driving clips. With benchmark-specific fine-tuning, Foundation4D achieves the lowest depth AbsRel on Waymo and nuScenes, the highest detection mAP on nuScenes, and the highest occupancy mIoU on OpenOccupancy among the compared methods. Our task-combination study shows benefits for both detection and geometry: co-training detection with geometry and occupancy improves top-class mAP by 1.2 points over detection-only training, while co-training geometry with detection reduces camera-to-rig translation error by 13.4% relative to geometry-only training. We further use the predicted geometry and trajectories as priors for lidarless NuRec, supporting reconstruction of driving scenes for simulation.
