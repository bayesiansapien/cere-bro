# Lighthouse Attention: Long-Context Pre-Training as a Detachable Wrapper

**Source:** HuggingFace Daily Papers · [arXiv 2605.06554](https://arxiv.org/abs/2605.06554) · [Code](https://github.com/ighoshsubho/lighthouse-attention)
**Raw:** [farmer file](../../raw/huggingface/2026-05-16-long-context-pre-training-with-lighthouse-attention.md)
**Authors:** Bowen Peng, Subho Ghosh, Jeffrey Quesnelle (Nous Research)
**Tier:** 1 — long-context, GPU efficiency, kernel-decoupled attention

## TL;DR

Lighthouse Attention is a training-only, kernel-decoupled wrapper around ordinary scaled dot-product attention (SDPA) for pre-training causal transformers at extreme context length. Queries, keys, and values are pooled **symmetrically** into a multi-resolution pyramid; a small score per pyramid head drives a top-k cascade that selects a hierarchical dense sub-sequence; a sorting pass keeps it left-to-right causal. The selection is gradient-free, so the backward pass is just ordinary FlashAttention on a shorter sequence. After the bulk of pre-training, a short recovery phase removes the wrapper and the model returns to full attention. Nous's own announcement claims 1.4-1.7x wall-clock speedup at 98K context and ~17x forward+backward speedup at 512K on a single B200, without a custom sparse kernel, a straight-through estimator, or an auxiliary loss.

## Why it matters

Three months ago the long-context pre-training conversation was either "swap softmax for a fixed-size state" (linear attention, SSM, log-linear) or "build a custom sparse kernel" (MoBA, Native Sparse Attention, DSA). Lighthouse takes neither path. It treats sparse attention as a pre-processing step that the standard dense-attention kernel still gets to consume, then it gets out of the way before the model is delivered. The result is the same final architecture downstream consumers expect (full attention), the same kernels the GPU vendor is optimizing for (FlashAttention on Hopper / Blackwell), and a training cost that scales subquadratically.

The symmetrical pooling is the deeper move. Earlier selective-attention work pooled keys and values but kept queries at full resolution, which made the cache an addressable memory rather than a true multi-resolution representation. Lighthouse pools all three. Hierarchical structure shows up in queries themselves, which is what makes the gradient-free top-k cascade learn something more than a memory index.

## Connections to prior wiki state

- **Subquadratic Appen-validated benchmark** (Gmail-starred 2026-05-15, [digest](../daily-digest/2026-05/2026-05-15.md)) — Subquadratic shipped a 56.2x speedup vs FlashAttention-2 at 1M tokens with 81.8% SWE-bench Verified. That was a deployment-side number on a proprietary architecture. Lighthouse is the open-source training-side counterpart: same week, same axis, two different research groups. The "subquadratic-train, dense-deploy" thread the wiki started tracking on 2026-05-12 now has its first published recipe.
- **Forcing-KV head-role compression** ([2026-05-15](2026-05-15-forcing-kv-video-diffusion-kv-cache-compression.md)) and **async continuous batching** ([2026-05-15](2026-05-15-async-continuous-batching-cpu-gpu-overlap.md)). Three pieces of the inference / training stack this week (Lighthouse training, Forcing-KV cache compression, async batching scheduling) that all leave the model architecture unchanged. The pattern from yesterday's digest continues: efficiency gains are coming from substrate rewrites, not new models.
- **Make Each Token Count** ([2026-05-12](2026-05-12-make-each-token-count-kv-eviction.md)) framed the KV cache as a programmable substrate. Lighthouse extends the same framing one layer back: the pre-training-time attention selection is a programmable substrate too. Gradient-free top-k is the simplest such program.
- **DLR** ([2026-05-15](../ai-routing/2026-05-15-dlr-dynamic-latent-routing-post-training.md)) made routing a training-time concern via learned discrete codes. Lighthouse makes attention sparsity a training-time concern via gradient-free hierarchical selection. Training-time substrate design is becoming its own subfield.

## How it works

The training run is split in two stages. For the bulk of pre-training, every attention layer runs Lighthouse. Queries, keys, and values are pooled symmetrically along the sequence axis into a small multi-resolution pyramid. A cheap scorer evaluates each pyramid head; the top-k cascade picks a hierarchical dense sub-sequence; a sort pass restores left-to-right order so causality is preserved. The selected sub-sequence is then fed through ordinary FlashAttention. Because selection is gradient-free, the backward pass does not need to differentiate through top-k. There is no auxiliary loss; the model only sees a slightly weird attention pattern.

For the final short phase, Lighthouse is removed and the model trains briefly with full attention. The published claim is that this recovery is fast and the final dense-attention loss is lower than dense-attention training matched on tokens.

## Open problems / Research angle

- **Recovery-phase scaling.** The preliminary experiments are small-scale. Whether the short recovery phase produces a competent dense model at 1B+ params is the obvious follow-up. If it doesn't, this becomes a long-context-only method rather than a general pre-training tool.
- **Composition with bounded-size state hybrids.** SANA-WM (2026-05-15) showed that hybrid linear attention + softmax can work for video. Lighthouse + Mamba-style state in alternating layers is an obvious composition; nobody has tried it.
- **Lighthouse for fine-tuning.** Lighthouse is described as a pre-training method, but the same wrapper applied to long-context SFT or RL fine-tuning is the higher-leverage deployment. Falsifiable: a follow-up paper reporting on 128K-context fine-tuning with Lighthouse achieving full-attention quality at sub-half compute.
- **Top-k cascade interpretability.** Each pyramid head selection is a routing decision the model implicitly learned. Whether those decisions correlate with content (entities, document boundaries, syntax phases) is open. If yes, Lighthouse becomes a self-supervised structural prior for free.

## Concept tags

`long-context-pretraining` · `subquadratic-attention` · `kernel-decoupled` · `hierarchical-selection` · `nous-research`
