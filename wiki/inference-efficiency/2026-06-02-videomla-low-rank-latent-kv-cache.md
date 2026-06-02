# VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion

## TL;DR

Long-rollout causal video diffusion has settled on a fixed-size sliding-window KV cache (the memory store that holds previous attention keys and values so they are not recomputed each step). Recent work only changed which tokens sit in that window or how their positions are encoded, while leaving the per-head KV layout, a dominant driver of streaming memory and latency, untouched. VideoMLA is the first study of Multi-Head Latent Attention (MLA, where the per-head keys and values are replaced by a single shared compressed latent that each head up-projects from) in video diffusion. It swaps per-head keys and values for one shared low-rank content latent plus one shared decoupled 3D-RoPE positional key, cutting per-token KV memory by 92.7% at every cached layer. The surprise is that MLA works here even though the low-rank attention spectrum that motivates it in language models does not hold: pretrained video attention is not low-rank, with 99%-energy effective rank far above any practical latent size. VideoMLA shows the MLA bottleneck dimension, not the pretrained spectrum, sets the effective rank. On VBench it matches short-horizon streaming baselines, scores best overall at long horizons among evaluated methods, and lifts throughput 1.23x on a single B200.

```
Baseline per-head KV:   head_1[K,V]  head_2[K,V] ... head_h[K,V]   ► large per-token KV, latency-bound
                                       │ replaced by
                                       ▼
VideoMLA per layer:     ┌──────────────────────────┐  ┌─────────────────────────┐
  stored ONCE per layer │ shared low-rank content  │  │ shared decoupled 3D-RoPE │
                        │   latent (small dim)     │  │   positional key         │
                        └────────────┬─────────────┘  └────────────┬────────────┘
  attention up-projects ─────────────┴──────────────► per-head K/V on the fly
  sliding-window cache holds the LATENTS (not per-head K/V)  ► 92.7% less KV/layer
```

## Key points

- **First MLA study in video diffusion.** Replaces per-head K/V with a shared low-rank content latent plus a shared decoupled 3D-RoPE positional key, stored once per layer; per-token KV memory drops 92.7% at every cached layer.
- **MLA succeeds despite a non-low-rank spectrum.** Pretrained video attention is not low-rank (99%-energy effective rank far above any practical latent dimension), yet quality holds at compression ratios where a direct spectral approximation would predict large reconstruction error.
- **The bottleneck, not the spectrum, sets effective rank.** Both spectral and random initialization fill nearly the full latent-rank budget from step zero, and training preserves that budget while adapting within it. So the latent bottleneck dimension determines effective rank, decoupling MLA's success from the spectral story it is usually sold with.
- **Results:** matches short-horizon streaming video diffusion baselines on VBench, best overall score at long horizons among evaluated methods, 1.23x throughput on a single B200. The modest throughput gain despite a 92.7% memory cut signals that compute, not memory, is now the binding constraint.

## How this relates to prior wiki pages

VideoMLA attacks the same video KV bottleneck as [StateKV](2026-06-01-statekv-linear-video-vlm.md) (2026-06-01, which carries cross-frame video context in a fixed-capacity recurrent state to turn quadratic prefill into linear time, training-free) but from a different angle. StateKV changes *how history is summarized over the sequence*; VideoMLA changes *what each head stores per token*, the per-head layout that the sequence-length line of work left alone. It is the per-head-layout entry in the broader KV-cache thread tracked in [kv-cache.md](kv-cache.md), which already logs eviction-by-token, eviction-by-head, and eviction-by-step budget; VideoMLA goes one layer underneath all of them. The page also contradicts a comfortable assumption imported from LLM MLA, that MLA needs a low-rank attention spectrum to work, and replaces it with the bottleneck-dimension explanation. One concrete signal worth carrying forward: 1.23x throughput off a 92.7% memory cut means the streaming bottleneck has shifted from KV memory bandwidth to attention compute, so the next video-efficiency win likely comes from sparser or cheaper attention, not more cache compression.

## Gaps

The 1.23x throughput, modest against the 92.7% memory reduction, hints the kernel or attention compute is now the bottleneck, but the paper does not profile where the remaining time goes. The bottleneck-not-spectrum claim is supported by initialization and training-budget analysis on the evaluated models; whether it holds across video architectures with very different attention shapes is not established. VBench "best overall at long horizons" is reported among evaluated methods only, so the comparison set's coverage matters and is not fully characterized in the abstract.

**Source:** [arXiv 2605.30351](https://arxiv.org/abs/2605.30351) · raw: [raw/huggingface/2026-06-02-videomla-low-rank-latent-kv-cache-for-minute-scale-autoregre.md](../../raw/huggingface/2026-06-02-videomla-low-rank-latent-kv-cache-for-minute-scale-autoregre.md)
