---
title: "DSpine parallel drafter and FLUX 3 Klein on Blackwell: two serving recipes"
date: 2026-11-09
source: https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16
raw: ../../raw/labs/2026-11-07-221605-labs.md
tags: [speculative-decoding, nvfp4, fp8-attention, diffusion-serving]
---

# DSpine and FLUX 3 Klein on Blackwell

## Tencent DSpine (open weights)
[Qwen3.8-27B-DSpine-b16](https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16) ([arXiv 2609.36173](https://arxiv.org/abs/2609.36173), [code](https://github.com/Tencent/DSpine)) is a 5-layer parallel draft model. Each layer passes its predicted predecessor features to the neighbouring positions, so causal dependence travels through network depth instead of through sequential steps. Block size 16, 8,192-token sliding window.

- Acceptance length vs DFlash2 at T=0: GSM8K 7.20 vs 5.69, MATH-500 6.49 vs 5.49, HumanEval 5.71 vs 4.87, MT-Bench 4.48 vs 4.11.
- Agent end-to-end in SGLang (BF16, FA3, concurrency 8): 2.71-3.84x over plain decoding vs DFlash2's 2.33-3.17x; SWE-bench Pro 3.19x, tau2-bench 3.20x.
- DeepSeek-style dynamic verification plus ReplaySSM for the linear-attention/Mamba layers of the hybrid target. Apache 2.0.
- The target, Qwen3.8-27B, is also the model Microsoft Foundry Local now runs on-device for GitHub Copilot (73.0 Terminal Bench 2.1).

## NVIDIA FLUX 3 Image Klein on Blackwell
[NVIDIA's post](https://developer.nvidia.com/blog/speed-up-image-generation-with-flux-3-image-klein-on-nvidia-blackwell-gpus/) stacks every serving trick on a diffusion transformer:
- NVFP4 vs BF16 on one B200: 1.62x text-to-image, 1.58x image-to-image; combined at 2048x2048: up to 3.46x and 4.45x.
- Attention is ~60% of DiT kernel time. cuDNN FP8 1.08x; VC-Attention FP8 with a 0.5% "repair budget" (exact recompute on the highest-error tokens) 1.18x; Sol-Attention block-sparse 1.24-1.30x.
- Cache-DiT step caching 1.94x at 2048, LPIPS 0.033. 8x B200 with Ulysses sequence parallel: 14.90s to 3.00s.

## Relation to prior wiki
- DSpine is the fourth drafter in a week to beat DFlash, after D3D (11-06, diffusion drafter without target hidden states, 5.00x vs 4.03x), SpecPilot's tuned configs (11-05) and ChainFlow ([11-09](2026-11-09-chainflow-speculative-listening.md), +11% over DFlash with flow matching on target hidden states). DFlash is now the baseline everyone beats, which is the sign of a crowded design space.
- VC-Attention's "repair the worst tokens exactly" is the same principle as outlier-aware KV quantization: spend precision only where error concentrates ([quantization](quantization.md)).

Concept pages: [speculative decoding](speculative-decoding.md) · [quantization](quantization.md)
