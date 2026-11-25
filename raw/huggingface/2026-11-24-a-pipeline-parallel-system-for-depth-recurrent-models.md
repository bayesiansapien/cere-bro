---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.925985+00:00
arxiv_id: 2611.30581
url: https://huggingface.co/papers/2611.30581
arxiv_url: https://arxiv.org/abs/2611.30581
date: 2026-11-24
---

# A Pipeline-Parallel System for Depth-Recurrent Models

Depth-recurrent (Looped) models raise effective depth by applying a shared stack of blocks several times. Scaling them usually requires pipeline parallelism, but commonly used interleaved 1F1B is drawn for an acyclic stage graph in which each micro-batch enters each stage once. Once that stack is split across stages, the same stage is visited several times on one micro-batch and later stages feed earlier ones: native 1F1B has no slot for the extra visit, cannot rank a first iteration against a second, and its neighbour-only send/receive order has no back edge to the first stage, so the arrangement stalls or fires out of order. We present Loop-PP, which rebuilds both the timetable and the communication for this cyclic layout. It schedules different iterations of the same stage separately, specializes a 1F1B skeleton into a globally consistent order over those visits, and emits a static instruction stream per rank that separates posting from waiting so communication overlaps local compute. Loop-PP is bit-identical to a single-stage reference. On 8B-60B MoE models, it lowers peak memory by as much as 32.8\%, and with compute budget fixed, the best observed throughput rises by 12.7\%.
