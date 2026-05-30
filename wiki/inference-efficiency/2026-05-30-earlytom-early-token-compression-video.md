# EarlyTom: Early Token Compression Inside the Vision Encoder

**Source:** HuggingFace Daily Papers (2026-05-30) · arxiv 2605.30010
**Raw:** [raw/huggingface/2026-05-30-earlytom-early-token-compression-completes-fast-video-unders.md](../../raw/huggingface/2026-05-30-earlytom-early-token-compression-completes-fast-video-unders.md)

## TL;DR

Most token-compression work on video LLMs prunes tokens late, after the vision encoder has already produced its full output. EarlyTom shows the vision encoder itself contributes a large share of time-to-first-token (TTFT) on video tasks, and proposes a training-free compression scheme that runs *inside* the encoder. Combined with a decoupled spatial-token-selection strategy, it cuts TTFT by up to 2.65x and FLOPs by 61% on LLaVA-OneVision-7B at a single A100, with accuracy comparable to the full-token baseline. The takeaway: the vision encoder is no longer a fixed-cost upstream stage; it is an addressable optimization surface.

## Where the compression happens

```
Prior work (late compression):

  video frames ─► [VISION ENCODER (full cost)] ─► all tokens ─► [PRUNE LATE] ─► LLM
                          ^^ untouched ^^             ↑
                                                 most prior work

EarlyTom (early compression inside the encoder):

  video frames ─► [VISION ENCODER (compressed)] ─► fewer tokens ─► LLM
                          ▲▲▲▲▲▲▲▲▲▲▲▲▲▲
                  in-encoder compression
                  + decoupled spatial token selection
                  = 2.65x TTFT, 61% FLOPs cut, comparable accuracy
```

## Key claims

- TTFT reduction up to **2.65x** on LLaVA-OneVision-7B at a single A100.
- FLOPs reduction up to **61%**.
- Accuracy comparable to full-token baselines (paper reports across video understanding benchmarks).
- Training-free; no encoder fine-tuning required.

## Why this matters

The wiki has tracked late-stage video token compression since MotionCache (2026-05-05) and Stream-T1 (2026-05-07), both of which operate on the *output* of the vision encoder. EarlyTom is the first paper in the wiki to reframe the vision encoder itself as a primary cost source rather than fixed overhead. Combined with WorldKV (2026-05-24, scene-conditioned retrieval of evicted chunks) and Forcing-KV (2026-05-15, role-conditioned head pruning), the video-side efficiency stack now has compression at every stage: in-encoder (EarlyTom), at the cache (WorldKV, Forcing-KV), and at the LLM input (Stream-T1, MotionCache).

## Gaps and limits

- Only LLaVA-OneVision-7B characterized at length. Behavior on larger video VLMs or 30B+ models is not reported.
- A100-only timing. Blackwell timing not reported (matters because in-encoder compression interacts with how the encoder uses tensor cores).
- "Comparable accuracy" is the published claim; the threshold for *comparable* and the tail behavior at adversarial long-form video are not shown.

## Research angle

The EarlyTom move (move compression upstream into a module previously treated as fixed) is the same move the wiki has seen on the LLM side: Make-Each-Token-Count moved eviction from late-stage pruning to a learned-per-token decision; Forcing-KV moved compression from a global policy to a per-head-role policy. The pattern says: every fixed-cost preprocessing stage in the inference pipeline is being reframed as an optimization surface. The next question is whether the entire video stack can be jointly optimized end-to-end (frame sampling → in-encoder compression → KV eviction → LLM-side pruning) rather than via stacked independent passes.

## Related concept pages

- [KV Cache](kv-cache.md)
- [Knowledge distillation](knowledge-distillation.md)
