---
source: raw/huggingface/2026-04-17-superlocalmemory-v3-3-the-living-brain-biologically-inspired.md
arxiv: https://arxiv.org/abs/2604.04514
date: 2026-04-17
---

# SuperLocalMemory V3.3: Biologically-Inspired Agent Memory

## TL;DR

A local-first agent memory system that implements human-like memory dynamics: forgetting curves, cross-session consolidation, 7-channel retrieval, and progressive compression. No cloud LLMs required — runs entirely locally.

## Key Findings

- **Fisher-Rao Quantization-Aware Distance (FRQAD)**: a new embedding distance metric on the Gaussian statistical manifold that prefers high-precision embeddings over quantized ones. 100% accuracy vs 85.6% for cosine distance.
- **Ebbinghaus Adaptive Forgetting**: mathematical forgetting curves in local agent memory. Fading memories progressively lose embedding precision (compression increases as memory fades).
- **7-channel retrieval**: semantic, keyword, entity graph, temporal, spreading activation, consolidation, and Hopfield-style associative channels — all running locally.
- **Cross-session consolidation**: mimics hippocampal-neocortical memory transfer between sessions.
- **Zero-LLM operation**: full local deployment, no cloud dependency.

## Why It Matters

Current agent memory is mostly flat vector databases with single-channel retrieval. This system brings biological memory concepts — forgetting, consolidation, multi-channel association — to local agent memory. The FRQAD metric is particularly interesting as a principled way to handle quantized embeddings (relevant when running models locally with reduced precision).

## Related Pages

- [Agent Benchmarks](agent-benchmarks.md)
