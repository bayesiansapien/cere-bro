---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.387252+00:00
arxiv_id: 2611.25279
url: https://huggingface.co/papers/2611.25279
arxiv_url: https://arxiv.org/abs/2611.25279
date: 2026-11-20
---

# Accord: Universal Online Metric Localization and Dense Mapping from one Camera and an IMU

Dense metric mapping from a single camera and IMU remains challenging: visual-inertial odometry (VIO) provides metric motion but sparse geometry, whereas feed-forward depth models predict dense structure without ensuring metric scale. We present Accord, which constructs an accurate online dense metric map from any camera with an IMU. A VIO filter publishes metric poses, a depth foundation model conditioned on them predicts depth for short keyframe windows, and a factor graph fuses the resulting submaps. Recent work has explored several approaches to this problem. What is essential is the multi-view agreement (Accord), which is considered in SLAM as a source of geometric self-consistency. Accord anchors each keyframe window to metric 3D points triangulated from the filter poses, then exploits bidirectional dense depth agreement between co-visible images to estimate and correct per-image scale errors while preserving the metric scale established by the anchors. Context keyframes further improve depth prediction, and the resulting submaps are fused in a factor graph. We evaluate a single mapping configuration across five public camera-IMU setups and a new Phone-rig/GoPro dataset. With nothing tuned per dataset/setup and every map aligned only by Accord's own trajectory, Accord achieves consistently best/second-best mean F-score at 5 cm on every platform. Accord is open-source along with the phone-rig dataset for the benefit of the research community
