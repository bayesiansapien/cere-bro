# Joint Training of Multi-Token Prediction in RL via Optimal Coefficient Calibration (OCC)

**Date ingested:** 2026-05-28
**Source:** HuggingFace Daily Papers
**Links:** [arxiv 2605.28184](https://arxiv.org/abs/2605.28184) · [HuggingFace](https://huggingface.co/papers/2605.28184) · [raw](../../raw/huggingface/2026-05-28-joint-training-of-multi-token-prediction-in-reinforcement-le.md)

## TL;DR

RLVR (Reinforcement Learning from Verifiable Rewards, the now-standard recipe for improving reasoning) and MTP (Multi-Token Prediction, the popular pretraining auxiliary) are usually combined by detaching MTP gradients during RL because joint training degrades performance. The authors decompose the per-step MTP effect on the RL objective into a first-order correlation term and a second-order perturbation penalty, which unifies and explains three regimes that prior work used inconsistently (detach, cross-entropy joint, policy joint). They show that even the principled-looking policy-joint regime degrades because the correlation term decays during training while the quadratic penalty does not. OCC adaptively tracks the optimal MTP coefficient online using a cheap log-probability proxy, and across six competition-level math benchmarks matches or exceeds the detach baseline.

```
Per-step MTP contribution to RL objective:
  ΔObj  =   α · [first-order correlation: aligned with policy improvement]
          - β · [second-order perturbation penalty: persists]
                                          ▲
                                          │
             Detach    : drops both terms — safe, leaves MTP signal unused
             CE-joint  : keeps both, penalty wins, performance degrades
             Policy-joint: correlation decays, penalty persists, also degrades
             OCC       : track α/β online via log-prob proxy, adapt coefficient
```

## Key findings

- The MTP-on-RL effect decomposes cleanly into first-order correlation (helps) and second-order perturbation penalty (hurts).
- This decomposition unifies and explains why detach, CE-joint, and policy-joint all behave the way they do.
- The correlation term decays during training while the penalty persists, so any fixed coefficient eventually loses.
- OCC tracks the optimal coefficient online via a log-probability proxy at negligible cost.
- Across six competition-level math benchmarks, OCC consistently matches or exceeds the detach baseline.

## How this fits prior wiki state

This sits at the intersection of three threads. First, MTP-in-llama.cpp (2026-05-17) brought practical multi-token-prediction inference to local stacks; OCC is the corresponding training-side story. Second, the RLVR-reward-hacking work in Kurate top-10 ([[2026-05-28#worth-watching]] — "LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking", cs.LG #11) is the same RL-fragility frame. Third, the broader on-policy distillation efficiency line (ESR, today; TIP, 2026-04-16; LongAct, 2026-04-18) is also about which auxiliary signals carry useful gradient during what training phase.

## Related pages

- [[2026-05-17-mtp-llama-cpp-merge-strix-halo-benchmarks]] — MTP inference adoption
- [[2026-05-21-ik-llamacpp-mtp-cpu-offload-qwen36]] — MTP CPU offload
- [[2026-05-28-less-is-more-esr-on-policy-distillation]] — front-loaded signal in distillation

## Research angle

The decay of the correlation term during training is the result that should generalize. It implies that almost any "joint" auxiliary loss for RL has the same problem: it helps at the start, hurts at the end, and the crossover point is unstable. The OCC log-prob proxy is a cheap diagnostic that other auxiliary-loss settings could borrow. A natural follow-up is to apply the same decomposition to other RL+auxiliary combinations (RLVR+value, RLVR+verifier-distillation).
