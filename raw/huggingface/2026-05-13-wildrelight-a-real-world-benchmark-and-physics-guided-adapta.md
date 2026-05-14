---
source: farmer/huggingface
farmed: 2026-05-14T10:39:11Z
arxiv_id: 2605.11696
url: https://huggingface.co/papers/2605.11696
arxiv_url: https://arxiv.org/abs/2605.11696
date: 2026-05-13
---

# WildRelight: A Real-World Benchmark and Physics-Guided Adaptation for Single-Image Relighting

Recent single-image relighting methods, powered by advanced generative models, have achieved impressive photorealism on synthetic benchmarks. However, their effectiveness in the complex visual landscape of the real world remains largely unverified. A critical gap exists, as current datasets are typically designed for multi-view reconstruction and fail to address the unique challenges of single-image relighting. To bridge this synthetic-to-real gap, we introduce WildRelight, the first in-the-wild dataset specifically created for evaluating single-image relighting models. WildRelight features a diverse collection of high-resolution outdoor scenes, captured under strictly aligned, temporally varying natural illuminations, each paired with a high-dynamic-range environment map. Using this data, we establish a rigorous benchmark revealing that state-of-the-art models trained on synthetic data suffer from severe domain shifts. The strictly aligned temporal structure of WildRelight enables a new paradigm for domain adaptation. We demonstrate this by introducing a physics-guided inference framework that leverages the captured natural light evolution as a self-supervised constraint. By integrating Diffusion Posterior Sampling (DPS) with temporal Sampling-Aware Test-Time Adaptation (TTA), we show that the dataset allows synthetic models to align with real-world statistics on-the-fly, transforming the intractable sim-to-real challenge into a tractable self-supervised task. The dataset and code will be made publicly available to foster robust, physically-grounded relighting research.
