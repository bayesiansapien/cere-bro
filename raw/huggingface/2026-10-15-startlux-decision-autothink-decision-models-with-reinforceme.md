---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.228472+05:30
arxiv_id: 2610.17309
url: https://huggingface.co/papers/2610.17309
arxiv_url: https://arxiv.org/abs/2610.17309
date: 2026-10-15
---

# StartLux-Decision: AutoThink Decision Models with Reinforcement Learning for Calibrated Deliberative Decisions

We introduce StartLux-Decision, decision models from 0.8B to 27B parameters that combine efficient single-pass prediction with adaptive, confidence-guided reasoning. The Instant models use bidirectional attention in full-attention layers to improve decision accuracy while keeping single-pass inference. The AutoThink models invoke explicit reasoning for uncertain decisions and answer confident cases directly. A three-stage training pipeline establishes shared decision capabilities, specializes the two variants, and equips AutoThink with reasoning through reasoning supervision and reinforcement learning. We introduce Reinforcement Learning for Calibrated Deliberative Decisions (RLCD^2), which uses a frozen model and proper scoring rules to reward improvements in decision probability quality and applies a soft penalty to overlong reasoning traces. RLCD^2 raises the share of reasoning traces that terminate within the generation limit by up to 48 percentage points and cuts average reasoning length by up to 65%, while largely preserving decision accuracy. On the public subset of Decision Index 0.3, the Instant models outperform the strongest evaluated comparable-scale open-weight decision models by 7.4-16.9 points, and the 27B AutoThink model reaches 73.4. We also introduce DecisionPivot, a programmatically verifiable benchmark of computational decisions built from contrast pairs that differ in a single answer-changing detail. On DecisionPivot, AutoThink outperforms its Instant counterparts by 11.5-18.4 points in pair accuracy and leads among evaluated systems. The models run on vLLM, llama.cpp and MLX, with quantized variants for lower memory use.
