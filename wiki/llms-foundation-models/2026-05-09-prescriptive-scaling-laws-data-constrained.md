---
source: HuggingFace Daily Papers
arxiv_id: 2605.01640
date: 2026-05-09
tier: 2
topics: [scaling-laws, data-constrained-training, weight-decay, chinchilla]
---

# Prescriptive Scaling Laws for Data Constrained Training

## TL;DR

Chinchilla assumed every training token is unique. With training compute now outpacing high-quality data, that assumption breaks. This paper extends Chinchilla with an additive overfitting penalty for repeated tokens, fits it empirically, and produces qualitatively new compute-optimal advice: past a point, repetition is counterproductive and compute is better spent on model capacity. Strong weight decay (lambda = 1.0) cuts the overfitting coefficient by ~70%, giving a scaling-law explanation for why optimal weight decay in data-constrained regimes is an order of magnitude larger than standard practice.

## Why this matters

The data-bound regime is where the frontier sits. Frontier labs are repeatedly training on the same web crawl with diminishing returns. Chinchilla's "scale data with model size" has been understood as inapplicable in this regime, but until now there was no replacement law. This paper provides one, and it changes the recipe: stop adding tokens past the saturation point, scale the model instead, and crank weight decay an order of magnitude higher than the usual 0.1.

## Connections to prior wiki

**Refines the Chinchilla section of `wiki/llms-foundation-models/scaling-laws.md`** (or whichever concept page tracks scaling laws — should add the additive-overfitting term to the canonical formulation).

**Connection to Distillation-Panic (Lambert, 05-04).** Lambert argued that data scarcity is now the binding constraint on frontier training, hence the move to distillation as a data-augmentation primitive. This paper provides the underlying scaling-law math: data scarcity raises the optimal repetition count, but only up to a saturation point, beyond which capacity wins. Distillation effectively manufactures pseudo-unique tokens, which sidesteps the saturation point entirely. The two papers compose into a coherent picture of why every frontier lab is now distillation-pilled.

**Connection to today's UniPool and EMO.** Both papers move expert capacity around without adding parameters. The scaling law in this paper says capacity matters more than data past the saturation point. UniPool and EMO are the architectural primitives that let you scale capacity efficiently in that regime.

## Research angle

1. **What is the saturation point for current frontier models?** The paper gives the law; it does not give the constants for, say, Llama-class or DeepSeek-class training corpora. Whether DeepSeek V4's reported re-pretraining is past or before the saturation point would be diagnostic.
2. **Does the weight-decay finding interact with sparsity?** MoE training has its own weight-decay quirks. Whether lambda = 1.0 is the right answer for sparse vs dense regimes is open.
3. **Composition with synthetic data.** Synthetic data is the obvious sidestep. The scaling law as written treats all tokens as "natural." A synthetic-token term in the loss is the natural extension.

## Source

- Paper: https://arxiv.org/abs/2605.01640
- HuggingFace: https://huggingface.co/papers/2605.01640
- Raw: `raw/huggingface/2026-05-09-prescriptive-scaling-laws-for-data-constrained-training.md`
