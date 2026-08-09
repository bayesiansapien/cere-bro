---
source: farmer/huggingface
farmed: 2026-08-09T07:10:01.249497+00:00
arxiv_id: 2608.05248
url: https://huggingface.co/papers/2608.05248
arxiv_url: https://arxiv.org/abs/2608.05248
date: 2026-08-09
---

# WorldClaw: Agentic 3D Open-World Generation at Scale

Generating large-scale, freely explorable 3D worlds from open-ended text remains challenging because a system must jointly maintain global spatial coherence, rich local content, and explicit assets suitable for downstream editing and reuse. We present WorldClaw, a fully agentic, coarse-to-fine framework for open-world 3D scene generation. Planning agents translate a text prompt into a structured specification of regions, terrain, assets, materials, and spatial relations. WorldClaw then builds a globally coherent terrain foundation from semantic layouts, reusable assets, generative or procedural materials, and a region-aware height field. For detail-demanding regions, it generates terrain-conditioned compositions, reconstructs editable textured meshes, and recovers their placement on the terrain; render-based agents further refine terrain, objects, appearance, and contacts. Across diverse open-world prompts, WorldClaw produces large-scale scenes with coherent spatial organization, visually compelling local content, and editable instance-level assets while preserving a consistent global terrain structure.
