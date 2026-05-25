# SkillOpt: text-space optimizer for self-evolving agent skills

**arxiv:** [2605.23904](https://arxiv.org/abs/2605.23904) · **HF:** [papers/2605.23904](https://huggingface.co/papers/2605.23904) · **Raw:** [farmed](../../raw/huggingface/2026-05-25-skillopt-executive-strategy-for-self-evolving-agent-skills.md)

## TL;DR

Agent skills today are either hand-crafted, one-shot LLM-generated, or evolved through loosely controlled self-revision. None behaves like a deep-learning optimizer. SkillOpt is a systematic controllable text-space optimizer for agent skills. A separate optimizer model turns scored rollouts into bounded add/delete/replace edits on a single skill document; each edit is accepted only when it strictly improves a held-out validation score. A textual learning-rate budget, a rejected-edit buffer, and an epoch-wise slow/meta update keep training stable while adding zero inference-time model calls. Across six benchmarks, seven target models, and three execution harnesses (direct chat, Codex, Claude Code), SkillOpt is best-or-tied on all 52 (model, benchmark, harness) cells and beats every per-cell competitor including human-written skills, one-shot LLM skills, Trace2Skill, TextGrad, GEPA, and EvoSkill. On GPT-5.5 it lifts no-skill accuracy by +23.5 points in direct chat, +24.8 inside Codex, +19.1 inside Claude Code. Optimized skills transfer across model scales, between Codex and Claude Code execution environments, and to a nearby math benchmark without further optimization.

## Why this matters

SkillOpt is the first paper to treat the skill artifact as the trainable parameter and a frozen agent as the inference layer, with the discipline of weight-space optimization. The recognition is exactly the inversion that the Code-as-Agent-Harness thesis ([2026-05-23-code-as-agent-harness.md](2026-05-23-code-as-agent-harness.md), the survey arguing that harness is a first-class research object not glue around an LLM) and Life-Harness from the 2026-05-23 Twitter retweet (the runtime-harness paper that improved frozen LLM agents 88.5% by modifying the harness rather than the model) made for the *runtime* layer. SkillOpt makes the same move for the *skill* layer: the artifact around the frozen model is the optimization target.

Three design choices that matter:
1. **Held-out validation gate.** Edits are accepted only when they strictly improve validation. This is text-space gradient descent with a hard line-search.
2. **Textual learning-rate budget plus rejected-edit buffer.** The optimizer has a bounded step size and a memory of rejected directions. This is the analog of momentum and learning-rate schedules in weight space.
3. **Slow/meta update.** Epoch-wise meta-step composes accepted edits at a slower cadence, preventing high-frequency noise from dominating.

The cross-harness transfer result is the load-bearing generality claim. A skill optimized inside Codex transfers to Claude Code and to direct chat. That says SkillOpt is recovering harness-invariant structure, not Codex-specific tricks.

## Where this fits

There are now three papers all making the same architectural move in three weeks. Together they form a pattern.

1. **Life-Harness (2026-05-23, via Twitter):** modify the runtime harness around a frozen LLM. 88.5% average relative improvement.
2. **Code-as-Agent-Harness (2026-05-23):** treat the harness as a first-class research object, not glue.
3. **SkillOpt (today):** treat the skill document as the trainable artifact; optimize it like a weight matrix.

The unified recognition: the model is frozen, the substrate around it is the design surface. This is the agent-systems analog of the routing-and-control-surface theme that 2026-05-24's KVServe established for inference and that today's DAR paper ([2026-05-25-dar-diffusion-adaptive-routing.md](../ai-routing/2026-05-25-dar-diffusion-adaptive-routing.md), which makes residual aggregation a learned, timestep-adaptive routing schedule) establishes for diffusion. The wiki is now tracking a meta-pattern: every static schedule in the system is becoming a learned controller.

## Open research angles

- SkillOpt validates that text-space optimization works at the skill-document level. Whether it extends to multi-skill compositions (the meta-skill that decides which skill applies to a query) is the next layer.
- The skill artifact transfers across harnesses. Whether it transfers across model families (GPT-5.5 to Claude Opus to open-weight Qwen3.6) is partially shown but needs more rigorous test.
- SkillOpt has zero inference-time overhead. The optimizer model is run only at training. If a *small* optimizer model can drive a *large* agent's skill artifact, the asymmetry is the basis for a new training cost curve.

## Industrial implication

Every agent framework that lets users author skills (Anthropic Skills, Claude Code SKILL.md, Cursor rules, OpenAI custom GPTs) has a hand-authoring user experience today. SkillOpt is the first credible path to *automated* skill authoring with a guarantee that the authored skill is at least as good as the human one. Combined with the 2026-05-23 SKILL.md supply-chain-attack paper ([2026-05-23-skill-md-supply-chain-attacks.md](../responsible-ai/2026-05-23-skill-md-supply-chain-attacks.md), which found 36-100% governance evasion in skill marketplaces), the policy question becomes how to certify automatically-optimized skills before deploying them in a marketplace.

## Related wiki pages

- [2026-05-25-skill-lifecycle-utility-evaluation.md](2026-05-25-skill-lifecycle-utility-evaluation.md) — same-day companion paper on the full skill lifecycle
- [2026-05-23-code-as-agent-harness.md](2026-05-23-code-as-agent-harness.md)
- [2026-05-23-skill-md-supply-chain-attacks.md](../responsible-ai/2026-05-23-skill-md-supply-chain-attacks.md)
