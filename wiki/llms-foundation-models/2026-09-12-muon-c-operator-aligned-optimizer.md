# Muon-C: Operator-Aligned Muon for Convolutional Kernels

**Source:** arXiv [2609.09676](http://arxiv.org/abs/2609.09676) · Kurate cs.LG #20 (ai_rating 6.5/10), absent from HuggingFace
**Authors:** Jiaxin Qing, Lexin Li
**Raw:** [Kurate cs.LG leaderboard](../../raw/kurate/2026-09-12-cs-lg.md)

## TL;DR

Muon is an optimizer that replaces momentum with an approximately orthogonal "polar" direction, and it has been one of the more consequential practical optimizer results of the last two years. Its weakness is that the orthogonalization depends on how you write the weights as a matrix. For convolutions, the standard trick is to unfold the kernel into a matrix, but that matrix describes a **local patch map**, not the convolution operator you actually care about. Muon-C fixes the representation: it moves to Fourier coordinates, treats the kernel's momentum as **frequency-wise channel-transfer matrices**, polarizes each block independently, and uses a critically sampled Fourier grid to project the update back onto the original finite kernel support exactly. On CIFAR-10 flow matching it reaches **9.87 FID at 40k iterations against 22.26 for unfolded Muon and 51.31 for Adam**, and reaches their final quality at **0.62x and 0.64x their model FLOPs**.

## The argument

Muon's whole premise is geometric: the update direction should be approximately orthogonal in the right norm. So the norm has to be the right one. The paper's observation is that **unfolding a convolution kernel into a matrix gives you the wrong norm**, because the unfolded matrix represents the map from a local patch to an output channel rather than the convolution operator acting on the whole signal. Orthogonalizing that matrix is orthogonalizing the wrong object.

The fix is to work where convolution is diagonal. In Fourier coordinates, a convolution becomes a per-frequency channel-transfer matrix, so the natural block structure is "one matrix per frequency." Muon-C polarizes those blocks independently. The subtlety, and the reason this is a real contribution rather than an obvious one, is that a finite kernel has finite support and the Fourier representation does not automatically respect that. **The critical Fourier grid is the device that returns updates exactly to the original kernel support**, so the optimizer stays in the space of valid kernels.

There is a clean theoretical statement attached: the exact-polar direction is a linear minimization oracle under the **critically sampled convolution norm**, and its worst-case guarantee relative to the continuous convolution-operator norm is **never weaker than unfolding, and strictly stronger for 3x3 kernels**. That is the right shape for this kind of claim, because it says the method cannot lose on the axis it optimizes and wins on the case that dominates practice.

## Numbers worth keeping

- CIFAR-10 flow matching, matched applied-update RMS, 40k iterations: **9.87 FID** (Muon-C) vs **22.26** (unfolded Muon) vs **51.31** (Adam).
- Reaches unfolded Muon's and Adam's final quality at **0.62x and 0.64x their model FLOPs** respectively.
- Under equal tuning budgets, **3.42 FID**.
- Gains persist across data scales and transfer to classification across convolutional architectures.

## How this relates to the rest of the wiki

**The efficiency framing is the reason this is here at all, and it is the number to carry: 0.62x FLOPs to equal quality.** An optimizer change that reaches the same result for 38% fewer training FLOPs is a compression result in everything but name, and it is on an axis the wiki's efficiency pages do not cover. Every entry on the [quantization](../inference-efficiency/quantization.md) and [model pruning](../inference-efficiency/model-pruning-sparsity.md) pages reduces the cost of a *fixed* model, at training time or serving time, by removing bits or removing structure. **Muon-C reduces the cost of reaching a given quality by changing the path**, which composes with all of them and competes with none.

**It is the same species of argument as [WRP (09-10)](../inference-efficiency/2026-09-10-wrp-forward-free-depth-pruning.md), one layer further down.** WRP's claim is that you can read redundancy directly off the checkpoint weights, without forward passes, because the weights already encode the structure you need. Muon-C's claim is that the weights have a **native geometry** that the standard matrix representation destroys. Both are saying the parameter tensor carries more usable structure than the tooling exposes. That is a frame worth naming, because most efficiency work treats the weight tensor as an undifferentiated block of numbers to be shrunk.

## Gaps, and they are large

**CIFAR-10 is a small benchmark and flow matching on it is a small task.** The entire empirical case rests there plus classification transfer. Muon's actual importance came from large-scale language-model pretraining, and **convolutions are not where modern frontier training spends its FLOPs.** So the result is narrow by construction: it is a correct and well-argued fix to a representation problem in a setting that matters most for vision and generative-image workloads. The theoretical guarantee is worst-case relative to unfolding, which is reassuring but does not predict the size of the practical gain at scale. Nothing is reported above CIFAR scale, and the 0.62x FLOPs figure should not be assumed to hold on a large diffusion or video model until someone runs it.

## Industrial implication

Where this lands, if it holds, is image and video generation training, which is both convolution-heavy and among the most expensive training workloads that is not frontier LLM pretraining. A 38% FLOP reduction to equal quality on that class of model is worth a real amount of money to anyone training generative-image models at scale. The adoption path is unusually easy, since it is a drop-in optimizer change with no architecture modification, which means the experiment that validates or kills it costs one training run and someone will do it within a quarter.

**Related:** [model pruning and sparsity](../inference-efficiency/model-pruning-sparsity.md) · [quantization](../inference-efficiency/quantization.md) · [WRP forward-free depth pruning (09-10)](../inference-efficiency/2026-09-10-wrp-forward-free-depth-pruning.md)
