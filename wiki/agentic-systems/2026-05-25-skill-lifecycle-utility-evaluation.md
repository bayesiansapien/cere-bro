# From Raw Experience to Skill Consumption: a utility-grounded study of the model-generated skill lifecycle

**arxiv:** [2605.23899](https://arxiv.org/abs/2605.23899) · **HF:** [papers/2605.23899](https://huggingface.co/papers/2605.23899) · **Raw:** [farmed](../../raw/huggingface/2026-05-25-from-raw-experience-to-skill-consumption-a-systematic-study.md)

## TL;DR

Language agents increasingly improve by reusing skills (structured procedural artifacts distilled from past experience). Model-generated, domain-level skills are particularly attractive because they scale beyond hand-crafting and adapt fast within a domain. But the field has no comprehensive study of the full lifecycle (experience generation, skill extraction, skill consumption). The authors build a utility-grounded evaluation framework across five agentic task domains and find: (a) model-generated skills are beneficial on average but exhibit non-trivial negative transfer; (b) neither extractors nor target consumers behave uniformly; a model can be a strong extractor and a weak consumer, or vice versa; (c) skill utility is independent of model scale or baseline task strength. They dissect each lifecycle stage and translate the findings into a concrete meta-skill that guides extraction toward features tied to actual utility, reducing negative transfer.

## Why this matters

This is the companion paper to SkillOpt ([2026-05-25-skillopt-text-space-optimizer-skills.md](2026-05-25-skillopt-text-space-optimizer-skills.md), today's other agent-skills paper that treats the skill document as the trainable parameter). SkillOpt is the optimization framework; this paper is the empirical study of what the optimization target should actually look like. Both papers landing the same day says the field has converged on agent-skills-as-engineering-substrate, just as the harness-engineering thesis converged in late May. SkillOpt and this paper define the surface a third paper will eventually unify.

The negative-transfer finding is the load-bearing empirical result. Skills extracted from one model and consumed by another sometimes hurt rather than help. The non-uniform-extractor / non-uniform-consumer asymmetry is the structural reason: extraction quality and consumption quality are separate competencies. A model can be excellent at distilling experience into a skill (because it has good introspection) and still be a poor consumer of skills (because it does not retrieve and apply them efficiently). The reverse also holds.

The meta-skill that guides extraction toward utility-correlated features is the practical takeaway. The paper does not just diagnose the problem; it shows that a hand-written meta-skill (call it "extract like this and only this") reduces negative transfer across domains. That makes the meta-skill itself the artifact worth iterating on.

## Where this fits

Three skill-related papers in three weeks:
1. **SKILL.md semantic supply-chain attacks (2026-05-23):** adversarial weakness of skill marketplaces. (36.5-100% governance evasion.)
2. **SkillOpt (today):** principled optimizer for skill documents. Best-or-tied on 52 of 52 (model, benchmark, harness) cells.
3. **Skill lifecycle utility evaluation (today, this paper):** empirical study of when and why skills work or fail; meta-skill for utility-guided extraction.

The triangulation is now complete. Skills are the new code, optimizable artifacts that need versioning, evaluation, security, and an optimization theory. Each of the three papers handles one corner of that triangle.

## Open research angles

- The meta-skill is hand-authored. Can SkillOpt's text-space optimizer learn a meta-skill that beats the hand-written one?
- The paper finds skill utility independent of model scale. If true, then small models could specialize in extraction (cheap) while large models do consumption (where they have the broader baseline). The asymmetry is an economic lever.
- Negative transfer is non-trivial. Whether utility-guided extraction can be combined with consumer-aware filtering (skip skills predicted to hurt this consumer) is the next ablation.

## Industrial implication

Anthropic Skills, Claude Code SKILL.md, Cursor rules, OpenAI custom GPTs all rely on user-authored skills today. This paper says even when extraction is automated, the extracted skill can hurt the consumer. The deployment recipe should include a per-consumer utility filter before a skill is applied. Combined with the SKILL.md security paper, the marketplace gating function needs *three* checks: utility-correlated content (this paper), consumer compatibility (this paper), and adversarial safety (the 2026-05-23 supply-chain paper).

## Related wiki pages

- [2026-05-25-skillopt-text-space-optimizer-skills.md](2026-05-25-skillopt-text-space-optimizer-skills.md) — companion optimizer paper
- [2026-05-23-skill-md-supply-chain-attacks.md](../responsible-ai/2026-05-23-skill-md-supply-chain-attacks.md) — adversarial skill marketplaces
