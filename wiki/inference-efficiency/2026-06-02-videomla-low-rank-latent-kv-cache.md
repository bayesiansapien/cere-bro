# VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion

**Source:** HuggingFace Daily Papers · [arXiv 2605.30351](https://arxiv.org/abs/2605.30351)
**Raw:** [raw/huggingface/2026-06-02-videomla-low-rank-latent-kv-cache-for-minute-scale-autoregre.md](../../raw/huggingface/2026-06-02-videomla-low-rank-latent-kv-cache-for-minute-scale-autoregre.md)
**Date:** 2026-06-02

## TL;DR

Long-rollout causal video diffusion runs on a fixed-size sliding-window KV cache (the memory store that holds previous attention computations so they are not recomputed), and recent work has only tinkered with *which* tokens sit in the window. VideoMLA is the first paper to bring Multi-Head Latent Attention (MLA) to video diffusion: it replaces per-head keys and values with a single shared low-rank content latent plus a shared decoupled 3D-RoPE positional key, cutting per-token KV memory by 92.7% at every cached layer. It matches short-horizon baselines on VBench, scores best overall at long horizons, and improves throughput 1.23x on a single B200.

## Diagram

```
Per-head KV (baseline):   each head stores its own K,V  ─► huge streaming memory, latency-bound
VideoMLA (MLA):           shared LOW-RANK content latent  +  shared decoupled 3D-RoPE positional key
                          ─► 92.7% less per-token KV per layer ─► 1.23x throughput (B200)

Why it works (surprise):  pretrained video attention is NOT low-rank
                          (99%-energy effective rank >> latent dim)
                          BUT the MLA bottleneck — not the spectrum — sets the effective rank:
                          both spectral & random init fill the full rank budget from step 0,
                          training adapts WITHIN that budget instead of approximating the spectrum.
```

## Key points

- **MLA ported from language to video.** In LLMs, MLA (compress per-head K/V into a shared latent) is usually justified by a low-rank spectral assumption on attention. VideoMLA shows that assumption does *not* hold for pretrained video attention, yet MLA still works.
- **The mechanism is the bottleneck, not the spectrum.** The authors find both spectral and random initialization occupy nearly the full latent-rank budget from initialization, and training preserves the budget while adapting inside it. So the MLA bottleneck dimension, not the pretrained spectrum, determines effective rank. This is the paper's most interesting claim: it decouples MLA's success from the low-rank-spectrum story it is usually sold with.
- **92.7% per-token KV reduction** at every cached layer; quality retained at compression ratios where direct spectral approximation would predict large reconstruction error.
- **Results:** matches short-horizon streaming video diffusion baselines on VBench, best overall score at long horizons among evaluated methods, 1.23x throughput on a single B200.

## Relation to prior wiki knowledge

This is the latest entry in the wiki's **KV-cache-as-the-binding-constraint** thread, and it sits one layer deeper than the video-efficiency work from the day before. StateKV (2026-06-01, carries cross-frame video context in a fixed-size recurrent state to turn quadratic prefill linear, training-free) changed *how history is summarized*; Forcing-KV (2026-05-15, compresses the cache by per-head static-versus-dynamic role for video diffusion) changed *which heads keep what*; Conf-KV (2026-05-30, sets a per-step cache budget from model confidence) changed *how much budget each step gets*. VideoMLA changes the **per-head KV layout itself** — the one piece those papers left untouched — by collapsing per-head K/V into a shared latent. See [kv-cache.md](kv-cache.md).

It also contradicts a comfortable assumption the field carried over from LLM MLA: that MLA needs a low-rank attention spectrum to work. VideoMLA's finding that the bottleneck dimension (not the spectrum) sets the rank is a genuine refinement worth tracking — if it holds, MLA-style compression should transfer to other modalities whose attention is *not* low-rank.

Related: [kv-cache.md](kv-cache.md) · [attention-mechanisms.md](../llms-foundation-models/attention-mechanisms.md) · [2026-06-01-statekv-linear-video-vlm.md](2026-06-01-statekv-linear-video-vlm.md)
