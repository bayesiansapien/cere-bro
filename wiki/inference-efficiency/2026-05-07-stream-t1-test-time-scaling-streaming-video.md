# Stream-T1: Test-Time Scaling for Streaming Video Generation

**Source:** HuggingFace Daily Papers (2026-05-07)
**Paper:** [arXiv 2605.04461](https://arxiv.org/abs/2605.04461) · [HF](https://huggingface.co/papers/2605.04461)
**Raw:** [raw](../../raw/huggingface/2026-05-07-stream-t1-test-time-scaling-for-streaming-video-generation.md)

## TL;DR

Test-Time Scaling for video diffusion has been bottlenecked by exorbitant candidate exploration costs and the absence of temporal guidance. Stream-T1 argues that streaming video generation, with its chunk-level synthesis and few denoising steps, is intrinsically suited to TTS. The framework has three units: Stream-Scaled Noise Propagation (reuse high-quality previous-chunk noise as the prior for the next chunk), Stream-Scaled Reward Pruning (combine immediate spatial assessment with sliding-window long-term coherence to prune candidates), and **Stream-Scaled Memory Sinking (route KV-cache evictions through reward-feedback-guided update pathways).**

## Why it matters

The Memory Sinking component is the part that intersects this wiki's KV-cache thread. Standard KV-cache eviction in long-form streaming generation drops the oldest tokens by recency. Stream-T1 routes evictions through reward-feedback pathways instead, preserving cache slots that anchor visually important regions. This is the first paper to treat KV-cache eviction in streaming video diffusion as a **content-aware routing problem** rather than a length-based one.

## Mechanism

```
chunk_t generation:
  Stream-Scaled Noise Propagation
    ┌── prior chunk noise (passed temporal-quality gate)
    └──► seeds chunk_t initial latent

  Stream-Scaled Reward Pruning
    ┌── short-term reward (per-chunk visual)
    └── long-term reward (sliding-window temporal coherence)

  Stream-Scaled Memory Sinking
    KV-cache eviction routed by reward feedback
    high-anchor tokens preserved against recency-based eviction
```

## Connections

The Memory Sinking mechanism puts streaming video diffusion in the same conceptual frame as text-side KV-cache management ([kv-cache.md](kv-cache.md)). KV Packet (04-17) addressed cross-context reuse, TurboQuant (04-22) addressed bit-width compression, PrfaaS (04-22) addressed cross-datacenter transport. Stream-T1's Memory Sinking is the first **content-aware eviction policy** in the wiki — it asks not "which token is oldest" but "which token still anchors downstream quality."

Pairs with MotionCache (05-05) on the inference axis: MotionCache reuses denoising work where motion is low; Stream-T1 reuses noise priors and KV slots where reward feedback says they still matter. Both are heterogeneous-information-density allocators on the same modality.

Pairs with Stream-R1 (also 05-07) on the training axis: Stream-R1 reweights distillation losses by reward, Stream-T1 reweights inference-time KV retention by reward. The same pretrained-video-reward primitive is now driving both directions.

## Research angle

Whether content-aware eviction generalises beyond streaming video to long-context language inference is the obvious next step. Today's text-side KV eviction policies are still recency-based or attention-score-based. A reward-feedback eviction policy would need a cheap reward proxy at inference time, which is the same constraint speculative decoding already lives under. The two ideas have not been combined.

## Related

- [kv-cache.md](kv-cache.md)
- [2026-04-17-kv-packet-recomputation-free-kv-cache.md](2026-04-17-kv-packet-recomputation-free-kv-cache.md)
- [2026-04-22-turbo-quant-kv-cache-quantization.md](2026-04-22-turbo-quant-kv-cache-quantization.md)
- [2026-05-05-motion-aware-caching-video.md](2026-05-05-motion-aware-caching-video.md)
- [2026-05-07-stream-r1-reliability-perplexity-distillation.md](2026-05-07-stream-r1-reliability-perplexity-distillation.md)
