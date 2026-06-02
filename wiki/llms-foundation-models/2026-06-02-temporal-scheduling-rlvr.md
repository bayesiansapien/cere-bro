# Not Only Where, But When: Temporal Scheduling for RLVR

## TL;DR

Reinforcement learning with verifiable rewards (RLVR, post-training where a checkable reward such as "did the math answer verify" drives policy updates) broadcasts one scalar reward across all sampled tokens, ignoring that different parts of a trajectory show different policy behaviors. Prior work fixes this with credit allocation, meaning token-level advantage reweighting or selective token optimization, but the allocation criterion stays fixed throughout training. This paper adds a temporal dimension: schedule the credit-allocation criterion over the course of training. Prioritizing targeted tokens tied to specific policy behaviors early, then gradually attenuating toward uniform optimization later, gives more stable and efficient learning. The analysis shows standard optimization sacrifices a lot of policy entropy (the diversity of the model's choices) when it tries to accommodate heterogeneous behaviors all at once, while temporal scheduling yields healthier entropy evolution. Gains are consistent across math and general reasoning, and simple trajectory percentiles are enough to distinguish behaviors.

```
  rollout ─► split into trajectory PERCENTILES (early / mid / late behavior)
                                  │
                                  ▼
        credit criterion C(t) CHANGES over training:
          early  ──► emphasize TARGETED behavior-specific tokens   (selective)
          ...                                                       │
          late   ──► relax toward UNIFORM optimization             (general)
                                  │
   weighting curve:  selective ─────────────────► uniform   (time axis)
                                  │
                                  ▼
        advantage reweight ─► policy update ─► healthier entropy evolution
```

## Key points

- Adds a time axis to credit assignment: existing methods decide where (which tokens) to put the learning signal; this paper argues when (at what training stage) the criterion applies is equally important, and makes the criterion evolve over training.
- Trajectory percentiles are a cheap behavior lens that distinguishes policy behaviors along a rollout and works well with temporal scheduling, with no extra model required.
- Entropy is the diagnostic: standard optimization sacrifices policy entropy when forcing one update to accommodate heterogeneous behaviors at once, while scheduling keeps entropy healthier, which is why training is more stable.
- Consistent improvements across mathematical and general reasoning benchmarks (the abstract gives no hard numbers).

## How this relates to prior wiki pages

This is the cleanest extension yet of the wiki's "locate the load-bearing part, then spend effort only there" thread, and it explicitly names the missing dimension. That thread has been spatial so far: [TIP (2026-04-16), which found the real learning signal lives in under 10% of tokens](../inference-efficiency/2026-04-16-tip-token-importance-on-policy-distillation.md), [TA-OPD (2026-06-01), which distilled only on tokens the student could actually reach](../inference-efficiency/2026-06-01-ta-opd-token-teachability.md), and [DELTA (2026-05-23), which assigned RLVR credit to discriminative tokens](2026-05-23-delta-discriminative-token-credit-rlvr.md). All answer where to concentrate effort. Temporal scheduling answers when, arguing the right token to emphasize changes as the policy evolves, so a fixed allocation rule leaves stability on the table. It also pairs with today's [ESPO (2026-06-02), which truncates doomed rollouts mid-generation to stop wasting compute](2026-06-02-espo-early-stopping-ppo.md): both reject PPO's uniform treatment of a trajectory. The entropy-preservation result is a concrete mechanism for the "don't let RLVR collapse to a narrow policy" concern tracked in [rl-for-llms.md](rl-for-llms.md).

## Gaps

The abstract reports consistent gains but no hard numbers, benchmark-by-benchmark deltas, or baseline comparisons, so the magnitude of the improvement is unknown. The schedule shape (how fast to attenuate from selective to uniform) appears hand-designed and its sensitivity is not characterized. Trajectory percentiles are used as a proxy for policy behavior, but whether percentiles actually capture the behaviors that matter, versus a learned behavior classifier, is not validated. Results are on reasoning tasks; whether temporal scheduling helps when rewards are noisier or less verifiable is open.

**Source:** [arXiv 2605.25381](https://arxiv.org/abs/2605.25381) · [raw file](../../raw/huggingface/2026-06-02-not-only-where-but-when-temporal-scheduling-for-rlvr.md)
