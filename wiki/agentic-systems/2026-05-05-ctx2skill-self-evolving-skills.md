# Ctx2Skill: From Context to Skills — Self-Evolving Multi-Agent Skill Extraction

**Source:** HuggingFace Daily Papers, 2026-05-05
**Paper:** [arXiv:2604.27660](https://arxiv.org/abs/2604.27660) · [HF page](https://huggingface.co/papers/2604.27660)
**Raw:** [`raw/huggingface/2026-05-05-from-context-to-skills-can-language-models-learn-from-context-skillfully.md`](../../raw/huggingface/2026-05-05-from-context-to-skills-can-language-models-learn-from-context-skillfully.md)
**Tier:** 2 (agents, skill extraction, context learning)

## TL;DR

Long, technically dense contexts contain rules and procedures that a model could in principle extract as natural-language skills, but manual annotation is prohibitive and there is no external feedback to drive automated skill induction. Ctx2Skill is a self-play loop with three roles: a Challenger that generates probing tasks and rubrics from context, a Reasoner that solves them under an evolving skill set, and a neutral Judge that gives binary feedback. Both Challenger and Reasoner evolve through accumulated skills; dedicated Proposer and Generator agents analyze failures and synthesize targeted skill updates. A Cross-time Replay mechanism prevents adversarial collapse by selecting the skill set that balances best across representative cases. On four CL-bench tasks, Ctx2Skill consistently lifts solving rates across backbone models. Skills are model-agnostic and pluggable.

## Why it matters

Skill extraction is the bridge between long-context retrieval (the model has the document) and parametric knowledge (the model has internalized it). Most production systems handle long context by retrieval or by dumping the document into the prompt. Ctx2Skill argues for a third path: extract reusable natural-language skills from the document and plug them into any model. The pluggability claim is the load-bearing one — if it holds, skills become a portable artifact that can be cached, shared, and routed.

## Connections

- **Corpus2Skill (2026-04-18)** — the wiki's first paper on knowledge-to-skill conversion. Corpus2Skill operated on knowledge graphs; Ctx2Skill operates on raw context with self-play. Two papers, two routes to the same artifact (a natural-language skill that can be plugged into any model). The convergence is a pattern.
- **Intern-Atlas (2026-05-01)** — method-evolution graph that tracks how research methods evolve through use. Ctx2Skill's Cross-time Replay is structurally similar: keep the skill set that best generalizes across representative cases. Both papers use evolution-with-replay to prevent over-specialization.
- **AgenticQwen (2026-05-04)** — dual flywheels (reasoning + agentic). Ctx2Skill is a third flywheel pattern: skill extraction + skill selection + adversarial-collapse prevention. The recipe family is now three-strong: AgenticQwen's flywheels harden the model on its own errors; Ctx2Skill hardens the skill set on its own failures.
- **AHE (2026-05-04)** — agentic harness engineering treats decisions as contracts. Ctx2Skill's Judge role is the contract enforcer for skill updates: a skill is added only if the Judge confirms it improves the Reasoner. The two papers describe the same architectural pattern at different levels (system harness vs skill harness).

## Research angle

1. **Skills as routing inputs.** A skill set extracted from a document is a per-task capability profile. A router that knows which skills are relevant for a query could pick the model that best supports those skills. This is a per-task version of Hermes's `ModelCapabilities.structured_output` flag (Ch 15, 05-04).
2. **Skill caching and reuse.** Skills are pluggable across models. A team that extracts skills once and serves them to multiple model backends gets per-task transfer for free. The infrastructure is similar to MCP, but for skills rather than tools.
3. **Skill-level distillation.** If skills are pluggable, an open question is whether distilling them into model weights (rather than serving as prompt context) preserves the transfer. The composition with on-policy distillation (TIP, 04-16) is unmeasured.

## Open questions

- The Cross-time Replay mechanism prevents collapse on representative cases, but what counts as "representative" depends on the Challenger's distribution. If the Challenger systematically misses a region of the task space, the skill set will too.
- The Judge is described as "neutral binary feedback" — but binary feedback on skill quality is itself a dimension-collapse problem (the wiki's three-paper pattern: ViPO, Semi-DPO, Themis). Whether multi-criteria judgment helps Ctx2Skill is open.
- Skill drift over long sessions: the paper evaluates on CL-bench, which has bounded task scope. Behavior under continued use, where skills accumulate and may interfere, is not characterized.
