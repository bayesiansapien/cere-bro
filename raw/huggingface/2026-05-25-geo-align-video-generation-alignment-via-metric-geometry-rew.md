---
source: farmer/huggingface
farmed: 2026-05-25T08:23:16Z
arxiv_id: 2605.23903
url: https://huggingface.co/papers/2605.23903
arxiv_url: https://arxiv.org/abs/2605.23903
date: 2026-05-25
---

# Geo-Align: Video Generation Alignment via Metric Geometry Reward

Camera-controlled video generation has achieved remarkable progress in recent years. However, existing video-to-video re-rendering methods primarily rely on Supervised Fine-Tuning using synthetic datasets. At present, there is an extreme scarcity of synchronized, multi-view real-world video data. Consequently, the prevailing paradigm often exhibits limited generalization when processing out-of-distribution real-world videos, with models struggling to accurately adhere to physical scales and camera trajectories. To bridge this gap, we propose Geo-Align, the first Reinforcement Learning framework specifically designed for camera-controlled video re-rendering. Built upon a pretrained model, we optimize the model through a scale-aware perceptual reward mechanism. Specifically, we introduce a metric 3D estimator to extract precise camera trajectories from generated videos, explicitly penalizing deviations in rotation and translation. Furthermore, we meticulously designed a data pipeline strategy based on real-world conditioning videos and target camera trajectories derived from synthetic data, eliminating the reliance on paired data. Extensive experiments demonstrate that Geo-Align consistently outperforms existing supervised learning baselines in both precise camera controllability and visual fidelity, indicating the effectiveness of our method.
