# Rebellious Student: Reversing Teacher Signals for Reasoning Exploration with Self-Distilled RLVR

**Date:** 2026-05-12
**Source:** HuggingFace Daily Papers
**arXiv:** [2605.10781](https://arxiv.org/abs/2605.10781)
**Tier:** 2 — RL for LLMs / reasoning / self-distillation

## TL;DR

In self-distillation, a teacher conditioned on extra information guides a student that does not have that information. The standard read of this signal is: when the student fails, follow the teacher. The paper's flip is to read the signal in reverse: when the student *succeeds* along a path the teacher would not have predicted, those tokens reflect the student's own reasoning, and they are the right exploration signal for RLVR. The method, RLRT, augments GRPO by reinforcing exactly those tokens on correct rollouts. Across base, instruction-tuned, and thinking-tuned Qwen3 checkpoints, RLRT beats both self-distillation and exploration-based baselines.

## Why it matters

The exploration story in RLVR has been stuck on diversity proxies (entropy bonuses, KL constraints, uniform sampling) that are not grounded in what the model is actually trying to do. RLRT proposes a principled exploration axis: information asymmetry between teacher and student. When the student finds a correct trajectory the teacher would not have predicted, the student is by definition exploring outside the teacher's posterior, and the rollout is correct, so the exploration paid off. Reinforce those tokens specifically. That moves exploration from a regularizer to a structural feature of self-distillation.

## How it relates to prior wiki state

- **PreRL / DSRL (2026-04-16).** Both papers argue that RL post-training should reinforce a specific subset of tokens or paths, not uniform diversity. PreRL works at the marginal distribution P(y), RLRT works at the token level inside rollouts. Same diagnosis from different layers.
- **LongAct (2026-04-18).** LongAct concentrated RL gradient updates on saliency-peak positions. RLRT concentrates them on teacher-disagreement positions. Two different definitions of "where to train," same overall move: identify the small set of locations doing real work and put the budget there. The thread from TIP (04-16, only 10% of distillation tokens carry signal) is now four papers deep.
- **VGF / Value Gradient Flow (2026-04-19).** VGF posed test-time exploration as a transport-budget question, and the [Worth Watching prediction from 04-19](../daily-digest/2026-04/2026-04-19.md) was that the next paper to formalize selective exploration would do so on the training side. RLRT is one of those follow-ups: it formalizes exploration on the rollout side via teacher-student information asymmetry. Partial resolution of the prediction.
- **GFT / SFT-as-degenerate-RL (2026-04-21).** GFT proved SFT is a degenerate case of policy gradient with single-path dependency. RLRT extends self-distillation in a similar move, by reading the same teacher signal differently and getting a non-degenerate gradient on correct rollouts.

## Research angle

Information asymmetry as a design axis opens several knobs. The teacher can be conditioned on hints, gold labels, retrieved evidence, or future tokens. Each defines a different version of "tokens the student found on its own." The paper uses one specific construction; the broader question is whether the *kind* of information asymmetry matters or whether any well-defined asymmetry yields the same exploration benefit. A related angle: how does this interact with G-Zero (also today), which derives reward from the predictive shift between an unhinted student and a hinted version of itself? G-Zero and RLRT both read teacher-student deltas, but RLRT reinforces the student's discoveries while G-Zero uses the delta as the reward signal directly. Composing them is the obvious experiment.

## Links

- [Paper (arXiv)](https://arxiv.org/abs/2605.10781)
- [HuggingFace page](https://huggingface.co/papers/2605.10781)
- Raw source: [raw/huggingface/2026-05-12-rebellious-student-reversing-teacher-signals-for-reasoning-e.md](../../raw/huggingface/2026-05-12-rebellious-student-reversing-teacher-signals-for-reasoning-e.md)

## Related wiki pages

- [RL for LLMs concept page](rl-for-llms.md)
- [Knowledge Distillation concept page](../inference-efficiency/knowledge-distillation.md)
- [PreRL / DSRL](2026-04-16-prerl-rl-in-pretrain-space.md)
- [LongAct: saliency-guided sparse RL](../inference-efficiency/2026-04-18-longact-saliency-sparse-rl.md)
- [VGF: Value Gradient Flow RL](2026-04-19-vgf-value-gradient-flow-rl.md)
