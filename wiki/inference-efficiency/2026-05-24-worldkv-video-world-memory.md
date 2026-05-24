# WorldKV: Efficient World Memory with World Retrieval and Compression

**Source:** HuggingFace daily papers, [arXiv 2605.22718](https://arxiv.org/abs/2605.22718). KAIST AI, Naver AI Lab.
**Date:** 2026-05-24
**Tier:** 1 (KV cache, world models)

## TL;DR

WorldKV is a training-free framework for sustaining a persistent world in autoregressive video diffusion models. The persistence problem is concrete: revisiting a previously seen viewpoint should yield the same content. Full KV-cache attention preserves the consistency but blows up linearly with rollout length, breaking real-time constraints. Sliding-window inference restores throughput but discards long-term memory. WorldKV proposes two components: World Retrieval stores evicted KV-cache chunks in GPU or CPU memory and selectively retrieves scene-relevant chunks via camera and action correspondence, inserting them back into the native attention window without re-encoding. World Compression prunes redundant tokens within each chunk via key-key similarity to an anchor frame, halving per-chunk storage to fit 2x more history under a fixed budget. On Matrix-Game-2.0 and LingBot-World-Fast, WorldKV matches or exceeds full-KV memory fidelity at roughly 2x the throughput, and is competitive with memory-trained baselines without any fine-tuning.

## Key findings

- The KV cache in a video diffusion model is already a visual memory. Treating it as a retrievable store (instead of a forgettable buffer) is what restores persistence.
- Action and camera correspondence are cheap retrieval keys that work without learning a separate memory module. World Retrieval needs no fine-tuning.
- Key-key similarity to a per-chunk anchor frame is a strong enough redundancy signal to halve per-chunk storage. The compression is local; the retrieval is global.
- The training-free property is a deployment win. Existing world-model checkpoints (Matrix-Game-2.0, LingBot-World-Fast) gain persistence by swapping in the attention layer's cache controller.

## Why this matters

This is the third paper in three weeks tying KV-cache management to non-text modalities. The pattern: MotionCache (2026-05-05, motion-aware caching for autoregressive video generation), Stream-T1 (2026-05-07, content-aware KV eviction for streaming video with reward-feedback routing), LongLive-2.0 (2026-05-19, NVFP4 quantized KV cache for long-video training), and now WorldKV. The shared move is the same one Make-Each-Token-Count made for text (2026-05-12): the KV cache is not a passive buffer, it is the system's primary memory, and the policy that governs it is the right design surface.

For world models specifically, the alternative path (training a dedicated memory module via cross-attention or explicit 3D reconstruction) is expensive and locks the architecture. WorldKV says you can get most of the benefit by treating the existing cache as the memory, then bolt on retrieval and compression policies. This is good news for embodied AI and game-side applications where the underlying world model is upstream of the memory controller.

## Research angle

The action and camera correspondence retrieval keys are domain-specific. The open research question is what the right correspondence keys are for non-spatial agent tasks. For a long-horizon browser agent, the retrieval key is probably URL or DOM identity; for a code agent, file path and AST node identity; for a multi-step database query, query plan identity. A general framework that learns correspondence keys per task class is the next paper. WorldKV provides the architectural template.

A second question is composition with sparse-attention systems. WorldKV evicts chunks and retrieves them on demand. UniPrefill (2026-05-11, block-wise dynamic sparsification) and MISA (2026-05-11, head-axis sparse routing) prune within chunks. The two should compose: WorldKV decides which chunks live in the cache, the sparse-attention layer decides which tokens within those chunks get attended to per query. No paper yet runs this composition.

## Related

- [KV Cache](kv-cache.md) — concept page.
- [MotionCache (2026-05-05)](2026-05-05-motion-aware-caching-video.md) — motion-aware caching for AR video.
- [Stream-T1 (2026-05-07)](2026-05-07-stream-t1-test-time-scaling-streaming-video.md) — content-aware KV eviction for streaming video.
- [LongLive-2.0 (2026-05-19)](2026-05-19-longlive-2-nvfp4-parallel-infrastructure-long-video.md) — NVFP4 KV cache for long-video training.

Project page: [cvlab-kaist.github.io/WorldKV/](https://cvlab-kaist.github.io/WorldKV/).

## Raw source

[`raw/huggingface/2026-05-24-worldkv-efficient-world-memory-with-world-retrieval-and-comp.md`](../../raw/huggingface/2026-05-24-worldkv-efficient-world-memory-with-world-retrieval-and-comp.md)
