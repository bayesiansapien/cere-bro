# Nemotron 3 Super: Hybrid Mamba-Attention MoE at NVFP4

**Date:** 2026-04-21  
**Source:** DAIR.AI weekly papers roundup  
**Coverage:** [DAIR.AI Top Papers](https://dair.ai/)  
**Raw:** (parallel daily digest 2026-04-21)

---

## TL;DR

NVIDIA's Nemotron 3 Super is a 120B parameter / 12B active parameter hybrid model combining Mamba state-space blocks with sparse LatentMoE attention layers. It is the first Nemotron 3 model pretrained in NVFP4 (4-bit floating point), trained on 25 trillion tokens. Key throughput: 2.2x over GPT-OSS-120B and 7.5x over Qwen3.5-122B at comparable accuracy. Supports 1M context length. Native speculative decoding via Multi-Token Prediction (MTP) layers with no external draft model required. All artifacts (datasets, base, post-trained, and quantized checkpoints) are open-sourced.

---

## Architecture

```
Nemotron 3 Super (120B total / 12B active):
  ┌──────────────────────────────────────────────┐
  │  Input tokens                                │
  │      │                                       │
  │  [Mamba block]  ← SSM, linear-time sequence  │
  │      │                                       │
  │  [LatentMoE]   ← sparse attention            │
  │    Route tokens → latent dimension            │
  │    Select K of N experts for computation      │
  │      │                                       │
  │  [Mamba block]                               │
  │      │                                       │
  │  [MTP heads]   ← speculative decoding        │
  │    Predict tokens t+1, t+2, ... t+k          │
  │    Main model verifies, accepts or rejects    │
  └──────────────────────────────────────────────┘
```

**Mamba blocks** replace standard attention for the majority of sequence processing. Mamba uses a selective state-space model (SSM) with O(L) complexity vs O(L²) for full attention. This is where the long-context (1M token) capability comes from — Mamba doesn't pay quadratic cost for longer sequences.

**LatentMoE layers** handle the capacity that Mamba doesn't cover. Standard MoE routes tokens to experts at full model dimension. LatentMoE first projects tokens into a smaller latent dimension, runs routing and expert computation there, then projects back. This reduces the parameter count per expert while maintaining expert diversity — the mechanism behind the 120B/12B ratio.

**NVFP4 pretraining** is the efficiency backbone. FP4 (4-bit floating point) at pretraining time (not just inference quantization) allows training on 25T tokens with dramatically reduced memory and compute per FLOP. NVIDIA's NV variant of FP4 tuned the numerical range for their hardware. This is the first large-scale demonstration of FP4 pretraining for a Nemotron model.

**MTP (Multi-Token Prediction)** layers are integrated into the main model for native speculative decoding. Standard speculative decoding needs a separate smaller "draft model" to propose tokens for the main model to verify. MTP embeds this speculation into the model itself — the same parameters generate both the verified output and the draft proposals for subsequent tokens. This removes deployment friction (no separate model to serve, manage, or keep in sync).

---

## Key Numbers

| Metric | Nemotron 3 Super | GPT-OSS-120B | Qwen3.5-122B |
|--------|-----------------|--------------|--------------|
| Active params | 12B | ~120B | ~120B |
| Throughput | 1x (baseline) | 0.45x | 0.13x |
| Context length | 1M | — | — |
| Pretraining precision | NVFP4 | — | — |

---

## Relation to Prior Wiki Pages

**Convergence with STOP (04-20) and 1D Ordered Tokens (04-20):** Both those papers attacked inference efficiency at the reasoning path level. Nemotron 3 Super attacks it at the architecture level — sparse activation through MoE + SSM base. The efficiency mechanisms are orthogonal and composable: you could run STOP's path pruning on top of a Nemotron 3 Super serving stack.

**Extends KV Packet (04-17):** KV Packet achieved zero-recomputation KV cache reuse via soft-token adapters. Nemotron's Mamba blocks sidestep the KV cache problem differently — SSMs don't have quadratic attention KV growth. For long context, these are competing approaches: Mamba avoids the problem, while KV Packet manages it.

**Extends LongAct (04-18) research angle:** LongAct asked whether high-magnitude activations (the positions where long-context training signal concentrates) can be profiled efficiently online. Nemotron's hybrid architecture changes the question: if Mamba handles most sequence processing, the "high-magnitude position" problem may be concentrated in the sparse LatentMoE layers — smaller and more tractable to profile.

**Intersection with SemiAnalysis Goodput (2026-04-21):** The 2.2x throughput improvement over GPT-OSS-120B is exactly the kind of efficiency gain that changes goodput economics for a cluster. Higher throughput per GPU means more tokens-per-hour at constant infrastructure cost, which improves the useful-work fraction of every GPU-hour.

---

## Why It Matters (Tier 1 Assessment)

This is a convergence model — the first major architecture to simultaneously use SSM + sparse MoE + low-precision pretraining + native speculative decoding at large scale. Each of those was a separate research direction. Nemotron 3 Super ships all four together and open-sources everything.

The 7.5x throughput advantage over Qwen3.5-122B is striking if the accuracy parity holds. It suggests that dense transformer baselines at 120B scale are now substantially sub-optimal for inference throughput. The question is whether this architecture generalizes across task types or is optimized for specific domains.

---

## Research Angle (Tier 1)

**Open problem 1:** NVFP4 at pretraining scale. FP8 is now standard for training at scale; FP4 introduces larger quantization error that requires specific techniques (careful initialization, loss scaling, gradient clipping). How much of Nemotron's training required NVIDIA-specific hardware features (H100 FP4 tensor cores)? If it's hardware-locked, FP4 pretraining won't democratize. If the techniques are architecture-general, this could push the field toward FP4 pretraining within 12–18 months.

**Open problem 2:** MTP layers and speculative decoding acceptance rate. The value of speculative decoding depends on how many proposed tokens get accepted. High acceptance means throughput multiplier; low acceptance means overhead. Acceptance rate is task-dependent. What's the acceptance rate distribution across Nemotron's use cases?

**Open problem 3:** SSM + MoE robustness. Mamba's selective state space has known limitations on tasks requiring very precise long-distance retrieval (e.g., "find the needle in the 100K-token haystack"). How does the Mamba+LatentMoE combination perform on retrieval-heavy tasks vs pure-attention baselines at the same active parameter count?

---

## Related Pages

- [KV Cache](kv-cache.md)
- [KV Packet: Recomputation-Free KV Cache Reuse](2026-04-17-kv-packet-recomputation-free-kv-cache.md)
- [LongAct: Saliency-Guided Sparse RL](2026-04-18-longact-saliency-sparse-rl.md)
- [STOP: Learnable Path Pruning](2026-04-20-stop-path-pruning-parallel-reasoning.md)
- [GPU Kernels](../hardware/gpu-kernels.md)
- [SemiAnalysis GPU Cluster Goodput](2026-04-21-semianalysis-gpu-cluster-goodput.md)
