---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.996550+05:30
arxiv_id: 2610.29003
url: https://huggingface.co/papers/2610.29003
arxiv_url: https://arxiv.org/abs/2610.29003
date: 2026-10-28
---

# T-DIG: Text-Conditioned Diversity for Image Generation

Text-to-image (T2I) platforms typically return several images per prompt so users can explore different visual interpretations and choose one that matches their intent. However, T2I models are usually optimized for single-image quality which comes at a cost of multi-image diversity, limiting this exploration. Diversity is also contextual: one user wants variations in background, while another wants them in artistic style, and the same user may later want variations in clothing. The generated images should differ along whatever axis the user cares about. In this paper, we introduce T-DIG, a text-conditioned diversity framework for image generation and editing. T-DIG is an iterative framework comprising multiple modules that lets users type prompts, inspect default generations, request variations using natural language, and continue refining outputs until they're satisfied. At its core, T-DIG uses an LLM policy that produces K axis-conditioned prompts or edit instructions for a frozen generator or editor. We train this policy with GRPO using a text-conditioned diversity reward and alignment penalties. Because the image generator remains frozen, T-DIG applies to open-weight, distilled, and proprietary models. We also release the first dataset for text-conditioned prompt diversity in image generation, with the training and validation splits built from human-written axes and a test set drawn from real user interactions with T-DIG. T-DIG far exceeds baselines in improving text-conditioned diversity, while preserving base-prompt alignment across a variety of metrics and human judgements. We show that user-directed diversity exploration can be added to a wide range of image generation models, open and closed, without the need to access their weights. Website: https://image-study.org/t-dig/
