---
source: farmer/huggingface
farmed: 2026-05-09T03:37:34Z
arxiv_id: 2605.06196
url: https://huggingface.co/papers/2605.06196
arxiv_url: https://arxiv.org/abs/2605.06196
date: 2026-05-09
---

# The Granularity Axis: A Micro-to-Macro Latent Direction for Social Roles in Language Models

Large language models (LLMs) are routinely prompted to take on social roles ranging from individuals to institutions, yet it remains unclear whether their internal representations encode the granularity of such roles. We find that a contrast-based Granularity Axis, defined as the difference between mean macro- and micro-role hidden states, aligns with the principal axis (PC1) of the role representation space at cosine 0.972 and accounts for 52.6% of its variance in Qwen3-8B. Role projections increase monotonically across all five granularity levels, and the structure remains stable across layers, prompt variants, and score-filtered subsets, and transfers to Llama-3.1-8B-Instruct. The axis is not merely descriptive but causal: intervening along it shifts response granularity in the predicted direction.
