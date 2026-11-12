---
source: farmer/huggingface
farmed: 2026-11-12T12:57:12.904916+05:30
arxiv_id: 2611.11912
url: https://huggingface.co/papers/2611.11912
arxiv_url: https://arxiv.org/abs/2611.11912
date: 2026-11-11
---

# LO-World: Unified BEV Latent Modeling for Joint 4D Occupancy and LiDAR Forecasting

LiDAR point clouds and 3D semantic occupancy represent two distinct modalities capturing fine-grained metric geometry and dense volumetric semantics, respectively, holding natural potential for mutual complementarity. However, existing world models typically forecast these modalities independently or cascade them heuristically, missing the opportunity for reciprocal cross-modal regularization. To address this, we propose LO-World, a unified 4D world model that forecasts both modalities within a shared BEV latent space. This single-stream formulation enables dense semantics and metric geometry to mutually reinforce each other, while eliminating multi-pipeline redundancy. Specifically, LO-World couples an efficient hybrid range-voxel autoencoder with a flow-matching generator that caches historical context to reduce iterative sampling latency. Extensive experiments demonstrate that LO-World outperforms prior state-of-the-art baselines, improving occupancy forecasting IoU by 10.9% and reducing LiDAR Chamfer Distance by 30.1%. Meanwhile, it sustains a real-time throughput exceeding 25~FPS on a single RTX 4090. Our code is available at https://github.com/lzzzzzm/LO-World.
