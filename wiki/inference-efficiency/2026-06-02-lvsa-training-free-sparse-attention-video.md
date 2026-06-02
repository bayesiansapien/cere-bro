# LVSA: Training-Free Sparse Attention for Long Video Diffusion

## TL;DR

In long-video diffusion, dense self-attention is both the compute bottleneck and a quality bottleneck. Cost grows quadratically with sequence length, and past the model's training horizon the output collapses toward a near-static, repetitive "frozen" video. Existing fixes either require expensive retraining or fail to hit both speed and quality at scale. LVSA (Long Video Sparse Attention) is a training-free, model-agnostic block-sparse attention for video diffusion transformers. Block-sparse means the attention map is computed only over selected rectangular blocks of the query-key grid rather than densely. LVSA combines a structured local window pattern with rotating global anchors, blocks of globally-attended positions that shift across diffusion timesteps so the model is not locked to a fixed grid. That rotation removes the fixed-grid bias responsible for the long-range temporal artifacts. Running on a FlashInfer block-sparse kernel, LVSA cuts compute up to 3.17x on Wan 2.1 1.3B at a 6x horizon, 2.98x on Wan 2.1 14B at a 6x horizon, and 3.33x on HunyuanVideo 1.5. It even enables HunyuanVideo 1.5 generation at a 2x horizon that is otherwise out-of-memory on one GPU, runs up to 2.71x faster on NPUs, and is quality-neutral at the training horizon and quality-positive at extended lengths under the paper's VQeval metric.

```
Video diffusion attention:
   dense full attention  ─► O(n^2) cost, "frozen"/repetitive output past training horizon
                          │ replaced (training-free, model-agnostic)
                          ▼
   ┌──────────────────────────┐   +   ┌─────────────────────────────────────┐
   │ structured LOCAL window  │       │ ROTATING global anchor blocks        │
   │ (block-sparse pattern)   │       │ (shift each diffusion step ─► no      │
   └──────────────────────────┘       │  fixed-grid bias, no temporal drift) │
                          │            └─────────────────────────────────────┘
                          ▼  run on FlashInfer block-sparse kernel
            up to 3.33x less compute, quality-positive at extended horizons
```

## Key points

- **Training-free and model-agnostic.** No retraining of the diffusion transformer; LVSA is a drop-in attention pattern, demonstrated on Wan 2.1 (1.3B and 14B), Wan 2.2 A14B, and HunyuanVideo 1.5.
- **Rotating global anchors kill the fixed-grid bias.** A structured local window plus anchors that shift each diffusion step removes the long-range temporal artifacts that cause "frozen" repetitive video beyond the training horizon. This is why LVSA is quality-positive (not just quality-neutral) at extended lengths.
- **Compute cuts:** up to 3.17x (Wan 2.1 1.3B, 6x horizon), 2.98x (Wan 2.1 14B, 6x horizon), 3.33x (HunyuanVideo 1.5) versus dense attention; up to 2.41x faster than RIFLEx and 3.27x than UltraViCo on Wan 2.1 1.3B; up to 2.71x on Wan 2.2 A14B on NPUs.
- **Memory unlock and a fairer metric.** Enables HunyuanVideo 1.5 at a 2x horizon that is otherwise out-of-memory on a single GPU. The paper introduces VQeval to score "loopy" video failures correctly, failures that VBench-Long actually rewards.

## How this relates to prior wiki pages

LVSA and [VideoMLA](2026-06-02-videomla-low-rank-latent-kv-cache.md) (same day, 2026-06-02, which collapses per-head K/V into a shared low-rank latent to cut KV memory 92.7%) are two complementary attacks on long-video efficiency: VideoMLA compresses the per-head KV *layout*, LVSA prunes the attention *pattern*. VideoMLA's modest 1.23x throughput despite a huge memory cut implied attention compute was the next bottleneck; LVSA is exactly the attention-compute lever, with up to 3.33x reduction, which is a nice closing of that loop. It also relates to [StateKV](2026-06-01-statekv-linear-video-vlm.md) (2026-06-01, fixed recurrent state for linear-time video prefill, training-free): both are training-free wrappers that change the cost of attention rather than the model, but StateKV linearizes prefill over the sequence while LVSA sparsifies the attention map block-wise. All three sit in the video-efficiency thread tracked in [kv-cache.md](kv-cache.md). The distinctive contribution is that LVSA improves quality at long horizons rather than merely preserving it, by attacking the fixed-grid bias directly.

## Gaps

VQeval is the paper's own metric, introduced to fix VBench-Long's reward of loopy failures; until it is independently validated, the "quality-positive at extended lengths" claim rests partly on a self-defined yardstick. Speedups are reported per model and horizon but the abstract does not give a single end-to-end wall-clock comparison at a fixed quality target. The rotating-anchor schedule appears tuned per setting; how sensitive quality is to the rotation rate and window size, and whether it transfers to architectures beyond Wan and HunyuanVideo, is not characterized.

**Source:** [arXiv 2605.31057](https://arxiv.org/abs/2605.31057) · raw: [raw/huggingface/2026-06-02-lvsa-training-free-sparse-attention-for-long-video-diffusion.md](../../raw/huggingface/2026-06-02-lvsa-training-free-sparse-attention-for-long-video-diffusion.md)
