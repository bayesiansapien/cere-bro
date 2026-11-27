---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.910574+00:00
arxiv_id: 2611.32335
url: https://huggingface.co/papers/2611.32335
arxiv_url: https://arxiv.org/abs/2611.32335
date: 2026-11-26
---

# GOLD-SLAM: Gaussian-splatting Omnidirectional LiDAR-Depth SLAM

Panoramic cameras capture nearly the entire spherical field of view in a single frame. However, the mismatch between this panoramic coverage and the field of view of LiDAR poses a substantial challenge for panoramic Gaussian splatting SLAM that relies on LiDAR depth priors. We introduce GOLD-SLAM, a Gaussian-splatting Omnidirectional LiDAR-Depth SLAM system that combines high-quality rendering with accurate geometric reconstruction. It performs tracking and mapping in the spherical domain and uses tracked visual features in regions without LiDAR coverage to improve pose estimation. To address insufficient coverage of newly observed surfaces and floating artifacts during incremental mapping, we introduce Depth-Aware Map Extension and Pruning (DAEP). To enable broader evaluation, we collect a new dataset, WHOLE, using a UAV platform across Weak-geometry, High-dynamic, Omnidirectional, Low-light, and Easy scenarios. Extensive experiments on public benchmarks and WHOLE demonstrate competitive rendering quality and improved geometric accuracy relative to perspective systems. Compared with existing panoramic baselines, GOLD-SLAM improves mean PSNR by 5.56-9.10 dB and reduces mean Depth-L1 by 71.9-83.9%. To assess deployment feasibility on resource-constrained platforms such as UAVs, we evaluate an embedded configuration of GOLD-SLAM on a Jetson Orin NX (16 GB), demonstrating online operation at the cost of reconstruction quality.
