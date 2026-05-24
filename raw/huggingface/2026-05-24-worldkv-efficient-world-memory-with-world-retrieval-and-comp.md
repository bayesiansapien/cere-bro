---
source: farmer/huggingface
farmed: 2026-05-24T05:07:38.368292+00:00
arxiv_id: 2605.22718
url: https://huggingface.co/papers/2605.22718
arxiv_url: https://arxiv.org/abs/2605.22718
date: 2026-05-24
---

# WorldKV: Efficient World Memory with World Retrieval and Compression

Autoregressive video diffusion models have enabled real-time, action-conditioned world generation. However, sustaining a persistent world, where revisiting a previously seen viewpoint yields consistent content, remains an open problem. Full KV-cache attention preserves this consistency but breaks real-time constraints: memory footprint and attention cost grow linearly with rollout length. Sliding window inference restores throughput but discards long-term consistency. We propose WorldKV, a training-free framework with two components: World Retrieval and World Compression. World Retrieval stores evicted KV-cache chunks in GPU/CPU memory and selectively retrieves scene-relevant chunks via camera/ action correspondence, inserting them back into the native attention window without re-encoding. World Compression prunes redundant tokens within each chunk via key-key similarity to an anchor frame, halving per-chunk storage to fit 2x more history under a fixed budget. On Matrix-Game-2.0 and LingBot- World-Fast, WorldKV matches or exceeds full-KV memory fidelity at roughly 2x the throughput, and is competitive with memory-trained baselines without any fine-tuning. Project Page: https://cvlab-kaist.github.io/WorldKV/
