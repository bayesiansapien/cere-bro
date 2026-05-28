# IB-TPO: Information Bottleneck Driven Tree-Based Policy Optimization

**Date ingested:** 2026-05-28
**Source:** HuggingFace Daily Papers
**Links:** [arxiv 2605.28109](https://arxiv.org/abs/2605.28109) · [HuggingFace](https://huggingface.co/papers/2605.28109) · [code](https://github.com/alibaba/EfficientRL) · [raw](../../raw/huggingface/2026-05-28-long-live-the-balance-information-bottleneck-driven-tree-bas.md)

## TL;DR

Online RL for LLMs (GRPO, PPO and their kin) routinely loses the exploration-exploitation balance: rollouts collapse on a narrow set of trajectories, or they spread so wide that the policy never converges. The authors define IB-Score, an Information Bottleneck quantity that measures, per step, the trade-off between reasoning diversity at that step and the mutual information that step carries about the final correct answer. They show GRPO with standard regularizers fails to hold this balance during training. IB-TPO turns IB-Score into a fine-grained training objective, paired with a tree-sampling strategy that yields 50% more trajectories per token budget and reuses the tree structure for cheap Monte Carlo estimation of IB-Score. Across standard reasoning benchmarks, IB-TPO beats GRPO by 2.9 to 3.6 points and other state-of-the-art online RL approaches.

```
GRPO sample shape:         IB-TPO tree:
  prompt                     prompt
   ├ rollout 1                ├ branch A ── A.1 ── A.1.1
   ├ rollout 2                │         └─ A.2
   └ rollout 3                └ branch B ── B.1
   (flat, often collapses)    (shared prefix, more trajectories per budget,
                               IB-Score estimated by Monte Carlo over the tree)
```

## Key findings

- IB-Score isolates the per-step exploration-exploitation trade-off as a measurable quantity grounded in Information Bottleneck theory.
- Popular online RL (GRPO with standard regularizers) does not maintain this balance during training; both diversity collapse and signal loss show up.
- Tree-structured sampling produces 50% more trajectories under the same token budget and supports cheap Monte Carlo IB-Score estimation.
- IB-TPO beats GRPO by 2.9 to 3.6 points and outperforms other SoTA online RL methods on standard reasoning benchmarks.

## How this fits prior wiki state

This is the third RL-for-reasoning paper in two days that argues the standard GRPO recipe wastes signal. AXPO ([[2026-05-28-axpo-explorative-policy-optimization]]) attacks the all-wrong-tool-call subgroup by resampling only the action branch. OCC ([[2026-05-28-joint-mtp-rl-occ]]) shows the joint MTP-RL coefficient must be adapted online because the helpful first-order term decays while the harmful penalty persists. IB-TPO targets a different failure mode again, the diversity-vs-signal trade-off across the rollout tree. All three frame current RL stacks as wasting gradient on rollouts that look bad but had no chance of being useful, and all three remedy it with selective resampling or adaptive weighting.

The Kurate cs.LG #11 "LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking" sits on the failure side: the policy finds shortcuts when the verifier is exploitable. IB-TPO's information-theoretic objective is structurally the right place to add a counter-incentive because IB-Score penalizes steps that carry no mutual information with the correct answer.

## Related pages

- [[2026-05-28-axpo-explorative-policy-optimization]] — resample all-wrong tool-call subgroups
- [[2026-05-28-joint-mtp-rl-occ]] — online coefficient adaptation for MTP+RL
- [[2026-05-28-bes-bidirectional-evolutionary-search]] — escaping the entropy shell via recombination
- [[2026-05-28-less-is-more-esr-on-policy-distillation]] — front-loaded signal in distillation rollouts
- [[2026-05-27-cpt-collaborative-parallel-thinking]] — sharing findings across parallel branches

## Research angle

The most general claim is that IB-Score is a per-step diagnostic of how much information a rollout step carries about the answer. If it survives stress-testing on agentic-coding rollouts (much longer, partial verifiability) it could replace the ad-hoc KL and entropy regularizers that current RL recipes patch into the loss. A natural follow-up is composing IB-TPO with BES's recombination operators: IB-Score chooses which tree branches to expand, BES recombines surviving partial trajectories. The combination would attack diversity collapse from two angles simultaneously.
