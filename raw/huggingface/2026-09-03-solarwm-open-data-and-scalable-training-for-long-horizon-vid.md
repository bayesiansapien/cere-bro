---
source: farmer/huggingface
farmed: 2026-09-03T17:01:45.591071
arxiv_id: 2609.02886
url: https://huggingface.co/papers/2609.02886
arxiv_url: https://arxiv.org/abs/2609.02886
date: 2026-09-03
---

# SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models

We introduce SolarWM, a fully open foundation for building interactive video world models from data preparation through long-horizon inference. Training across heterogeneous data sources and video backbones is challenging: datasets differ in temporal scale, camera geometry, visual quality, motion, and captioning styles, while video generators use distinct representations and architectures. Naive data mixing and model-specific implementations therefore produce inconsistent supervision and make results difficult to reproduce and compare. SolarWM addresses this coupling with a reconfigurable multi-source data engine and a backbone-native adaptation framework. The engine converts 1.43 million canonical clips from 10 datasets into a unified, frame-aligned contract covering visual observations, metric camera geometry, captions, quality metadata, selection decisions, and provenance, while decoupling source processing from mixture construction. Under shared camera-conditioning, training, and inference interfaces, we instantiate four 5B--33B models based on Wan2.2, LTX-2.5, and MiniMax-H3 while preserving their native representations and objectives. A unified three-stage recipe combines bidirectional adaptation, teacher-forced autoregressive initialization, and distribution matching distillation. The resulting causal models enable real-time interaction over rollouts ranging from minutes to hours after being trained on only 5s sequences. By releasing the resulting data, pipeline, recipes, weights, and framework, SolarWM provides a reproducible and extensible foundation for interactive world-model research.
