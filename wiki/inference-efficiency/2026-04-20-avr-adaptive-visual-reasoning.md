---
date: 2026-04-20
source: raw/huggingface/2026-04-20-learning-adaptive-reasoning-paths-for-efficient-visual-reaso.md
arxiv: https://arxiv.org/abs/2604.14568
tier: 2 — Inference Efficiency / Visual Reasoning
---

# AVR: Adaptive Visual Reasoning for Efficient VRMs

## TL;DR

Visual Reasoning Models (VRMs) overthink simple visual questions — producing long reasoning chains for tasks that need a single perception step. AVR decomposes visual reasoning into three functions (perception, logical reasoning, answer application) and trains a model to pick the minimally sufficient format via FS-GRPO. Reduces token usage 50-90% while maintaining accuracy.

## Key Findings

**Root cause — Reasoning Path Redundancy:** Many visual questions don't need multi-step reasoning. A "what color is the car?" question doesn't need a chain-of-thought. Current VRMs apply full reasoning regardless, because they're trained to reason fully.

**AVR's three response formats:**
```
Full Format:          [Perception] → [Logical Reasoning] → [Answer Application]
Perception-Only:      [Perception] → [Answer]
Direct Answer:        [Answer]
```

The model learns to select the minimally sufficient format. FS-GRPO (a GRPO variant) rewards the most efficient correct format.

**Results:** 50-90% token reduction across vision-language benchmarks. Largest reductions in perception-intensive tasks (object detection, attribute questions) where full reasoning is most wasteful.

**FS-GRPO:** Format-aware GRPO variant that gives bonus reward for selecting a shorter format when that format produces a correct answer. The reward signal teaches frugality without sacrificing correctness.

## Connection to the Selective-Compute Pattern

AVR joins STOP (04-20), TIP (04-16), and LongAct (04-18) in the same paradigm: identify the minimal computation that achieves the result. TIP does this at token level in distillation. STOP at path level in parallel reasoning. AVR at format level in visual reasoning. These are now five papers in five days making the same claim at different granularities.

## Relations to Prior Wiki Pages

- **STOP (04-20)**: STOP prunes paths that fail early. AVR selects the format that requires the least reasoning. They compose: STOP could prune AVR's Full Format paths that fail early.
- **Switch-KD (04-18)**: Switch-KD routed visual outputs through language pathway for distillation efficiency. AVR reduces the reasoning computation that produces those outputs.
- **Knowledge Distillation**: A teacher with AVR-style adaptive reasoning could produce shorter, more targeted traces for student training. This would intersect with TESSY (04-18) on what kind of reasoning traces are stylistically compatible.

## Raw Source

→ [raw/huggingface/2026-04-20-learning-adaptive-reasoning-paths-for-efficient-visual-reaso.md](../../raw/huggingface/2026-04-20-learning-adaptive-reasoning-paths-for-efficient-visual-reaso.md)
