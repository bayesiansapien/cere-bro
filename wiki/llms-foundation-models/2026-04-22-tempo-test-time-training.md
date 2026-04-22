# TEMPO: Scaling Test-Time Training for Large Reasoning Models

**Date:** 2026-04-22  
**Source:** [HuggingFace](https://huggingface.co/papers/2604.19295) | [Paper](https://arxiv.org/abs/2604.19295)  
**Raw:** [raw/huggingface/2026-04-22-tempo-scaling-test-time-training-for-large-reasoning-models.md](../../raw/huggingface/2026-04-22-tempo-scaling-test-time-training-for-large-reasoning-models.md)

## TL;DR

Test-time training (TTT) adapts model weights on unlabeled test instances at inference time. Existing TTT methods for reasoning models plateau quickly — the self-generated reward signal drifts as the policy evolves, causing both performance saturation and diversity collapse. TEMPO fixes this by interleaving policy refinement on unlabeled questions with periodic critic recalibration on a labeled calibration set, formalized via the EM algorithm. Result: OLMO3-7B AIME 2024 from 33% → 51.1%; Qwen3-14B from 42.3% → 65.8%.

## Key Findings

- Prior TTT methods plateau because the E-step (reward evaluation) degrades as the policy model changes — they omit the M-step recalibration
- TEMPO alternates: (1) policy refinement on unlabeled test queries, (2) critic recalibration on a small labeled calibration set
- Formalizing this as EM reveals prior methods are "incomplete EM" — they only run E-steps
- Reintroducing the M-step tightens the ELBO and enables sustained improvement without diversity collapse
- Works across model families (Qwen3 and OLMO3)

## Mechanism

```
Standard TTT (degrades):
  [policy generates rollouts on test query]
        ↓
  [reward model scores them]   ← reward model not updated, drifts from policy
        ↓
  [policy update]
  (repeat → fast plateau, diversity collapse)

TEMPO:
  [policy update on unlabeled test queries]  ← E-step
        ↓
  [critic recalibration on labeled set]      ← M-step (the missing piece)
        ↓
  [policy update on unlabeled test queries]  ← E-step again
  (alternating → sustained improvement, diversity preserved)
```

The EM framing is the key insight. The "E-step" is estimating the quality of rollouts (reward evaluation). The "M-step" is recalibrating the reward model to stay accurate as the policy evolves. Running only E-steps eventually produces a reward model that's evaluating a policy it no longer understands — the drift causes the plateau.

## Relation to Prior Wiki Knowledge

The saturation problem TEMPO solves is the same one documented in **RLVR Under Weak Supervision (04-21)**. That paper showed that rapid reward saturation during training predicts failure to generalize — the model memorizes rather than reasoning. TEMPO provides a mechanism to *prevent* that saturation at test time: keep the critic calibrated so the reward signal stays informative.

**Connecting to GFT (04-21)**: GFT showed that SFT's implicit reward is too sparse to distinguish "very wrong" from "almost right." TEMPO shows that even a good initial reward eventually goes stale if the critic isn't updated alongside the policy. Both papers argue the reward signal needs active management, not just the right initial form.

**Connecting to Self-Evolution (04-21)**: Self-evolution agents bake exploration behavior into model weights during training, then deploy reward-free. TEMPO is the opposite approach — keep adapting at inference time but keep the reward model calibrated. These are two different solutions to the "where does the learning signal come from at deployment?" problem.

## Open Questions

- How large does the labeled calibration set need to be? Very small calibration sets might not represent the diversity of unlabeled test queries.
- Does periodic critic recalibration generalize to domains beyond math reasoning where verifiable ground truth is harder to obtain?
- What's the optimal alternation frequency between E-step and M-step? This paper uses a fixed schedule — an adaptive schedule might improve further.

## Related Pages

- [RL for LLMs](rl-for-llms.md)
- [RLVR Under Weak Supervision](2026-04-21-rlvr-weak-supervision-reasoning-faithfulness.md)
- [GFT: SFT as Degenerate RL](2026-04-21-gft-sft-as-degenerate-rl.md)
