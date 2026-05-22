# OScaR: Extreme KV Cache Quantization via Canalized Rotation + Omni-Token Scaling

**Source:** HuggingFace Daily Papers 2026-05-21 · arXiv 2605.19660 · [paper](https://arxiv.org/abs/2605.19660) · [raw](../../raw/huggingface/2026-05-21-oscar-the-occam-s-razor-for-extreme-kv-cache-quantization-in.md)
**Topic:** inference-efficiency / KV cache / quantization
**Authors:** Zunhai Su, Rui Yang, Chao Zhang, Yaxiu Liu et al. (Meituan LongCat, Tsinghua, HKU, Edinburgh, UCAS, HK PolyU)

## TL;DR

OScaR identifies Token Norm Imbalance (TNI) as the structural bottleneck of per-channel KV cache quantization at extreme bit widths, then fixes it with a two-step lightweight recipe: a Canalized Rotation that re-aligns token-level outliers into channels, then an Omni-Token Scaling pass that absorbs the residual sequence-dimensional variance. With optimized CUDA kernels, near-lossless INT2 quantization holds across text, multimodal, and omni-modal LLMs. Versus a BF16 FlashDecoding-v2 baseline, decoding accelerates up to 3.0x, memory drops 5.3x, throughput rises 4.1x.

## What is new

Per-channel quantization is the dominant per-LLM KV codec because Key tensors carry strong channel-wise outliers. At 2 bits the per-channel paradigm collapses, and the literature has responded with progressively more intricate pipelines (randomized rotations, residual error correction, mixed-precision outlier protection, TurboQuant). OScaR identifies the load-bearing failure mode the field had missed: it is not channel outliers anymore at extreme bits, it is **Token Norm Imbalance**, where tokens within the same channel group have substantial norm disparities and a shared quantization parameter cannot span them without amplifying error. The fix is structural and lightweight. Canalized Rotation re-orients the token-level outlier energy so it lines up with channels rather than splaying across token positions. Omni-Token Scaling then applies a token-axis scaling that compresses the remaining norm spread before the per-channel quantizer fires. Both passes are cheap. The CUDA kernels are tuned so the dequant overhead is amortized inside FlashDecoding.

## Why it matters

OScaR is the cleanest INT2 KV codec the wiki tracks. The Pareto front at extreme compression has been the Achilles heel of every per-channel method since per-channel quantization went mainstream, and the recent rotation codecs (TurboQuant on 2026-04-22, PolarQuant, QJL) had to load up auxiliary mechanisms to keep accuracy at sub-3-bit. OScaR's claim is that you do not need the auxiliary mechanisms once you fix TNI directly. The 3.0x decode speedup over BF16 FlashDecoding-v2 plus 5.3x memory reduction at INT2 is a strict Pareto win at every reported bit width on text-only, multimodal, and omni-modal models. Pairs naturally with OCTOPUS (today's other quantization paper, which sits in the joint-quantization branch of the rotation family) since OScaR remains in the per-channel branch.

## Research angle

The TNI diagnostic is the more transferable contribution than the recipe. Three open questions follow directly. First, does TNI show up the same way in Value tensors or only in Key tensors? Second, how does Canalized Rotation compose with TurboQuant's Walsh-Hadamard rotation? They operate on the same axis but for different purposes (TurboQuant for Beta-distribution induction, OScaR for outlier re-alignment), so they may interfere or stack. Third, the omni-modal evaluation is the first wiki paper to claim INT2 KV holds across text plus vision plus audio under one codec; the Make-Each-Token-Count composition (selective eviction + INT2 retention) is one experiment away.

## Related wiki pages

- [KV Cache concept page](kv-cache.md)
- [TurboQuant KV quantization (2026-04-22)](2026-04-22-turbo-quant-kv-cache-quantization.md)
- [OCTOPUS triplet-rotation codec (2026-05-21)](2026-05-21-octopus-octahedral-kv-cache-codec.md)
- [Make Each Token Count (2026-05-12)](2026-05-12-make-each-token-count-kv-eviction.md)
- [Mix-Quant phase-aware NVFP4 (2026-05-21)](2026-05-21-mix-quant-phase-aware-quantization.md)
