# DRIFT: Decoupled Rollouts and Importance-Weighted Fine-Tuning for Efficient Multi-Turn Optimization

**TL;DR.** LLMs are increasingly deployed in multi-turn settings where users or environments give lightweight feedback across several turns. Optimizing for this is a dilemma. Online reinforcement learning (RL, where the model learns by trial and reward) handles the multi-turn dynamics well, but it is very expensive because it must generate fresh correction trajectories at every update step. Offline supervised fine-tuning (SFT, training on a fixed labeled dataset) is cheap, but it suffers distribution shift and behavioral collapse. DRIFT uses a known theoretical fact: the KL-regularized RL objective (RL with a penalty that keeps the new policy close to a reference policy) is equivalent to importance-weighted supervised learning. It DECOUPLES rollout from optimization. It samples offline interaction trajectories once from a fixed reference policy, derives return-based importance weights, and then optimizes the policy by weighted SFT on that fixed dataset. Empirically it matches or exceeds multi-turn RL baselines while keeping SFT's training efficiency and simplicity.

```
┌────────────────┐   sample once   ┌───────────────────┐
│ reference policy│ ──────────────► │ offline rollouts   │
└────────────────┘                 └─────────┬─────────┘
                                              │ return-based
                                              ▼ importance weights
                            ┌──────────────────────────┐
                            │ weighted SFT (no per-update│ ──► policy
                            │ generation)               │
                            └──────────────────────────┘
```

## Key points

- DRIFT exploits the equivalence between the KL-regularized RL objective and importance-weighted supervised learning. RL-quality behavior can be reached by reweighting fixed offline data.
- Rollouts are sampled ONCE from a fixed reference policy. There is no per-update trajectory generation, which is where online RL spends most of its compute.
- Each trajectory gets a return-based importance weight. The policy is then trained by weighted SFT on the fixed dataset.
- Reported to match or exceed multi-turn RL baselines while keeping SFT-level training cost and simplicity.
- Targets multi-turn deployment, where users or environments give lightweight corrective feedback across turns.

## Gaps in the study

- Importance weights derived from a fixed reference policy can have high variance once the trained policy drifts far from that reference.
- Benchmark breadth is unclear: how many multi-turn task families were tested.
- The paper does not fully characterize how stale the reference policy can get before re-sampling new rollouts becomes necessary.

## How it relates to prior wiki pages

DRIFT is the practical sibling of a thread the wiki has been tracking strongly: SFT as a special or degenerate case of RL.

- **GFT (2026-04-21)** proved that SFT is a degenerate case of policy gradient with a maximally sparse implicit reward. DRIFT lives on the same equivalence but turns it into an efficiency play rather than a theoretical reframing.
- **DAgger for LLM agents (2026-05-14)** diagnosed the SFT covariate-shift problem against RLVR's sparse-outcome problem, and recovered an on-policy distribution with dense teacher labels. DRIFT attacks the same covariate-shift weakness of plain SFT, but does it by importance-weighting offline data rather than re-querying a teacher.
- **VGF (2026-04-19)** reframed behavior-regularized RL as optimal transport. DRIFT and VGF both start from KL-regularized RL, but VGF asks where probability mass should move while DRIFT asks how to reweight already-sampled trajectories.

DRIFT's contribution to the thread: it exploits the same RL-equals-weighted-supervised-learning equivalence to get RL-quality multi-turn behavior at SFT cost, by decoupling rollout from update.

## Links

- Paper: [arxiv 2605.31455](https://arxiv.org/abs/2605.31455)
- Related concept pages: [rl-for-llms.md](rl-for-llms.md), [knowledge-distillation.md](../inference-efficiency/knowledge-distillation.md)
- Raw source: [raw/huggingface/2026-06-01-drift-decoupled-rollouts-and-importance-weighted-fine-tuning.md](../../raw/huggingface/2026-06-01-drift-decoupled-rollouts-and-importance-weighted-fine-tuning.md)
