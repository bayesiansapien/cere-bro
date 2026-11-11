---
title: "Efficiency shorts 2026-11-11: e-means, onóna, SD-ViT early exit, PhysioWave-T, Sugar Glider, hybrid-attention census, NVIDIA Snapshot"
date: 2026-11-11
source: https://arxiv.org/abs/2611.09501
raw: ../../raw/huggingface/
tags: [clustering, embeddings, early-exit, tokenization, long-context, cold-start]
signal: HuggingFace Daily Papers 11-10; X Following feed; NVIDIA Developer blog
---

# Efficiency shorts

- **e-means** ([2611.09501](https://arxiv.org/abs/2611.09501)). Mini-batch k-means with an exponential moving average update, plus scaling laws that set the decay rate and batch size by formula, so no hyperparameter sweep. Beats Lloyd's k-means loss at 25 epochs in 1.4 to 2.6 epochs, 10-45x GPU wall-clock speedups over state-of-the-art implementations, often beating k-means++. Partitioned 10B DINO embeddings into 16M clusters in 2.5 epochs. Reported shipped in FAISS (@BoWang87). Relevance: k-means is the inner loop of vector quantization, product-quantized KV caches and data curation.
- **onóna** ([2611.10556](https://arxiv.org/abs/2611.10556)). Two embedding tables whose average is the input and whose two softmaxes, mixed by a gate that depends only on the current token, form the output head. Keeps weight tying, costs one extra table and projection, and the gate can be precomputed. Lower loss in 11 of 12 comparisons at 142M to 1B across dense, Gated DeltaNet hybrid, MoE and Attention Residual models; the exception is the 1B MoE.
- **SD-ViT** ([2611.09987](https://arxiv.org/abs/2611.09987)). Stochastic deep supervision through a shared head makes every ViT block a usable exit for face recognition. Early exits keep over 96% of full-depth performance at 50% compute, against an unchanged full-depth gallery. Generalizable lesson: train intermediate layers into the final embedding space and early exit needs no re-indexing.
- **PhysioWave-T** ([2611.08969](https://arxiv.org/abs/2611.08969)). Folds J+1 wavelet subbands before tokenizing, cutting sequence length by (J+1)x for EEG/ECG/sEMG. 4.0-7.2x lower Transformer latency and 6.8-12.7x lower peak memory, no accuracy loss. Token-count compression at the input, the cheapest place to do it.
- **Sugar Glider** (i14 Labs, via @omarsar0). An architecture family with a fixed-size KV cache as context grows; claims up to 32x more requests per server at 1M tokens, cache size chosen at deploy time. Vendor numbers, no paper yet.
- **Full attention is leaving open models** (Sebastian Raschka, @rasbt). H2 2026 open releases split 50/50 between hybrids with a few global layers and models with no dense global attention at all; no full-attention-only models remain. Two gains: less attention compute, and a smaller KV cache.
- **NVIDIA Snapshot** ([blog](https://developer.nvidia.com/blog/start-and-restore-gpu-workloads-in-seconds-with-nvidia-snapshot/)). Open-source checkpoint/restore of fully initialized CPU and GPU state on Kubernetes. Inference replicas come up in 3.6 to 42.7 s, 8-36x faster than cold starts, with checkpoints up to 1 TB across eight B200s. GPU state restore dominates (18-29 s). Autoscaling cost lever: cold start is idle paid GPU time.
- **FlyHash for agent memory** ([2611.05791](https://arxiv.org/abs/2611.05791)). Fruit-fly hashing keeps its per-bit quality edge over SimHash under a fair protocol, but at equal bits its codes are larger and slower to compare, and HNSW beats both at ordinary scale. A careful negative result.

Relation: e-means and FlyHash both sit under retrieval-backed [agent memory](../agentic-systems/agent-memory.md); Sugar Glider and the Raschka census continue the [KV cache](kv-cache.md) page's architecture thread (fixed-state layers replacing a growing cache).
