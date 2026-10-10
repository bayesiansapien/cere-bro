---
source: farmer/huggingface
farmed: 2026-10-10T05:09:51.421270+00:00
arxiv_id: 2609.31507
url: https://huggingface.co/papers/2609.31507
arxiv_url: https://arxiv.org/abs/2609.31507
date: 2026-10-09
---

# SatNav: A Scalable Benchmark for Long-Horizon UAV Vision-Language Navigation from Satellite Imagery

Urban uncrewed aerial vehicle (UAV) vision-language navigation (VLN) requires agents to follow instructions across extended urban spaces, inherently demanding long-term memory and geospatial grounding. However, scaling existing benchmarks remains difficult because of their reliance on costly reconstructed 3D assets, limiting geographic diversity and episode scale. To address this, we introduce SatNav, a scalable, long-horizon UAV VLN benchmark built from high-resolution satellite imagery. SatNav targets city-level navigation missions and uses satellite crops as approximations of UAV nadir views for visual observations. Through an automated cue-to-episode pipeline, SatNav constructs 118K episodes from 59 scenes across 18 cities, with an average trajectory length of 379 m. To stress-test long-horizon memory and geospatial reasoning, SatNav defines three task families: Boundary, Landmark, and Route, targeting loop progress tracking, landmark-based spatial grounding, and route following with counting cues. Benchmarking classical VLN agents and recent agents based on large vision-language models (LVLMs) on SatNav shows that city-scale navigation remains challenging. We further introduce SwiftVLN, a modular framework with switchable memory components, and conduct systematic memory-design ablations. Finally, satellite-to-UAV transfer experiments show that satellite-trained navigation models can operate on real-flight UAV observations, showing the practical relevance of SatNav. Our project page: https://eku127.github.io/SatNav/
