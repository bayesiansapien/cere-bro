---
source: farmer/huggingface
farmed: 2026-05-22T10:21:55.060746+00:00
arxiv_id: 2605.21487
url: https://huggingface.co/papers/2605.21487
arxiv_url: https://arxiv.org/abs/2605.21487
date: 2026-05-21
---

# Uni-Edit: Intelligent Editing Is A General Task For Unified Model Tuning

Currently, enhancing Unified Multimodal Models (UMMs) with image understanding, generation, and editing capabilities mainly relies on mixed multi-task training. Due to inherent task conflicts, such strategy requires complex multi-stage pipelines, massive data mixing, and balancing tricks, merely resulting in a performance trade-off rather than true mutual reinforcement. To break this paradigm, we propose Uni-Edit, an intelligent image editing task that serves as the first general task for UMM tuning. Unlike complex mixed pipelines, Uni-Edit improves performance across all three abilities at once using only one task, one training stage, and one dataset. Specifically, we first identify image editing as an inherently ideal general task, as it naturally demands both visual understanding and generation. However, existing editing data relies on simplistic instructions that severely underutilize a model's understanding capacity. To address this, we introduce the first automated and scalable data synthesis pipeline for intelligent editing, transforming diverse VQA data into complex and effective editing instructions with embedded questions and nested logic. This yields Uni-Edit-148k, pairing diverse reasoning-intensive instructions with high-quality edited images. Extensive experiments on BAGEL and Janus-Pro demonstrate that tuning solely on Uni-Edit achieves comprehensive enhancements across all three capabilities without any auxiliary operations.
