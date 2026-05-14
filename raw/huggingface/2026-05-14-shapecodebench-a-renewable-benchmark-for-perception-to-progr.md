---
source: farmer/huggingface
farmed: 2026-05-14T00:00:00
arxiv_id: 2605.11680
url: https://huggingface.co/papers/2605.11680
arxiv_url: https://arxiv.org/abs/2605.11680
date: 2026-05-14
---

# ShapeCodeBench: A Renewable Benchmark for Perception-to-Program Reconstruction of Synthetic Shape Scenes

We introduce ShapeCodeBench, a synthetic benchmark for perception-to-program reconstruction: given a rendered raster, a model must emit an executable drawing program that a deterministic evaluator re-renders and compares. The DSL has four primitives on a 512x512 black-on-white canvas, but every instance is generated from a seeded RNG, so fresh held-out sets can be minted to mitigate benchmark contamination. Because both instance generation and scoring are automatic, the same loop can refresh evaluations quickly without per-instance human annotation or manual judging. We release a frozen split, eval_v1 (150 samples, 50 per difficulty tier), scored by exact match, pixel accuracy, and foreground IoU alongside parse and execution success. Evaluating four reasoning-effort configurations of two frontier multimodal models against an empty-program floor and a classical-CV heuristic baseline exposes a tier-dependent crossover: the heuristic leads easy-tier exact match by individuating separated connected components, but collapses on medium and hard scenes as overlapping shapes fuse; the strongest multimodal model by foreground IoU retains most of the spatial structure and leads foreground IoU on every tier (up to 0.87), yet misses exact match by small parameter errors. Best overall exact match is 0.087 (heuristic) and 0.027 among multimodal models, so ShapeCodeBench is far from saturated.
