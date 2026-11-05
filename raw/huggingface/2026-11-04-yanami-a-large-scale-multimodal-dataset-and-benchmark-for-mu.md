---
source: farmer/huggingface
farmed: 2026-11-05T20:36:55.360464+05:30
arxiv_id: 2611.05280
url: https://huggingface.co/papers/2611.05280
arxiv_url: https://arxiv.org/abs/2611.05280
date: 2026-11-04
---

# YANAMI: A Large-Scale Multimodal Dataset and Benchmark for Multiturn Stateful Interaction

Unified Multimodal Models (UMMs) integrate visual understanding, generation, and editing within a single unified framework. However, existing unified multimodal datasets and benchmarks remain dominated by single-turn tasks. Even in recent multi-turn datasets, many turns can be solved independently without tracking information across turns. Consequently, they provide limited supervision and evaluation for multimodal stateful interaction, which requires models to understand, maintain, update, and faithfully realize evolving dialogue states across turns. To address this gap, we introduce YANAMI, the first large-scale multimodal dialogue dataset and benchmark for stateful interaction, comprising YANAMI-400K and YANAMI-Bench. YANAMI-400K contains 400K multi-turn multimodal dialogues, with more than 2M images and 2.6M dialogue turns. The dialogues span four representative scenarios: Multi-Image Fusion, Image Editing, World Modeling, and Visual Reasoning, and require models to continuously track, preserve, and revise evolving multimodal dialogue states across turns. YANAMI-Bench comprises 400 multi-turn dialogues for systematically evaluating multimodal stateful interaction. It jointly evaluates Dialogue State Understanding and Visual Realization, characterizing the gap between models' ability to understand evolving dialogue states and their ability to faithfully realize them in visual outputs. Experiments show that fine-tuning BAGEL on YANAMI-400K improves image editing, generation, and multimodal stateful interaction by 10.3%, 2.0%, and 13.23%, respectively, while preserving its general visual understanding capabilities. Evaluations on YANAMI-Bench further reveal that existing UMMs still struggle to maintain, update, and visually realize evolving multimodal dialogue states.
