---
date: 2026-04-20
source: raw/huggingface/2026-04-20-maximal-brain-damage-without-data-or-optimization-disrupting.md
arxiv: https://arxiv.org/abs/2502.07408
tier: 1 — Compression / GPU Optimization / Model Security
---

# Maximal Brain Damage: Disrupting Neural Networks via Sign-Bit Flips

## TL;DR

Two sign-bit flips in carefully-chosen parameters collapse ResNet-50 accuracy by 99.8% on ImageNet. Two sign flips into different experts zero out Qwen3-30B reasoning from 78% to 0% accuracy. The vulnerability scan (Deep Neural Lesion, DNL) requires no data and no optimization — just one forward-backward pass on random inputs. The same analysis reveals a defense: protect a small set of vulnerable sign bits.

## Key Findings

**The attack — Deep Neural Lesion (DNL):**
- Finds the parameters whose sign flip causes maximal output disruption
- Data-free and optimization-free in the base version
- 1P-DNL (one-pass variant): one forward + backward pass on random inputs to refine the selection
- Span: image classification, object detection (COCO Mask R-CNN, YOLOv8-seg), reasoning LLMs

**Results across domains:**
- ResNet-50 on ImageNet: 2 sign flips → -99.8% accuracy
- Mask R-CNN / YOLOv8-seg: 1-2 sign flips → COCO detection AP collapses
- Qwen3-30B-A3B-Thinking: 2 sign flips into different experts → 78% → 0% accuracy

**Why sign bits specifically?** In standard float32/float16/bfloat16, the sign bit is a single bit that flips a parameter's effect from positive to negative (or vice versa). For a parameter with large magnitude, this causes the largest possible value change. The most influential weights — precisely those that the model relies on most — are also the most catastrophically disruptable.

**The defense:** Identify the small fraction of vulnerable sign bits (same method used for attack) and selectively protect them. The paper shows this is feasible without protecting all parameters.

## Implications for Compression Research

This paper is a direct challenge to any compression scheme that identifies "important" parameters and keeps them at higher precision. TIP (04-16) identifies high-entropy and overconfident tokens; LongAct (04-18) identifies high-magnitude KV activations; standard quantization preserves high-magnitude weights. These identification methods are useful precisely because the identified parameters are influential. But DNL shows the same influence makes them maximally exploitable.

The field is simultaneously building methods to find important parameters (for efficiency) and now discovering that important parameters are the attack surface. These two lines of research need to converge.

## Relations to Prior Wiki Pages

- **LongAct (04-18)**: LongAct identifies high-magnitude KV activations as the positions where attention does real work. DNL shows that high-magnitude parameters are exactly the sign-bit-flip targets. The insight is the same from opposite directions.
- **TIP (04-16)**: TIP's selective token approach preserves the most informative parameters. DNL shows those parameters are also the most vulnerable.
- **Knowledge Distillation**: compression methods that find and preserve important parameters may inherit this vulnerability profile.

## Open Questions

1. Does the vulnerability extend to MoE routing? The Qwen3-30B result targeted different experts — which suggests routing parameters specifically might be high-value targets.
2. Can hardware-level bit-flip protection be applied selectively to vulnerable parameters only (not all memory)?
3. Is there a connection between saliency-based KV cache eviction (keep the important tokens) and the sign-bit target set (flip the important weights)?

## Raw Source

→ [raw/huggingface/2026-04-20-maximal-brain-damage-without-data-or-optimization-disrupting.md](../../raw/huggingface/2026-04-20-maximal-brain-damage-without-data-or-optimization-disrupting.md)
