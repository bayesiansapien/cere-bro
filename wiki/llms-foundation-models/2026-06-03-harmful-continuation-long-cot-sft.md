# Diagnosing Harmful Continuation in Answer-Correct Long-CoT Training Traces

**Date:** 2026-06-03
**Source:** HuggingFace Daily Papers
**arXiv:** [2605.29288](https://arxiv.org/abs/2605.29288)
**Tier:** 2 — CoT supervision, reasoning SFT data quality

## TL;DR

Long chain-of-thought (CoT) traces are standard SFT supervision for reasoning models, but even answer-correct traces produce very different fine-tuning outcomes. This paper isolates one culprit: *post-conclusion continuation*, where the answer is already sufficiently supported but the trace keeps reasoning, and that extra reasoning stays in the supervised target. Using a delete-only editor to build answer-preserving suffix-removed traces, SFT on the trimmed traces beats SFT on the originals — so the trailing continuation is *harmful continuation*. Characterizing the removed spans shows persistent local uncertainty together with weakened terminal-directional progress (an "uncertainty–geometry mismatch"). The authors ship Harmful Continuation Cut (HCC), a lightweight boundary proxy that approximates the editor-identified cut point.

```
answer-correct long-CoT trace:
  [ reasoning ...... ANSWER SUPPORTED | post-conclusion continuation ]
                                       └── persistent local uncertainty
                                           + weakened terminal progress
                                       = "harmful continuation"
                                                │
                          HCC boundary proxy ───┘  → cut, then SFT
                          (trimmed traces > original traces)
```

## Key points

1. **Answer-correct ≠ training-clean.** Correctness of the final answer does not guarantee the trace is good supervision; the tail after the conclusion can degrade SFT.
2. **Causal test, not correlation.** A delete-only editor preserves the answer and removes only the continuation; the improvement after removal is what licenses the "harmful" label.
3. **A signature for the boundary.** Harmful continuation shows persistent local uncertainty with weakened terminal-directional progress in hidden states; HCC is a cheap proxy that finds the cut.

## Relation to prior wiki state

This is a data-side member of the wiki's dominant "the learning signal is sparse and locatable, and most of the trace is noise" thread. [TIP](../inference-efficiency/2026-04-16-tip-token-importance-on-policy-distillation.md) (04-16) found <10% of distillation tokens carry signal; [TA-OPD](2026-06-01-ta-opd-token-teachability.md) (06-01) kept only reachable teacher corrections; [Temporal Scheduling for RLVR](2026-06-02-temporal-scheduling-rlvr.md) (06-02) scheduled *when* to apply credit. Harmful Continuation adds the *suffix* axis: even within a correct trace, the tail is negative signal. It pairs with [PUMA](../inference-efficiency/2026-05-19-puma-semantic-preserving-early-exit-reasoning.md) (05-19, semantic-preserving early exit for reasoning) — PUMA cuts continuation at *inference*, HCC cuts it from *training data*. Same insight (reasoning past the answer is wasted or harmful) at two stages.

## Links

- [Paper (arXiv)](https://arxiv.org/abs/2605.29288) · [HuggingFace page](https://huggingface.co/papers/2605.29288)
- Raw: [raw/huggingface/2026-06-03-diagnosing-harmful-continuation-in-answer-correct-long-cot-t.md](../../raw/huggingface/2026-06-03-diagnosing-harmful-continuation-in-answer-correct-long-cot-t.md)
- Concept page: [RL for LLMs](rl-for-llms.md)
- Related: [TIP 04-16](../inference-efficiency/2026-04-16-tip-token-importance-on-policy-distillation.md) · [PUMA 05-19](../inference-efficiency/2026-05-19-puma-semantic-preserving-early-exit-reasoning.md)
