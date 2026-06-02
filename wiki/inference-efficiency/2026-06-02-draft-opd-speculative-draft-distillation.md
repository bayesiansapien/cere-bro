# Draft-OPD: On-Policy Distillation for Speculative Draft Models

**Source:** HuggingFace Daily Papers · [arXiv 2605.29343](https://arxiv.org/abs/2605.29343)
**Raw:** [raw/huggingface/2026-06-02-draft-opd-on-policy-distillation-for-speculative-draft-model.md](../../raw/huggingface/2026-06-02-draft-opd-on-policy-distillation-for-speculative-draft-model.md)
**Date:** 2026-06-02

## TL;DR

Speculative decoding speeds up LLM inference by pairing a slow target model with a small draft model whose proposed tokens are verified in parallel. Draft models (EAGLE3, DFlash) are usually built by supervised fine-tuning (SFT) on target-generated trajectories, but the authors show SFT plateaus: the drafter's acceptance length stops improving because of an offline-to-inference mismatch. SFT trains on fixed target trajectories, while at decode time the drafter is judged on blocks it proposed under *its own* policy. Draft-OPD applies on-policy distillation (training the student on its own rollouts under teacher supervision) to the drafter, using target-assisted rollout for stable continuations and replaying drafting from the exact positions where verification exposed an error. Result: over 5x lossless acceleration for thinking models, beating EAGLE-3 by 23% and DFlash by 13%.

## Diagram

```
SFT drafter:   learn from FIXED target trajectories ─► plateau (offline≠inference)
               train distribution ≠ test distribution (drafter judged on ITS OWN blocks)

Draft-OPD:     target-assisted rollout  ─► stable continuation that follows target dist
               replay drafting FROM verification-exposed error positions
               ─► learn from target feedback on BOTH accepted & rejected proposals
               ─► focus training on the draft-induced errors that cap acceptance
               ─► 5x lossless accel · +23% vs EAGLE-3 · +13% vs DFlash
```

## Key points

- **Diagnosis: SFT for draft models has an offline-to-inference mismatch.** The drafter trains on the target's trajectories but is evaluated on the blocks it proposes itself; acceptance length plateaus on test data.
- **Why naive OPD is hard here.** Draft models cannot reliably roll out complete sequences alone. If you let the target assist the rollout (so sequences follow the target distribution), you destroy the on-policy signal you wanted. Draft-OPD's fix is to use target-assisted rollout *for stable continuations* but replay drafting specifically from the verification-exposed error positions, so the drafter still learns from its own induced errors.
- **Learns from rejected proposals too.** Training concentrates on the draft-induced errors that actually limit speculative acceptance, not just the accepted tokens.
- **Results:** >5x lossless acceleration for thinking (reasoning) models across diverse tasks; +23% over EAGLE-3 and +13% over DFlash.

## Relation to prior wiki knowledge

Two threads converge here. First, **on-policy distillation keeps reappearing as the fix for offline-training brittleness.** TA-OPD (2026-06-01, distill only on the ~5% of tokens whose teacher correction the student's support can actually reach) and the broader OPD line all stem from the same diagnosis the wiki keeps recording: training on a fixed offline distribution is mismatched to on-policy inference. DRIFT (2026-06-01, RL-quality multi-turn behavior at SFT cost by reweighting once-sampled rollouts) and DAgger-for-LLM-agents (2026-05-14, fixes covariate shift with on-policy distribution plus dense teacher labels) name the same covariate-shift problem. Draft-OPD applies that exact lesson to the speculative-decoding draft model, a place it had not yet been applied. See [knowledge-distillation.md](knowledge-distillation.md).

Second, it advances the **speculative decoding** line directly: EAGLE3 and DFlash were the SFT-built baselines; Draft-OPD shows the training objective, not just the draft architecture, is where the next acceleration gains live. See [speculative-decoding.md](speculative-decoding.md). It pairs naturally with today's other speculative-decoding paper, SPD (pipeline-parallel speculation), which attacks the *latency* of drafting rather than the *quality* of the drafter.

Related: [speculative-decoding.md](speculative-decoding.md) · [knowledge-distillation.md](knowledge-distillation.md) · [2026-06-02-spd-speculative-pipeline-decoding.md](2026-06-02-spd-speculative-pipeline-decoding.md) · [2026-06-01-ta-opd-token-teachability.md](2026-06-01-ta-opd-token-teachability.md)
