---
source: farmer/huggingface
farmed: 2026-06-06T09:05:36Z
arxiv_id: 2606.05172
url: https://huggingface.co/papers/2606.05172
arxiv_url: https://arxiv.org/abs/2606.05172
date: 2026-06-06
---

# Is This Edit Correct? A Multi-Dimensional Benchmark for Reasoning-Aware Image Editing

Diffusion-based image editing has achieved strong visual fidelity under natural language instructions, yet most existing systems still operate at the level of surface instruction following, without reasoning about the implicit contextual constraints embedded in real user requests. This often leads to visually plausible but logically inconsistent edits. In this work, we introduce RE-Edit, a benchmark for REasoning-aware image Editing that evaluates image editing systems across five complementary reasoning dimensions: physical, environmental, cultural, causal, and referential. RE-Edit comprises 1,000 carefully curated samples, each designed such that visual plausibility alone is insufficient and correct editing requires satisfying implicit logical constraints. To support fine-grained analysis, we establish dimension-aligned evaluation criteria and conduct a comprehensive study of ten open-source and two commercial image editing models. Our results show that even advanced systems frequently struggle with implicit multi-dimensional reasoning despite producing high-quality visuals. We further present a lightweight reasoning-guided post-edit baseline as an initial exploration, illustrating how inserting explicit reasoning can help mitigate such failures in a model-agnostic manner.
