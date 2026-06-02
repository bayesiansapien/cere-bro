# Not Only Where, But When: Temporal Scheduling for RLVR

**Source:** HuggingFace Daily Papers · [arXiv 2605.25381](https://arxiv.org/abs/2605.25381)
**Raw:** [raw/huggingface/2026-06-02-not-only-where-but-when-temporal-scheduling-for-rlvr.md](../../raw/huggingface/2026-06-02-not-only-where-but-when-temporal-scheduling-for-rlvr.md)
**Date:** 2026-06-02

## TL;DR

Reinforcement learning with verifiable rewards (RLVR, post-training where a checkable reward like "did the math answer verify" drives policy updates) broadcasts one scalar reward across all sampled tokens, ignoring that different parts of a trajectory exhibit different policy behaviors. Prior work fixes this with credit allocation (token-level advantage reweighting, selective token optimization), but the allocation criterion stays *fixed throughout training*. This paper adds a temporal dimension: schedule the credit-allocation criterion over the course of training. Prioritizing targeted tokens tied to specific policy behaviors early and gradually attenuating toward general optimization yields more stable, efficient learning, with consistent gains on math and general reasoning.

## Diagram

```
Standard RLVR:        one scalar reward broadcast to ALL tokens ─► heterogeneous behaviors blurred,
                      large entropy sacrifice
Credit allocation:    reweight/ select tokens — but the criterion is STAGNANT all of training

This paper (temporal scheduling): WHEN you allocate credit matters as much as WHERE
   early:  prioritize targeted tokens with specific policy behaviors
           (trajectory percentiles distinguish behaviors)
   later:  gradually attenuate ─► general optimization
   ─► healthier policy-entropy evolution, more stable/efficient learning
```

## Key points

- **Adds a time axis to credit assignment.** Existing methods decide *where* (which tokens) to put learning signal; this paper argues *when* (at what training stage) the criterion applies is equally important, and makes the allocation criterion evolve over training.
- **Trajectory percentiles as a behavior lens.** Simple trajectory percentiles naturally distinguish policy behaviors and work well with temporal scheduling — a cheap signal, no extra model.
- **Entropy is the diagnostic.** Standard optimization sacrifices a lot of policy entropy when forcing one update to accommodate heterogeneous behaviors at once; temporal scheduling keeps entropy healthier, which is why training is more stable.
- Consistent improvements across mathematical and general reasoning benchmarks.

## Relation to prior wiki knowledge

This paper is the cleanest extension yet of the wiki's **"locate the load-bearing part, spend only there"** thread — it explicitly names the next dimension. The thread so far has been spatial: TIP (2026-04-16, learning signal lives in under 10% of tokens), TA-OPD (2026-06-01, distill only on tokens whose teacher correction the student can reach), Make-Each-Token-Count (2026-05-12, learned KV eviction). All answer *where* to concentrate effort. Temporal Scheduling answers *when*, arguing the right token to emphasize changes as the policy evolves, so a fixed allocation rule is leaving stability on the table. The title literally encodes the wiki's framing: "not only where, but when." See [rl-for-llms.md](rl-for-llms.md).

It also connects to the entropy-collapse concern that RLVR papers keep raising: by scheduling credit, the method preserves policy entropy that uniform credit assignment burns. That is a concrete mechanism for the "don't let RLVR collapse to a narrow policy" problem the wiki has tracked.

Related: [rl-for-llms.md](rl-for-llms.md) · [2026-06-01-ta-opd-token-teachability.md](../inference-efficiency/2026-06-01-ta-opd-token-teachability.md)
