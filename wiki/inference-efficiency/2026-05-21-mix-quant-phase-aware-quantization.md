# Mix-Quant: Phase-Aware NVFP4 for Agentic LLM Prefill, BF16 for Decoding

**Source:** HuggingFace Daily Papers 2026-05-21 · arXiv 2605.20315 · [paper](https://arxiv.org/abs/2605.20315) · [raw](../../raw/huggingface/2026-05-21-mix-quant-quantized-prefilling-precise-decoding-for-agentic.md)
**Topic:** inference-efficiency / quantization / agentic systems
**Authors:** Haiquan Lu, Zigeng Chen, Gongfan Fang, Xinyin Ma, Xinchao Wang (National University of Singapore)

## TL;DR

Mix-Quant is a phase-aware quantization recipe for agentic LLMs that splits precision across the prefill-versus-decode boundary: high-throughput NVFP4 for the compute-intensive prefilling stage, BF16 preserved for the autoregressive decoding stage. The motivation comes from a direct measurement: prefill exhibits substantial quantization redundancy in agentic workloads (long inputs, repeated tool returns and memory retrievals), while decoding is error-sensitive because errors compound across the autoregressive trajectory. Up to 3x speedup during prefilling, task accuracy largely preserved across long-context and agentic benchmarks.

## What is new

The dominant production pattern (W4A4, GPTQ, AWQ) applies a uniform quantization across the inference pipeline. For chatbot-style serving where decode dominates the latency budget, that pattern is reasonable. For agentic LLMs it is wrong on both axes: the input context grows fast because each step appends tool outputs, retrievals, intermediate reasoning, and execution traces, so prefill becomes the dominant compute and the dominant source of latency. But agentic trajectories are also long, so quantization error in decode compounds across many tokens. Mix-Quant decouples the two: NVFP4 on prefill exploits the Blackwell tensor-core throughput while accepting the small quality hit (which the prefill stage is empirically robust to), and BF16 on decode preserves the precision the autoregressive trajectory needs. This is the algorithmic analog of the prefill-decode disaggregation pattern that Splitwise and DistServe established at the system level, but it lives inside a single GPU rather than across cluster boundaries.

## Why it matters

Agentic LLM inference is the production frontier that has been growing fastest: Cursor's Composer 2.5 economics on CursorBench 3.1 land at $0.55 per task vs Opus 4.7 Max at $11.02 (2026-05-20 digest), and that gap is dominated by prefill cost on long inputs. A 3x prefill speedup at preserved task accuracy is a direct production lever, and the algorithm-level move (rather than system-level disaggregation) means it composes with existing serving stacks. The Blackwell-native NVFP4 path is the same fabric LongLive-2.0 (2026-05-19) used end-to-end for video; this is the first text-LLM phase-aware NVFP4 deployment in the wiki.

## Research angle

Mix-Quant raises the right question for agentic inference economics: which stages tolerate which bit widths under which workload shapes? Three threads to track. First, the prefill-NVFP4 / decode-BF16 split is the simplest version; a finer-grained schedule (NVFP4 prefill, INT4 KV cache via OScaR or OCTOPUS, BF16 decode for the active token stream) is the natural composition and the diagnostic is whether the compound speedup multiplies or saturates on memory bandwidth. Second, the "decoding quality matters more than prefill quality" claim is workload-specific; whether it holds on reasoning agents (where decode is the actual reasoning work) versus tool-use agents (where decode is more often short responses) needs separate measurement. Third, the NVFP4 prefill path opens space for prefill-only sparse attention (UniPrefill on 2026-05-11 ships as a vLLM operator); the combination should compound.

## Related wiki pages

- [KV Cache concept page](kv-cache.md)
- [OScaR INT2 KV codec (2026-05-21)](2026-05-21-oscar-extreme-kv-cache-quantization.md)
- [OCTOPUS triplet codec (2026-05-21)](2026-05-21-octopus-octahedral-kv-cache-codec.md)
- [LongLive-2.0 NVFP4 video stack (2026-05-19)](2026-05-19-longlive-2-nvfp4-parallel-infrastructure-long-video.md)
- [UniPrefill (2026-05-11)](2026-05-11-uniprefill-universal-prefill-acceleration.md)
