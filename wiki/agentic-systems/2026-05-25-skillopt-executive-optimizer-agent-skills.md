# SkillOpt: a deep-learning-style optimizer for agent skills

**arXiv:** [2605.23904](https://arxiv.org/abs/2605.23904) · **HF Daily Papers:** [page](https://huggingface.co/papers/2605.23904) · **Date:** 2026-05-25
**Authors:** Yifan Yang, Xuemei Gao, Qi Dai, Bei Liu, Kai Qiu, Yuqing Yang, Dongdong Chen, Chong Luo (Microsoft) with co-authors at Shanghai Jiao Tong, Tongji, Fudan
**Raw:** [farmer file](../../raw/huggingface/2026-05-25-skillopt-executive-strategy-for-self-evolving-agent-skills.md)

## TL;DR

SkillOpt is the first systematic, controllable text-space optimizer for agent skills. A separate optimizer model takes scored rollouts and emits bounded add/delete/replace edits on a single skill document; an edit is accepted only when it strictly improves held-out validation. A textual learning-rate budget, a rejected-edit buffer, and slow/meta epoch updates make the training loop reproducible. Zero inference-time overhead at deployment. Across 6 benchmarks, 7 target models, and 3 harnesses (direct chat, Codex, Claude Code), SkillOpt is best or tied on all 52 (model, benchmark, harness) cells. On GPT-5.5 it lifts no-skill accuracy by +23.5 in direct chat, +24.8 inside Codex, +19.1 inside Claude Code. Skills transfer across model scales and execution environments.

## Key claims

- The frame is: the skill is the external state of a frozen agent, and that external state should be trained with the same discipline as weight-space optimization (learning rate, validation gate, structured updates, rejected-edit buffer).
- The optimizer is a separate model from the agent itself; it consumes scored rollouts and emits bounded edits on a single `best_skill.md`.
- The validation gate is the key control: an edit is accepted only when it strictly improves the held-out validation score. This prevents the optimizer from churning the skill document and making it incoherent.
- Slow/meta updates at epoch granularity prevent over-fitting to within-epoch sample noise.
- The benchmark grid is unusually thorough: 52 cells covering 6 benchmarks, 7 target models, and 3 execution harnesses. SkillOpt is best or tied on every cell.
- Headline numbers on GPT-5.5: +23.5 direct chat, +24.8 inside Codex, +19.1 inside Claude Code.
- Transfer: a skill optimized on one model and one harness retains value when moved to a different scale or to a different harness, and to a nearby math benchmark without further optimization.
- Zero deployment overhead because the skill is just a text artifact.

## Relation to prior wiki content

SkillOpt is the second paper in May to operationalize the "external state is trainable" frame, joining the [Life-Harness](2026-05-23-code-as-agent-harness.md) thread from 05-23 (the code-as-agent-harness survey that argued the runtime interface, not the model weights, is the right design surface for agent improvement). Life-Harness evolved the *harness* from trajectories. SkillOpt evolves the *skill document* from trajectories. Both keep the LLM frozen. Both make the external state the trainable surface. The two papers together establish a clean two-axis taxonomy: harness (the wrapper) and skill (the procedural knowledge), each independently trainable, each independently transferable.

It is also the third paper in May on disciplined text-space optimization, joining [GEPA](2026-04-16-trex-llm-finetuning-automation.md)-style prompt optimization and [EvoSkill](2026-05-05-ctx2skill-self-evolving-skills.md). SkillOpt's contribution over these is the validation gate plus the rejected-edit buffer; both are direct imports from deep-learning optimization, and both are what make the training loop stable. Without them, prior text-space optimizers degenerate as the skill document grows.

The transfer claim is the most consequential. If a skill optimized on Qwen-7B transfers to GPT-5.5 inside Claude Code without retraining, the cost-of-deployment model for agentic systems flips. The skill becomes a portable artifact like a model checkpoint, not a per-model-per-environment fixture. Combined with [SDAR](2026-05-15-sdar-self-distilled-agentic-rl.md) (the 05-15 self-distilled agentic RL paper) and the [code-as-agent-harness](2026-05-23-code-as-agent-harness.md) thread, the picture is that agent intelligence is now decomposing into a stable model + portable harness + portable skill stack.

## Research angle

The validation gate is the load-bearing mechanism. Without it the optimizer drifts. The paper's gate is binary (strict improvement on validation); a probabilistic gate based on uncertainty would likely be tighter and would suggest a Bayesian-optimization analog for text-space optimization. Worth a follow-up.

A second open question: how does the rejected-edit buffer interact with the meta updates? The paper treats them as orthogonal controls, but a rejected edit at one epoch might be the right edit two epochs later (after other edits have been accepted). A learned policy over the buffer would be the natural next step.

The transfer claim deserves stress testing on real production loads. Microsoft is well-positioned to run that test; the lift on Codex (+24.8) suggests this is being prepared for production deployment in their coding tools.
