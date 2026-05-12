# DeltaRubric: Generative Multimodal Reward Modeling via Joint Planning and Verification

**Date:** 2026-05-12
**Source:** HuggingFace Daily Papers
**arXiv:** [2605.09269](https://arxiv.org/abs/2605.09269)
**Tier:** 2 — Multimodal reward modeling / RLHF / vision-language

## TL;DR

Multimodal reward models suffer from **lazy judging**: single-step evaluators exploit language priors over fine-grained visual verification. DeltaRubric reformulates multimodal preference evaluation as plan-and-execute inside one MLLM. The model first acts as a **Disagreement Planner**, generating a neutral, instance-specific verification checklist. Then it transitions to a **Checklist Verifier**, executing the self-generated checks against the image and question to produce a grounded judgment. Trained as multi-role reinforcement learning with joint optimization of planning and verification. On VL-RewardBench, base-model overall accuracy improves by +22.6 points (4B) and +18.8 points (8B) over no-rubric baselines.

## Why it matters

Lazy judging is the multimodal-RM equivalent of mode collapse in generative models: the model finds a high-reward shortcut that ignores the modality the reward is supposed to gate on. DeltaRubric breaks the shortcut by forcing the model to write down what it intends to check *before* it does the check. The 22.6-point gain on VL-RewardBench is large and consistent with the gains AlphaXIV-style external rubric methods deliver in pure text. The novelty is the joint optimization: planning and verification share a single MLLM trained as a multi-role RL problem.

## How it relates to prior wiki state

- **Auto-Rubric as Reward / ARR (today).** Same architectural diagnosis. ARR externalizes rubrics upstream of policy training. DeltaRubric externalizes them inside the reward model itself as plan-then-verify. The two papers bracket the rubric-as-reward design space: training-side externalization (ARR) and inference-side decomposition (DeltaRubric).
- **RationalRewards (2026-04-16).** Same plan-then-execute logic. RationalRewards used Generate-Critique-Refine at inference time. DeltaRubric trains the planner and verifier roles end-to-end with RL. The pattern of "split judgment into a structured sequence of operations" is now five papers strong across multimodal and text domains.
- **ROMA (today, Reinforcing Multimodal Reasoning Against Visual Degradation).** Both papers modify the RL fine-tuning dynamics for MLLMs. ROMA addresses *robustness* to corrupted inputs, DeltaRubric addresses *fidelity* of the reward signal. Composing them is the natural next experiment: a DeltaRubric reward inside a ROMA-stabilized RL loop.

## Research angle

The 4B-vs-8B gap is informative. 4B gains 22.6 points, 8B gains 18.8. Diminishing returns from plan-and-execute as base capability grows, which suggests this is a scaffolding intervention rather than a capability intervention. The interesting question: at what model scale does plan-and-execute become net-zero or net-negative against a stronger one-shot judge? If the crossover is observable, the multimodal-RM design choice becomes scale-conditional, and the field can stop debating "is rubric-based reward better" and start asking "at which scale does it help."

## Links

- [Paper (arXiv)](https://arxiv.org/abs/2605.09269)
- [HuggingFace page](https://huggingface.co/papers/2605.09269)
- Raw source: [raw/huggingface/2026-05-12-deltarubric-generative-multimodal-reward-modeling-via-joint.md](../../raw/huggingface/2026-05-12-deltarubric-generative-multimodal-reward-modeling-via-joint.md)

## Related wiki pages

- [Auto-Rubric as Reward](2026-05-12-auto-rubric-as-reward-arr.md)
- [RationalRewards](2026-04-16-rationalrewards-visual-generation.md)
- [ROMA: reinforcing multimodal reasoning against degradation](2026-05-12-roma-visual-degradation.md)
