---
source: HuggingFace Daily Papers
arxiv_id: 2605.04077
date: 2026-05-09
tier: 2
topics: [rlvr, grpo, gradient-aggregation]
---

# Balanced Aggregation: Understanding and Fixing Aggregation Bias in GRPO

## TL;DR

Standard GRPO uses sequence-level aggregation (downweights longer responses implicitly). Recent work moved to token-level aggregation (introduces sign-length coupling). Both are biased. Balanced Aggregation (BA) computes token-level means separately within positive and negative subsets, then combines with sequence-count weights. Drop-in replacement, consistent gains on Qwen2.5-Math-7B and Qwen3-1.7B.

## Connection to prior wiki

This is the third paper in the wiki this month diagnosing GRPO's optimization bias (after [LongAct](../inference-efficiency/2026-04-18-longact-saliency-sparse-rl.md) on saliency masking, and the [ResRL](../llms-foundation-models/2026-05-08-resrl-negative-sample-projection-rl.md) negative-projection fix from yesterday). The pattern: GRPO's headline simplicity hides multiple structural biases that need to be fixed independently. ResRL fixes the gradient interference. BA fixes the aggregation bias. They compose.

## Research angle

Combine BA with ResRL: BA's split aggregation already separates positive and negative gradients; ResRL's projection then decouples them inside the negative subset. The composition is a one-line swap on top of standard GRPO and should be evaluated.

## Source

- Paper: https://arxiv.org/abs/2605.04077
