---
source: farmer/huggingface
farmed: 2026-05-17T00:00:00Z
arxiv_id: "2605.15128"
url: "https://huggingface.co/papers/2605.15128"
arxiv_url: "https://arxiv.org/abs/2605.15128"
date: 2026-05-17
---

# MemEye: A Visual-Centric Evaluation Framework for Multimodal Agent Memory

Long-term agent memory is increasingly multimodal, yet existing evaluations rarely test whether agents preserve the visual evidence needed for later reasoning. In prior work, many visually grounded questions can be answered using only captions or textual traces, allowing answers to be inferred without preserving the fine-grained visual evidence. Meanwhile, harder cases that require reasoning over changing visual states are largely absent. Therefore, we introduce MemEye, a framework that evaluates memory capabilities from two dimensions: one measures the granularity of decisive visual evidence (from scene-level to pixel-level evidence), and the other measures how retrieved evidence must be used (from single evidence to evolutionary synthesis). Under this framework, we construct a new benchmark across 8 life-scenario tasks, with ablation-driven validation gates for assessing answerability, shortcut resistance, visual necessity, and reasoning structure. By evaluating 13 memory methods across 4 VLM backbones, we show that current architectures still struggle to preserve fine-grained visual details and reason about state changes over time. Our findings show that long-term multimodal memory depends on evidence routing, temporal tracking, and detail extraction.
