---
source: farmer/huggingface
farmed: 2026-11-03T14:58:56.496119+05:30
arxiv_id: 2610.40373
url: https://huggingface.co/papers/2610.40373
arxiv_url: https://arxiv.org/abs/2610.40373
date: 2026-11-02
---

# HiFOR: Hierarchical Foresight with Action-Guided World Grounding for Vision-Language-Action Model

Vision-Language-Action (VLA) models have demonstrated promising capabilities in robotic manipulation by integrating visual perception, language understanding, and action generation. Recent advances have further incorporated future prediction to enhance the understanding of environmental dynamics and task progression. However, existing methods often model short-term dynamics and long-term task objectives separately, while directly incorporating predicted futures into action policies without sufficiently considering their relevance to current action requirements. To address these limitations, we propose HiFOR, a hierarchical foresight framework with action-guided world retrieval. Specifically, Hierarchical Foresight Prediction jointly predicts short-term state evolution, semantic milestones, and final goal states through a Hierarchical Dependency Mask (HDM), establishing dependencies across temporal horizons. Building upon these predictions, Structure-Aware Latent World Modeling organizes future latent representations along the horizon, view, and spatial dimensions to facilitate fine-grained retrieval. Furthermore, Action-Guided Factorized World Retrieval adaptively retrieves relevant future information from the structured latent world based on evolving action representations during denoising, providing targeted guidance for action generation. Extensive experiments on two simulation benchmarks and six real-world robotic manipulation tasks demonstrate the effectiveness of our approach.
