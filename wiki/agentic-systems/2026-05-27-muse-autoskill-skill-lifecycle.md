# MUSE-Autoskill: Lifecycle-Managed Self-Evolving Skills

**Source:** HuggingFace daily papers (2026-05-27, 6 upvotes) · arxiv 2605.27366
**arxiv:** [2605.27366](https://arxiv.org/abs/2605.27366)
**Date:** 2026-05-27
**Raw:** [raw/huggingface/2026-05-27-muse-autoskill-self-evolving-agents-via-skill-creation-memor.md](../../raw/huggingface/2026-05-27-muse-autoskill-self-evolving-agents-via-skill-creation-memor.md)
**Tier:** 2 (agentic systems, skill evolution)

## TL;DR

Existing skill-creation methods treat skills as isolated, static artifacts, which caps reusability and long-term improvement. MUSE-Autoskill (Memory-Utilizing Skill Evolution) manages skills under a unified lifecycle: creation on demand, memory, management/selection, evaluation via unit tests and runtime feedback, and refinement. It adds skill-level memory that accumulates per-skill experience across tasks. On SkillsBench it shows initial evidence that lifecycle-managed skills improve task success, efficiency, reuse, and cross-agent transfer.

## Key points

- **Skills as long-lived, testable assets**, not one-off artifacts: each skill carries accumulated experience and is validated by unit tests plus runtime feedback before reuse.
- **Full lifecycle** (create, store, select, evaluate, refine) rather than just creation.
- **Cross-agent transfer** is an explicit target and an evaluated dimension.

## Relation to prior wiki state

MUSE-Autoskill is the constructive counter-move in the skill-evolution debate the wiki has been tracking. [SkillEvolBench (05-26)](2026-05-26-skillevolbench-episodic-to-procedural-skills.md) delivered the harsh result: distilled skills under-transfer versus raw-trajectory reuse, and larger skill libraries hurt. MUSE-Autoskill's answer is that the failure is one of *lifecycle management*, not of the skill abstraction itself: if skills are unit-tested, refined from runtime feedback, and carry per-skill memory, the clutter and drift that SkillEvolBench blamed for the negative result are managed away. Whether lifecycle management actually beats raw-trajectory reuse on SkillEvolBench's frozen-deployment-under-context-shift protocol is the test it has not yet run (it evaluates on SkillsBench instead). It also pairs with SkillOpt (05-25, treat the skill document as a trainable parameter): SkillOpt optimizes the skill's text, MUSE-Autoskill manages the skill's lifecycle, and the open question is whether either survives SkillEvolBench's frozen deployment.

## Gaps

Evaluated on SkillsBench, not the adversarial SkillEvolBench protocol, so it does not yet refute the negative result it implicitly responds to. "Initial evidence" framing signals early-stage results.

## Links

- [Paper](https://arxiv.org/abs/2605.27366)
- Raw: [raw/huggingface/2026-05-27-muse-autoskill-self-evolving-agents-via-skill-creation-memor.md](../../raw/huggingface/2026-05-27-muse-autoskill-self-evolving-agents-via-skill-creation-memor.md)
- Related: [SkillEvolBench 2026-05-26](2026-05-26-skillevolbench-episodic-to-procedural-skills.md)
