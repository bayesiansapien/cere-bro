# SCRL: Subproblem Curriculum Reinforcement Learning

**Date:** 2026-05-23
**arxiv:** [2605.22074](https://arxiv.org/abs/2605.22074)
**HF papers:** [https://huggingface.co/papers/2605.22074](https://huggingface.co/papers/2605.22074)
**Raw source:** [farmer/huggingface](../../raw/huggingface/2026-05-23-from-reasoning-chains-to-verifiable-subproblems-curriculum-r.md)

## TL;DR

Outcome-based RLVR (reinforcement learning from verifiable rewards, where the only reward signal is final-answer correctness) collapses on hard problems because correct rollouts are too rare to produce a usable gradient. SCRL derives a sequence of verifiable subproblems from each reference reasoning chain, fixes the last subproblem to be the original problem, and uses subproblem-level reward normalization to turn partial progress into a learning signal. On Qwen3-4B-Base, SCRL improves average accuracy on seven math benchmarks by +4.1 over GRPO (Group Relative Policy Optimization, the on-policy RL algorithm that DeepSeek used to train R1). On AIME24 and AIME25 it improves pass@1 by +3.7 and pass@64 by +4.6, evidence the gain is on exploration of hard problems specifically.

## Why this matters

Hard problems are a known dead zone for outcome-based RLVR: when no rollout is correct, every advantage estimate is the same and there is no gradient. SCRL solves this by decomposing the reward structure rather than the policy. Subproblems are easier than the whole, so rollouts hit positive reward more often, and the normalization happens per subproblem so the credit lands on the right span of the answer.

This is the third paper in 30 days that re-engineers the RLVR reward signal at a different level of the stack: [DelTA (today)](./2026-05-23-delta-discriminative-token-credit-rlvr.md) reweights tokens within an already-rewarded rollout; [uPRM (today)](./2026-05-23-unsupervised-process-reward-models.md) replaces the supervised PRM with an unsupervised one. SCRL replaces the binary outcome reward with a denser subproblem-level reward derived from the curriculum itself. Three independent attacks on the same problem in one day: outcome-based RLVR's sparse-gradient ceiling on hard reasoning.

The wiki has tracked this since the [04-18 LongAct paper](../inference-efficiency/2026-04-18-longact-saliency-sparse-rl.md) (the paper that showed long-context training signal is concentrated in the first 5% of tokens) and the [04-19 VGF paper](./2026-04-19-vgf-value-gradient-flow-rl.md) (which routed gradient through a transport budget). SCRL is the problem-level analogue: route the gradient through a curriculum of verifiable intermediate states.

## Mechanism

Given a reference reasoning chain for a hard problem, SCRL extracts a sequence of verifiable subproblems whose final element is the original problem. During RL, the policy attempts each subproblem; rewards are normalized independently at each subproblem position and advantages are attributed to the corresponding answer spans. The result is fine-grained credit assignment without external rubrics or auxiliary reward models.

Two design pieces:
1. **Subproblem extraction:** verifiable subgoals derived from the reference chain.
2. **Position-wise normalization:** rewards normalized at each subproblem position separately, so a problem that is hard everywhere but trivial at step 3 still produces a usable gradient at step 3.

## Key takeaways

- +4.1 average points over GRPO on seven math benchmarks (Qwen3-4B-Base).
- +1.9 average points on Qwen3-14B-Base (gain shrinks at larger scale, consistent with the gradient-dead-zone hypothesis).
- AIME24, AIME25, IMO-Bench: +3.7 pass@1, +4.6 pass@64 on Qwen3-4B-Base: pass@64 gain suggests better exploration, not just better single-shot accuracy.
- No external rubrics, no reward model: only the reference reasoning chain.

## Gaps

The +4.1 advantage shrinks to +1.9 on Qwen3-14B-Base. At 70B+ scale the benefit may disappear, since larger models have lower rollout failure rates on the same benchmarks. The dependence on the quality of the reference reasoning chain is undisclosed: if the subproblems are extracted from a teacher model whose intermediate reasoning is wrong, SCRL inherits the error. Composition with [uPRM](./2026-05-23-unsupervised-process-reward-models.md) (which scores intermediate steps without a reference) is not tested.

## Industrial implication

For any team training reasoning models under RLVR on math, code, or formal reasoning, SCRL is a drop-in upgrade that does not need extra annotations beyond the reference chains already used for SFT. Expect this pattern to converge with [uPRM](./2026-05-23-unsupervised-process-reward-models.md) (verifier-free) and [DelTA](./2026-05-23-delta-discriminative-token-credit-rlvr.md) (token-level reshape) into a single reasoning-RL recipe by mid-2026 H2.

## Research angle

The interesting open question is whether SCRL composes with on-policy distillation. If the subproblem curriculum is constructed from a teacher's reasoning chain, the student is effectively learning to imitate the teacher's intermediate states under an RL objective. Whether this hybrid SCRL+distill regime outperforms pure SCRL or pure distillation is the natural follow-up. A related angle: can the curriculum be generated by the policy itself rather than from a reference chain? Self-curriculum RLVR would close the loop entirely.

## Related wiki pages

- [DelTA (2026-05-23)](./2026-05-23-delta-discriminative-token-credit-rlvr.md).
- [Unsupervised PRMs (2026-05-23)](./2026-05-23-unsupervised-process-reward-models.md).
- [VGF: Value-Gradient Flow RL (2026-04-19)](./2026-04-19-vgf-value-gradient-flow-rl.md).
- [LongAct (2026-04-18)](../inference-efficiency/2026-04-18-longact-saliency-sparse-rl.md).
- [RLVR weak-supervision (2026-04-21)](./2026-04-21-rlvr-weak-supervision-reasoning-faithfulness.md).
