---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.499572+00:00
arxiv_id: 2610.18356
url: https://huggingface.co/papers/2610.18356
arxiv_url: https://arxiv.org/abs/2610.18356
date: 2026-10-14
---

# Urbex: Agentic Spatial Grounding for City-Scale 3D Scenes

City-scale 3D grounding is commonly formulated as candidate ranking, which requires precomputed instance proposals and becomes inefficient in large outdoor scenes. We propose Urbex, an agentic vision-language framework that instead casts grounding as active spatial search. Urbex represents a city-scale 3D scene as an interactive multi-view environment, allowing a VLM agent to query landmarks, zoom into local regions, render oblique views, and commit a grounded bounding box. We optimize this tool-use policy with reinforcement learning on CityRefer, using smooth localization rewards and lightweight shaping rewards for efficient exploration. Experiments show that Urbex achieves the best Hit@1 and IoU on CityRefer, supports candidate-free grounding without ground-truth boxes, and is substantially faster than the strongest city-scale ranking baseline. Zero-shot results on STPLS3D-Refer further indicate improved cross-scene robustness.
