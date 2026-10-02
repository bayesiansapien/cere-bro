---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.352124+05:30
arxiv_id: 2609.38716
url: https://huggingface.co/papers/2609.38716
arxiv_url: https://arxiv.org/abs/2609.38716
date: 2026-10-01
---

# SpatialCORE: Confidence-Aware Grounded Spatial Reasoning in Large Vision--Language Models

Large Vision-Language Models (LVLMs) have made remarkable progress across visual perception tasks, yet spatial reasoning remains a persistent weakness, especially for questions that require reasoning over visual space. Recent spatial-reasoning methods incorporate generated grounding, where models predict bounding boxes, masks, or other localization outputs for task-relevant objects as part of their reasoning trace. However, these approaches typically optimize final-answer correctness alone, allowing correct answers to be rewarded even when the model does not reason from confidently localized task-relevant objects. We introduce SpatialCORE (Spatially COnfident REasoning), a post-training framework that turns the model's own confidence in generated grounding into a learning signal for spatial reasoning. Its central idea is to reinforce grounding that is both accurate and confident, encouraging the model to reason from confidently localized task-relevant objects. SpatialCORE realizes this through a self-regulating spatial reward that weights each predicted bounding box's matching quality by its coordinate-token confidence. An answer gate further ties grounding optimization to final-answer correctness. SpatialCORE achieves state-of-the-art results among open-source and specialized spatial reasoning models across diverse benchmarks, and transfers effectively in zero-shot settings to unseen data distributions. The source code is available at https://github.com/rafiibnsultan/SpatialCORE.
