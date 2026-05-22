# 110 tok/s on 12GB VRAM with Qwen3.6-35B-A3B via ik_llama.cpp and MTP

**Source:** r/LocalLLaMA practitioner report by u/janvitos, 2026-05-21. Score 271, comments 92.
**Reddit:** [Benchmark post](https://www.reddit.com/r/LocalLLaMA/comments/1tjh7az/110_toks_with_12gb_vram_on_qwen36_35b_a3b_and_ik/)
**Adjacent fix:** [llama.cpp b9274 MTP VRAM leak fix (issue #23461)](https://github.com/ggml-org/llama.cpp/releases) (separately reported on r/LocalLLaMA by u/Bulky-Priority6824).

## TL;DR

A practitioner running an RTX 4070 Super (12 GB VRAM), Ryzen 7 9700X CPU, and 48 GB DDR5-6000 reports 110 tok/s decode throughput on Qwen3.6-35B-A3B (a 35B-total / 3B-active MoE) using a fork of llama.cpp called ik_llama.cpp, with Multi-Token Prediction (MTP) speculative decoding enabled. After Tencent's MTP PR was merged into upstream llama.cpp, throughput on the original benchmark setup dropped, but ik_llama.cpp, which is reportedly better optimized for CPU offloading of MoE expert layers, recovered and surpassed the original. Comparison numbers across upstream llama.cpp's mtp-bench.py for the same quant (byteshape/Qwen3.6-35B-A3B-IQ4_XS-4.19bpw, 4 GB smaller than Unsloth's Q5_K_XL at similar accuracy) show 79.8-89.1 tok/s on standard code/explain/summarize tasks. The ik_llama.cpp run pushes that higher.

## Why this matters

Three concrete Tier 1 inference-efficiency signals:

1. **MoE + CPU offloading + speculative decoding now produces frontier-relevant throughput on a single consumer GPU.** 110 tok/s decoding on a 35B-A3B is in the range where the local-LLM stack is genuinely usable for coding agents and conversational work, not just toy.

2. **ik_llama.cpp emerges as the production-grade fork for MoE-on-consumer-GPU workloads.** When upstream merges break performance for niche but important configurations (CPU offload of MoE expert weights), specialized forks fill the gap. This is the same dynamic that produced llama.cpp itself originally.

3. **The byteshape IQ4_XS quant family is interesting.** 4.19 bpw with 4 GB smaller footprint than Unsloth's Q5_K_XL at "similar accuracy" suggests the quantization frontier is still moving. Worth tracking alongside Tencent's AngelSlim 1.25-bit ([2026-05-21 Tencent Hy-MT2](2026-05-21-tencent-hy-mt2-translation-quantization.md)).

The companion llama.cpp PR #23461 (release b9274) fixes a long-standing MTP VRAM leak in the speculative decoder context cleanup path: the destroy() function in server_context_impl previously did not free spec/ctx_dft/model_dft on sleep, so each sleep/resume cycle leaked GPU resources until OOM. This is a load-bearing fix for any deployment that relies on sleep_idle_seconds for power management.

## What ik_llama.cpp does differently (from the post)

The poster does not give a deep technical breakdown, but the upstream-vs-fork gap appears to be in:
- CPU offload of expert layers (the "A3B" structure means most expert weights are inactive per token, so they can sit in CPU RAM and be paged into GPU only when activated).
- MTP integration that handles speculative-decoding draft model context cleanup correctly even when expert routing changes between draft and target.
- ROCm and CUDA path differences that haven't merged back upstream.

## Industrial implication

The wiki has been tracking the gap between "frontier capability" and "frontier capability that runs on a single GPU you can buy at retail." That gap is now smaller than it was a quarter ago. With 110 tok/s on a 4070 Super, the threshold for personal-AI deployment is roughly $700 GPU + $1500 system rather than $25,000 H100 + datacenter. This shifts the deployment model the wiki tracks in its agentic-systems pages: agentic workloads can run on a developer's desk, with cloud GPUs reserved for training and the largest models.

## Cross-references

- [Tencent Hy-MT2 (2026-05-21)](2026-05-21-tencent-hy-mt2-translation-quantization.md)
- [MoE muP scale-stable parameterization (2026-05-21)](2026-05-21-moe-mup-scale-stable-parameterization.md)
- [TIP token-importance on-policy distillation (2026-04-16)](2026-04-16-tip-token-importance-on-policy-distillation.md)

## Source

Raw: `raw/reddit/2026-05-22-r-localllama.md` (entries on ik_llama.cpp benchmark, b9274 release, and OpenCode/Pi prompt-processing fix).
