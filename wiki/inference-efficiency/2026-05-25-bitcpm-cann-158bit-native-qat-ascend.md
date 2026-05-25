# BitCPM-CANN: native 1.58-bit QAT on Huawei Ascend NPUs

**Source:** r/LocalLLaMA, [Reddit post](https://www.reddit.com/r/LocalLLaMA/comments/1tmf63y/bitcpmcann_native_158bit_large_language_model/) · [Paper PDF](https://github.com/OpenBMB/MiniCPM/blob/main/docs/BitCPM_CANN.pdf)
**Raw:** [farmed](../../raw/reddit/2026-05-25-r-localllama.md)

## TL;DR

BitCPM-CANN is the first end-to-end 1.58-bit (ternary) quantization-aware training pipeline running natively outside the CUDA ecosystem. The team at OpenBMB ported their MiniCPM-aligned ternary QAT pipeline to Huawei's CANN, MindSpeed, and Megatron-LM stack and trained four models (0.5B, 1B, 3B, 8B) aligned in architecture and pre-training data with full-precision MiniCPM4 counterparts. Across 11 benchmarks the 1B, 3B, 8B variants retain 95.7-97.2% of full-precision performance; the 3B variant achieves parity on BBH and the 3B/8B variants recover nearly all of GSM8K. The 0.5B variant retains 90.1%, with the residual gap concentrated on math — capacity, not the quantizer, is the bottleneck at sub-billion scales. The QAT integration adds only 4.5% training-throughput overhead (148 vs 155 TFLOP/s per NPU), making ternary training viable as a *default* configuration, with up to 8x weight memory reduction at inference (about 6x end-to-end including scaling factors).

## Why this matters

Two separate results matter, and they support each other.

**Result 1: ternary capability retention at the right scale.** The 1B and above variants retain ~96% of full precision on real benchmarks. The 0.5B variant retains 90%. The gap concentrates on math, which is the capacity-bound axis. The implication is that ternary representation is not the bottleneck for capability above a billion parameters. Capacity is. That is the cleanest empirical claim about extreme low-bit training to date.

**Result 2: 4.5% training overhead.** Ternary QAT has historically added 20-40% training overhead, which is the reason it stays a research artifact rather than a default. 4.5% is small enough that the only remaining reason to use full-precision pretraining is inertia. Combined with 8x inference-weight memory reduction, the deployment economics tilt decisively toward ternary.

**Result 3: outside CUDA.** This is the first 1.58-bit native pipeline on Ascend NPUs. Up to now, every credible extreme-low-bit result was on NVIDIA hardware. Huawei now has a credible native quantization story. For the geopolitical inference stack (Chinese labs forbidden from H100/H200/B200) this matters: a domestic-silicon QAT pipeline that delivers 96% retention at 4.5% training overhead is the practical fallback that the export-control regime was assumed to make hard.

## Where this fits

The compression / quantization concept page has been tracking 1-bit / 2-bit / ternary work for months. Until today the open question was whether sub-2-bit training was production-ready outside research clusters. BitCPM-CANN is the answer: yes, at modest training overhead, with capability retention that scales with parameter count. Combined with the OSCAR (extreme KV cache quantization) and Octopus (octahedral KV cache codec) papers from 2026-05-21, the inference stack now has both extreme weight quantization and extreme KV quantization landing in the same window.

## Open research angles

- 1.58-bit retains 96% at 1B-8B scale. Whether the gap stays at 4% at 30B+ is unproven and is the next compute-budget test.
- The 4.5% training overhead is measured on Ascend NPUs. Whether the analogous overhead on H100s is comparable would help calibrate cross-vendor expectations.
- The 0.5B math gap is the cleanest test of "capacity, not quantizer" — increasing the parameter budget should close the gap if the framing is right.

## Industrial implication

Local LLM stacks (LM Studio, llama.cpp, ollama) are the natural deployment target. 8x weight memory reduction means a 70B model fits in 24GB. For consumer hardware (RTX 5090, Apple Silicon, Strix Halo) this is the single biggest accessibility win of 2026. For Huawei specifically, this provides a sovereign-silicon training path that the export-control regime cannot disrupt.

## Related wiki pages

- [2026-05-21-oscar-extreme-kv-cache-quantization.md](2026-05-21-oscar-extreme-kv-cache-quantization.md)
- [2026-05-21-octopus-octahedral-kv-cache-codec.md](2026-05-21-octopus-octahedral-kv-cache-codec.md)
