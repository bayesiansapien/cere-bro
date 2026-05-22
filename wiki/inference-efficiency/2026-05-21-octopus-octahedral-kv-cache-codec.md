# OCTOPUS: Joint Triplet Quantization for KV Cache via Octahedral Parametrization

**Source:** HuggingFace Daily Papers 2026-05-21 · arXiv 2605.21226 · [paper](https://arxiv.org/abs/2605.21226) · [raw](../../raw/huggingface/2026-05-21-octopus-optimized-kv-cache-for-transformers-via-octahedral-p.md)
**Topic:** inference-efficiency / KV cache / quantization
**Authors:** Mark Boss, Vikram Voleti, Simon Donné, Shimon Vainer (Stability AI)

## TL;DR

OCTOPUS advances the rotation-preconditioned quantization family (TurboQuant, PolarQuant, QJL) by quantizing rotated coordinates as triplets rather than one at a time. Each triplet's direction is mapped to a square via an octahedral parametrization, then the two square coordinates plus the triplet norm are Lloyd-Max quantized against implementation-matched marginals. The bit allocation is strictly non-uniform and depends only on key dimensionality, and a fused Triton kernel reconstructs keys on the fly without materializing the uncompressed tensor. Across text, video, and audio, OCTOPUS matches or beats every prior rotation codec at every reported bit width, with the lead widening at extreme low-bit.

## What is new

The rotation-codec family compresses Keys in three steps: a structured random rotation that makes per-coordinate marginals tractable, then a per-coordinate Lloyd-Max quantizer, then an unbiased dot-product reconstruction. TurboQuant uses a symmetric Beta marginal, PolarQuant works on polar angles, QJL adds a 1-bit residual. The shared limitation: each coordinate (or each polar angle) is quantized independently, so the spectral structure across small sub-blocks of rotated coordinates is not exploited. OCTOPUS observes that after a Walsh-Hadamard rotation, the norm of a small sub-block of coordinates carries asymptotically less entropy as channel count grows. Quantizing a triplet's direction separately from its norm therefore lets a non-uniform bit allocation between direction and norm achieve lower MSE at the same total bit rate. The direction lives on S^2; the octahedral map gives an equal-area parametrization that turns S^2 into a square [-1,1]^2 with O(1) arithmetic and near-uniform Jacobian. The triplet's two square coordinates plus the norm are then Lloyd-Max quantized against implementation-matched marginals (not the asymptotic ones, the actual ones the implementation produces).

## Why it matters

OCTOPUS is the second KV codec landing today (alongside OScaR) that pushes the Pareto front at extreme low-bit. They sit in different sub-branches of the rotation family: OScaR stays per-channel and fixes Token Norm Imbalance directly, OCTOPUS goes joint-quantization on rotated triplets and exploits the entropy distribution across coordinates. Both publish near-lossless extreme compression with optimized kernels. The fused Triton implementation matters: it reconstructs keys on the fly without ever materializing the uncompressed tensor, so the codec adds no decode-time bandwidth or latency above the dequantization step the model already pays.

## Research angle

The "data-oblivious, online, deterministic given a seed" framing is the deployment-relevant claim: OCTOPUS does not require a calibration set or per-model tuning, which removes the operational friction every prior rotation codec carries into production. Two open questions follow. First, does the entropy advantage of triplet over coordinate scale beyond text, video, and audio Keys? Triplets are dimensionality-specific; whether higher-order joints (quadruplets, n-tuples) give monotone gains, or whether triplets sit at a sweet spot, is empirically open. Second, OCTOPUS is data-oblivious by design, but production KV streams have head-specific and layer-specific statistics. A per-head conditional variant could combine OCTOPUS's joint-coordinate structure with head-role compression (Forcing-KV on 2026-05-15 found static vs dynamic head clusters; both could plausibly use OCTOPUS with head-specific bit budgets).

## Related wiki pages

- [KV Cache concept page](kv-cache.md)
- [OScaR INT2 KV codec (2026-05-21)](2026-05-21-oscar-extreme-kv-cache-quantization.md)
- [TurboQuant (2026-04-22)](2026-04-22-turbo-quant-kv-cache-quantization.md)
- [Forcing-KV head-role compression (2026-05-15)](2026-05-15-forcing-kv-video-diffusion-kv-cache-compression.md)
