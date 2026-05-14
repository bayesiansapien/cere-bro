---
source: farmer/huggingface
farmed: 2026-05-14T00:00:00
arxiv_id: 2605.13062
url: https://huggingface.co/papers/2605.13062
arxiv_url: https://arxiv.org/abs/2605.13062
date: 2026-05-14
---

# Edit-Compass & EditReward-Compass: A Unified Benchmark for Image Editing and Reward Modeling

Recent image editing models have achieved remarkable progress in instruction following, multimodal understanding, and complex visual editing. However, existing benchmarks often fail to faithfully reflect human judgment, especially for strong frontier models, due to limited task difficulty and coarse-grained evaluation protocols. In parallel, reward models have become increasingly important for RL-based image editing optimization, yet existing reward model benchmarks still rely on unrealistic evaluation settings that deviate from practical RL scenarios. These limitations hinder reliable assessment of both image editing models and reward models. To address these challenges, we introduce Edit-Compass and EditReward-Compass, a unified evaluation suite for image editing and reward modeling. Edit-Compass contains 2,388 carefully annotated instances spanning six progressively challenging task categories, covering capabilities such as world knowledge reasoning, visual reasoning, and multi-image editing. Beyond broad task coverage, Edit-Compass adopts a fine-grained multidimensional evaluation framework based on structured reasoning and carefully designed scoring rubrics. In parallel, EditReward-Compass contains 2,251 preference pairs that simulate realistic reward modeling scenarios during RL optimization. We conduct extensive evaluations on 29 frontier image editing models and 21 reward models. The results reveal a substantial gap between proprietary and open-source systems, while also exposing persistent weaknesses in world knowledge understanding, visual reasoning, and multi-image editing. Moreover, native multimodal large language models outperform existing open-source reward models, including models explicitly trained on preference data. Overall, our benchmark suite provides a comprehensive and human-aligned framework for evaluating frontier image editing systems and reward models.
