# Less is More: Early Stopping Rollout for On-Policy Distillation (ESR)

**Date ingested:** 2026-05-28
**Source:** HuggingFace Daily Papers
**Authors:** Zhou Ziheng, Jiaqi Li, Huacong Tang, Ying Nian Wu, Demetri Terzopoulos (UCLA; BIGAI Beijing)
**Links:** [arxiv 2605.27028](https://arxiv.org/abs/2605.27028) · [HuggingFace](https://huggingface.co/papers/2605.27028) · [raw](../../raw/huggingface/2026-05-28-less-is-more-early-stopping-rollout-for-on-policy-distillati.md)

## TL;DR

On-policy distillation (OPD) trains a student to mimic a teacher by scoring the student's own rollouts. Standard OPD trains on every token of the rollout. ESR throws out everything after a small prefix and keeps only the first response tokens. That alone beats full-rollout OPD across model size, family, task, and training regime, with much higher GPU efficiency and training stability. The mechanism is that the teacher's corrective signal decays the further it gets from on-policy territory: after the student has talked itself into off-policy ground, the teacher just predicts the next token rather than correcting the trajectory. Position, not just entropy or KL, is the load-bearing dimension.

```
Standard OPD rollout:           [tok_1 ... tok_5 | tok_6 ............... tok_N]
                                  ◄── teacher corrective ──►◄ teacher decays to LM completion ─►
                                  position 1-5 carries signal     positions 6-N pollute the loss

ESR keeps only the prefix:      [tok_1 ... tok_5] ✂  rest discarded
                                  shorter rollouts, higher GPU efficiency, fewer off-policy tokens
```

## Key findings

- ESR beats full-rollout OPD across multiple model sizes, families, tasks, and training regimes.
- GPU efficiency is much higher because rollouts are shorter; training is also more stable, especially under cross-model-family scenarios where the off-policy gap is largest.
- Two new effects explain the surprising gains: Cascading Alignment (early correct tokens stabilize the rest) and Sub-mode Commitment (early prefix locks the student into a coherent solution mode the teacher endorses).
- Position-based selection cannot be fully replicated by entropy or KL-divergence-based token weighting. Position carries information neither of those captures.
- In some settings ESR-trained students exceed the teacher's own performance, because the teacher's "best moves" are in its early-token regime.

## How this fits prior wiki state

The OPD waste-cluster has been building for weeks. TIP (2026-04-16) found that most teacher-generated tokens carry no signal and showed that selectively weighting tokens by importance is enough to keep quality. LongAct (2026-04-18) found that long-context gradient signal is concentrated in the first 5% of tokens, making selective training a saliency problem. The Extrapolation Cliff (2026-05-14) gave a closed-form threshold above which on-policy distillation collapses entirely. TIP-style and LongAct-style cuts both relied on saliency profiling. ESR sidesteps profiling entirely: just truncate by position. The agreement across four independent threads (TIP, LongAct, Extrapolation Cliff, and now ESR) is that on-policy distillation training signal is heavily front-loaded, and the gradient on tokens past a short prefix is mostly noise.

The novelty over TIP/LongAct is that ESR makes no claim about which specific tokens matter; it just claims the prefix carries enough signal that the rest can be discarded for free. That is a simpler operational rule than saliency thresholds, and it ties cleanly to the entropy/exploration findings in AXPO (today, 2026-05-28) about resampling tool-call subgroups where the early prefix is what matters.

## Related pages

- [[2026-04-16-tip-token-importance-on-policy-distillation]] — selective token weighting in OPD
- [[2026-04-18-longact-saliency-sparse-rl]] — saliency-driven long-context training
- [[2026-05-14-extrapolation-cliff-on-policy-distillation]] — OPD collapse threshold
- [[2026-05-13-many-faces-on-policy-distillation]] — survey of OPD variants

## Research angle

The Cascading Alignment effect deserves a clean mechanistic study. If early tokens lock the student into the teacher-endorsed mode, then the teacher is not really providing token-level supervision at all; it is providing mode-selection supervision and the rest is autoregressive momentum. That reframing connects OPD to the "sleep" line of work (LMs Need Sleep, surfaced 05-26 via Twitter) which also tries to push computation out of the token-level inner loop. An ablation that compares ESR rollouts of length k against k random tokens or k high-entropy tokens, holding total token count constant, would settle whether position carries information independent of token identity.
