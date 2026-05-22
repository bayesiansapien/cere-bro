# TIDE: Lossless MoE Diffusion LLM Inference via I/O-Aware Expert Offload

**Source:** HuggingFace Daily Papers 2026-05-21 · arXiv 2605.20179 · [paper](https://arxiv.org/abs/2605.20179) · [raw](../../raw/huggingface/2026-05-21-tide-efficient-and-lossless-moe-diffusion-llm-inference-with.md)
**Topic:** inference-efficiency / MoE / diffusion LLMs

## TL;DR

TIDE is a lossless inference acceleration system for diffusion LLMs with Mixture of Experts (MoE, where each token routes through a small subset of specialized sub-networks) architectures. It exploits the temporal stability of expert activations across denoising steps within a block to build an interval-based expert refresh strategy, schedule the refreshes via mathematical programming for I/O-aware optimality, and never modify the model. On a single GPU-CPU system, throughput rises 1.4x on LLaDA2.0-mini and 1.5x on LLaDA2.0-flash. Training-free, lossless.

## What is new

Diffusion LLMs are starting to compete with autoregressive models on hardware utilization and bidirectional context via parallel block-level decoding. The deployment problem: at MoE scale they outgrow consumer-class memory, and the standard AR-based expert offload strategies (which assume token-by-token autoregression) impose prohibitive I/O overhead or cap throughput on compute. TIDE finds the structural property AR-style strategies cannot exploit: during the denoising process inside a block, the active expert set is temporally stable. Once you know which experts a block of tokens needs, you can keep them resident in GPU memory across multiple denoising steps before refreshing. Formulating the refresh interval as a programming problem (minimize I/O traffic plus CPU compute subject to throughput constraint) gives the optimal interval per workload point. The model never changes; this is a serving-stack optimization.

## Why it matters

Diffusion LLM inference is a small but rapidly growing wedge of the deployment stack. The wiki tracked dLLM efficiency on 2026-04-23 (LLaDA2.0-Uni unification of multimodal understanding and generation) and on 2026-04-23 (expert upcycling for MoE compute efficiency). TIDE is the first systems-side dLLM inference paper in the wiki and the first to find dLLM-specific structure (temporal stability across denoising steps) that AR-MoE serving cannot exploit. 1.4-1.5x throughput on resource-constrained single-GPU-plus-CPU setups is large enough to matter for consumer deployment of LLaDA-class models.

## Research angle

TIDE's temporal-stability claim is dLLM-specific because each denoising step over a block updates many tokens together. Two open questions follow. First, does the temporal stability hold at frontier MoE scale (where DeepSeek-V3-class fine-grained MoE has many more experts per layer)? Second, the refresh interval is solved per workload point; an adaptive policy that tracks the actual expert usage online (rather than pre-solving the program) is the obvious extension and could compose with traffic-shaping at the system level. Cross-paradigm: whether the temporal-stability property has an AR-MoE analog through different token windows is open and would unify dLLM and AR-MoE inference under one framework.

## Related wiki pages

- [LLaDA2.0-Uni multimodal diffusion (2026-04-23)](../llms-foundation-models/2026-04-23-llada20-uni-unifying-multimodal-understanding-generation.md)
- [Expert Upcycling MoE compute efficiency (2026-04-23)](../llms-foundation-models/2026-04-23-expert-upcycling-moe-compute-efficient-frontier.md)
