# Asynchronous Continuous Batching: CPU-GPU Overlap via Dual Buffer Slots

**Source:** [HuggingFace blog](https://huggingface.co/blog/continuous_async)
**Date ingested:** 2026-05-15 (post dated 2026-05-14)
**Tier:** 1. GPU optimization, continuous batching, inference throughput
**Raw:** [farmer file](../../raw/rss/2026-05-14-huggingface-blog-unlocking-asynchronicity-in-continuous-batching.md)

## TL;DR

Continuous batching tightly packs requests into batches and eliminates padding waste. But the CPU and GPU still alternate: while the CPU updates request state and schedules the next batch, the GPU idles, and vice versa. On an 8B model at batch size 32 for 8K-token generation, the CPU-side gap costs about 24% of total runtime. The HuggingFace `transformers` continuous-batching implementation now ships an asynchronous version that uses three CUDA streams (H2D, compute, D2H), CUDA events for ordered handoff, and two parallel input/output buffer slots (A and B) so the CPU can prepare batch N+1 while the GPU computes batch N. GPU utilization rises from 76.0% to 99.4%; generation wall time drops from 300.6s to 234.5s, a 22% speedup. No new kernels, no model changes, pure scheduling.

## What's new

Three primitives stitched together.

**Three CUDA streams.** The default stream synchronizes on every operation. The async implementation explicitly opens a Host-to-Device stream, a compute stream, and a Device-to-Host stream. Each stream returns control to the CPU immediately, so the CPU can keep working while the GPU runs.

**CUDA events for handoff.** A naive multi-stream design can race. The fix is event-based ordering: `h2d_stream.record(h2d_done)` marks the H2D transfer complete, `compute_stream.wait(h2d_done)` makes compute wait for that event, and `d2h_stream.wait(compute_done)` blocks output retrieval until compute finishes. The CPU never blocks on the GPU; events keep the order correct.

**Two buffer slots (A and B).** Without dual buffers, the CPU would have to write into the same tensors the GPU is reading from, racing on every batch. With slots A and B, the CPU writes batch N+1 into slot B while the GPU reads batch N from slot A; on the next step they swap. A carry-over mask transfers freshly generated tokens from batch N's output to batch N+1's input via tensor ops, using placeholder zeros initially populated as the GPU finishes.

**CUDA graph memory pool.** Multiple captured graphs share one memory pool to avoid duplicating VRAM for both slots.

## Why this is Tier 1

This is the production-inference complement to the architectural papers landing this week. Where [Forcing-KV](2026-05-15-forcing-kv-video-diffusion-kv-cache-compression.md) compresses the cache and [Orthrus](2026-05-14-orthrus-dual-view-diffusion-ar.md) reuses it across two heads, async continuous batching is the scheduling layer underneath. Continuous batching has been the production-inference workhorse since 2023; adding async CPU-GPU overlap on top is the next step on the same axis.

The 22% number is close to the 24% theoretical ceiling (eliminating CPU overhead entirely). That gap is the few unavoidable synchronization points where the CPU has to block to sample outputs. There is no obvious further compression on this dimension without either GPU-side sampling or paged-out CPU work.

## Connections to prior wiki pages

- [Make Each Token Count](2026-05-12-make-each-token-count-kv-eviction.md) — eviction is policy-aware; async continuous batching is scheduling-aware. Both layers compose without conflict.
- [Speculative decoding for RL rollouts](2026-04-30-speculative-decoding-rl-rollouts.md) — used continuous batching as the substrate. Async overlap would compose multiplicatively with the 1.77x speculative-decoding speedup.
- [Energy-to-Token position paper](../hardware/2026-05-14-energy-to-token-position-paper.md) — argued that the binding constraint moves toward energy. Async batching is the cleanest energy-efficiency win on this stack: 99.4% utilization means the GPU is working when it's powered, which directly converts power draw into useful tokens.
- [PreFaaS cross-datacenter prefill](2026-04-22-prfaas-cross-datacenter-prefill.md) — the cross-DC complement on the prefill axis. Both are scheduling-side optimizations that change the substrate without touching the model.
- [gpu-kernels.md](../hardware/gpu-kernels.md) — concept page should add "asynchronous batching" to the throughput-optimization taxonomy.

## Cross-source signal

The HuggingFace blog drops the same week as r/LocalLLaMA's TurboQuant practitioner study and NVIDIA's NVFP4 Kimi-K2.6 release. Three pieces of the inference stack updating in one week: scheduling (async batching), quantization (NVFP4, TurboQuant), and head-role cache compression (Forcing-KV). None of them are model changes. All of them are deployable today.

## Research angle

1. **Async batching for RL rollouts.** The 16K+ generation lengths the post mentions are exactly the RL post-training regime. NeMo-RL speculative rollouts could compose with async continuous batching for 2x+ wall-clock training improvements on the rollout phase, which is typically 60-70% of RL training cost.
2. **Async batching with paged attention.** vLLM uses paged attention plus continuous batching. The TGI vs vLLM vs transformers split now diverges on the async axis. Whether vLLM adopts async continuous batching is the watch.
3. **GPU-side sampling.** The residual 2-percentage-point gap to theoretical ceiling is the CPU-side sampling step. Moving sampling onto the GPU eliminates the last sync point.

## Why it matters

Continuous batching was a 2023 production workhorse. Two years later, the scheduling primitive has gotten one structural upgrade (async overlap) that returns 22% with no model or kernel changes. The lesson is the same as the cache thread: the substrate has more headroom than the architecture papers suggest.

## Links

- [Blog post](https://huggingface.co/blog/continuous_async)
- [Raw farmer file](../../raw/rss/2026-05-14-huggingface-blog-unlocking-asynchronicity-in-continuous-batching.md)
- Related: [gpu-kernels.md](../hardware/gpu-kernels.md), [Orthrus](2026-05-14-orthrus-dual-view-diffusion-ar.md), [Energy-to-Token](../hardware/2026-05-14-energy-to-token-position-paper.md)
