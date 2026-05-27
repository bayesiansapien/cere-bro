# MobileMoE: Scaling On-Device Mixture of Experts

**Source:** HuggingFace daily papers (2026-05-27, 4 upvotes) · arxiv 2605.27358
**arxiv:** [2605.27358](https://arxiv.org/abs/2605.27358)
**Date:** 2026-05-27
**Raw:** [raw/huggingface/2026-05-27-mobilemoe-scaling-on-device-mixture-of-experts.md](../../raw/huggingface/2026-05-27-mobilemoe-scaling-on-device-mixture-of-experts.md)
**Tier:** 1 (MoE + inference efficiency + on-device/hardware constraints)

## TL;DR

Mixture-of-experts (MoE, where each token routes through a small subset of specialized sub-networks instead of the whole model) is the default for hundred-billion-parameter LLMs, but nobody had worked out whether it helps at the sub-billion scale that fits on a phone. MobileMoE derives an on-device MoE scaling law that jointly optimizes the architecture under mobile memory *and* compute limits, and finds a sweet spot: moderate sparsity with fine-grained and shared experts is simultaneously memory- and compute-optimal. The resulting model family (0.3-0.9B active, 1.3-5.3B total) is trained with a four-stage recipe (pre-train, mid-train, instruction tuning, quantization-aware training) on open data. Across 14 benchmarks it matches or beats leading on-device dense LLMs at 2-4x fewer inference FLOPs, and matches/surpasses the SoTA OLMoE-1B-7B with up to 60% fewer parameters. With real on-device profiling at equal INT4 weight memory, MobileMoE-S runs 1.8-3.8x faster prefill and 2.2-3.4x faster decode than the dense baseline MobileLLM-Pro.

```
On-device MoE sweet spot (memory- AND compute-optimal):

  dense baseline ──► all params active every token (compute-bound on phone)
  too-sparse MoE ──► few active params, but huge total weight (memory-bound)
  MobileMoE      ──► moderate sparsity
                     + fine-grained experts (specialize)
                     + shared experts (carry common knowledge)
                     ⇒ 0.3-0.9B active / 1.3-5.3B total
                     ⇒ 1.8-3.8x prefill, 2.2-3.4x decode at equal INT4 memory
```

## Key findings

1. **An on-device MoE scaling law.** Unlike datacenter MoE scaling (which optimizes for FLOPs/quality at fixed sparsity), the mobile regime is constrained by both DRAM footprint and compute. Jointly optimizing under both yields a distinct optimum: moderate sparsity, fine-grained experts plus shared experts.
2. **2-4x fewer inference FLOPs at matched quality** vs leading on-device dense LLMs across 14 benchmarks.
3. **Up to 60% fewer parameters** than OLMoE-1B-7B at matched or better quality.
4. **Real smartphone deployment**, not just FLOP accounting: 1.8-3.8x prefill and 2.2-3.4x decode speedup over MobileLLM-Pro at equal INT4 weight memory, with the first comprehensive on-device MoE inference profiling.

## Relation to prior wiki state

This is the on-device instance of the MoE-scaling thread the wiki has been building. [MoE-muP (05-17 via Kurate, re-confirmed today on Kurate cs.LG #14, ai_rating 9.0)](../ai-routing/2026-05-17-moe-mup-maximally-scale-stable-parameterization.md) derived how to scale hyperparameters across the MoE axes (number of experts M, per-expert width Ne, sparsity K) so frontier MoEs can be tuned at small scale and trained at large. MobileMoE works the opposite end of the same axis space: instead of "tune small, train huge," it asks what the *optimal* point in (M, Ne, K) is when the hard constraint is a phone's memory and compute, not a training budget. Together they bracket MoE design: MoE-muP makes scale-up principled, MobileMoE makes scale-down principled. The "fine-grained + shared experts" finding also echoes ZeDA (05-19, post-trained MoE that skips half the experts at inference): both say the sub-network granularity is a tunable efficiency lever, not a fixed architecture choice.

## Why it matters

On-device LLMs have been a dense-model story because MoE's total-parameter footprint seemed incompatible with phone DRAM. MobileMoE shows the opposite if you pick the operating point correctly: MoE's sparsity buys back the compute that mobile NPUs can't spare, and INT4 quantization keeps the total weight in budget. If the scaling law holds, the next generation of on-device assistants (the ones that need to run offline, privately, at low battery cost) will be MoE, and the "MoE is only for datacenters" assumption dies.

## Research angle

1. **Compose with MoE-muP.** MobileMoE finds the optimum empirically via its scaling law; whether MoE-muP's closed-form hyperparameter transfer applies under the mobile memory/compute constraint is unwritten, and would let the sweet spot be predicted rather than swept.
2. **Expert-skipping at inference (ZeDA) on top of MobileMoE.** The model is already moderate-sparsity; whether further inference-time expert skipping compounds the speedup or breaks the shared-expert structure is a concrete test.
3. **NPU-specific kernels.** The profiling is on commodity smartphones; the gap between INT4 CPU/GPU inference and a dedicated mobile-NPU MoE kernel is the next efficiency frontier.

## Links

- [Paper](https://arxiv.org/abs/2605.27358)
- Raw: [raw/huggingface/2026-05-27-mobilemoe-scaling-on-device-mixture-of-experts.md](../../raw/huggingface/2026-05-27-mobilemoe-scaling-on-device-mixture-of-experts.md)
- Related: [MoE-muP](../ai-routing/2026-05-17-moe-mup-maximally-scale-stable-parameterization.md), [ZeDA 2026-05-19](2026-05-19-zeda-post-trained-moe-skip-half-experts.md), concept page [LLM routing](../ai-routing/llm-routing.md)
