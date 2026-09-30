---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.936296+00:00
arxiv_id: 2609.32913
url: https://huggingface.co/papers/2609.32913
arxiv_url: https://arxiv.org/abs/2609.32913
date: 2026-09-29
---

# Allspark: Weak to Strong Transfer via Alternating Chain of Thought

Recent progress in frontier models has renewed interest in large-scale reinforcement learning (RL), but the cost of generating large-model rollouts makes even testing RL recipes expensive. We ask whether reasoning improvements learned by a small, weak model can benefit a larger, stronger model without using the strong model's rollouts during training. We introduce Allspark, a training and inference framework for weak-to-strong transfer through alternating chains of thought. A weak teacher is trained alongside a frozen copy of the same model; the two alternate reasoning segments, and the frozen model produces the final answer. At inference time, a stronger student replaces the frozen training partner, while both models remain fixed. Because they communicate through text, the teacher can steer students from different model families and with different tokenizers. We study Allspark at two scales: controlled Qwen experiments across math and reasoning, and larger-scale Inkling experiments on ARC-AGI-2. The Inkling experiments show accuracy gains in within-family and cross-family settings, including transfer to Kimi and Nemotron, with benefits that vary across inference settings. These findings motivate reusing a trained weak teacher across strong students and examining the resulting accuracy--token tradeoff.
