---
date: 2026-04-20
source: raw/huggingface/2026-04-20-cut-your-losses-learning-to-prune-paths-early-for-efficient.md
arxiv: https://arxiv.org/abs/2604.16029
tier: 1 — Inference Efficiency / Parallel Reasoning
---

# STOP: Super Token for Path Pruning in Parallel Reasoning

## TL;DR

Parallel reasoning in Large Reasoning Models (LRMs) wastes compute on paths that fail early due to errors that compound. STOP (Super TOken for Pruning) introduces a learnable special token inserted at the prefix that learns to predict whether a reasoning path is worth continuing. At a fixed compute budget, it lifts GPT-OSS-20B accuracy on AIME25 from 84% to ~90%. Works across models from 1.5B to 20B parameters.

## Key Findings

**The taxonomy — first systematic framework for path pruning:**
```
                Signal Source
               Internal  │  External
               ──────────┼────────────
Non-learnable │  entropy  │  verifier
  Learnable   │  STOP ★   │  trained judge
```

Prior work fragmented across all four quadrants. Learnable internal methods (bottom-left) were unexplored before STOP. The insight: internal signals (from the model itself, not an external oracle) are cheaper to obtain; learnable signals generalize better than hand-crafted heuristics.

**STOP mechanism:**
- A learned super-token is prepended to each parallel path at the prefix level
- The token learns to represent "should this path continue?" based on the prefix so far
- Pruning happens before the path is fully generated — saving computation proportional to the path's remaining length
- "Prefix-level" matters: early pruning saves more compute than late pruning

**Scalability validation:** Results across 1.5B → 20B parameter LRMs. The +6% AIME25 improvement (84% → 90%) holds at fixed compute budget — meaning STOP doesn't just reduce cost at fixed quality, it improves quality at fixed cost.

**Empirical guidelines distilled:** The paper includes deployment guidance on: (1) when path pruning helps most (high error-early path rate), (2) how to set the pruning threshold, (3) how to combine with external verifiers.

## Connection to the Broader Selective-Compute Pattern

This is the fifth consecutive paper in the wiki (since 04-16) instantiating the same core insight: identify and discard uninformative computation.

```
TIP (04-16):    discard uninformative tokens in distillation (10% signal tokens)
LongAct (04-18): discard uninformative gradient positions (sparse RL on high-saliency)
TESSY (04-18):  discard stylistically-divergent teacher tokens
STOP (04-20):   discard futile reasoning paths at the prefix (before spending compute)
AVR (04-20):    discard unnecessary reasoning format (pick perception-only or direct-answer)
```

The granularity is shifting: TIP operates at the token level, STOP at the path level, AVR at the reasoning format level. These are not competing methods — they can stack.

## Relations to Prior Wiki Pages

- **AIMO 3 / model-capability-dominates (04-17)**: AIMO 3 showed that prompt-level diversity can't close the pass@20 gap. STOP doesn't try to close the diversity gap — it makes each parallel path more cost-efficient. This is orthogonal to but composable with capability improvements.
- **VGF (04-19)**: VGF offered targeted particle refinement as an alternative to wider sampling. STOP is a middle path — sample widely, but prune failing paths early. Together they bracket the design space: refine-one (VGF) vs. prune-many (STOP).
- **Knowledge Distillation**: STOP could be applied to distillation: prune candidate rollouts that are clearly off-track before the student completes them.

## Open Questions

1. Does STOP generalize to open-ended reasoning (code, math proofs) or only constrained tasks with identifiable early failure signals?
2. Can STOP be combined with VGF's particle-transport approach? (Transport only paths that pass STOP's gate)
3. What does the super-token learn? Is it identifying syntactic errors, semantic inconsistencies, or something more abstract?

## Raw Source

→ [raw/huggingface/2026-04-20-cut-your-losses-learning-to-prune-paths-early-for-efficient.md](../../raw/huggingface/2026-04-20-cut-your-losses-learning-to-prune-paths-early-for-efficient.md)
