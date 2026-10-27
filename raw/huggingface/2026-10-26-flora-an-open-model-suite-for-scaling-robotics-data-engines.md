---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.802483+00:00
arxiv_id: 2610.31779
url: https://huggingface.co/papers/2610.31779
arxiv_url: https://arxiv.org/abs/2610.31779
date: 2026-10-26
---

# FLORA: An Open Model Suite for Scaling Robotics Data Engines

The life-cycle of robotics foundation models crucially depends on data labels. Outcome reward labels are needed for monitoring real-world deployments. Process reward labels are needed during RL post-training. Timestamped captions are needed for filtering and balancing pretraining data. We present Flora, an industrial-quality data engine used for training GR00T models, that simultaneously covers these capabilities. Flora achieves SOTA scores on the captioning benchmark WGO-Bench and reward benchmarks RoboReward and Robometer. On internal benchmarks it is competitive with GPT-6 Astra while beating other frontier models. The model is substantially cheaper than API-based alternatives, roughly 125 times cheaper than GPT-6 Astra. Florais battle tested at scale, labeling 200,000 hours of data per day across 512 GB300s. By open-sourcing our data engine, we enable researchers to scale custom robotics datasets and explore emerging applications such as physical auto-research and human-to-robot transfer.
