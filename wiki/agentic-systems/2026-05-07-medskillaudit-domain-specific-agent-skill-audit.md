# MedSkillAudit: Domain-Specific Audit Framework for Medical Research Agent Skills

**Source:** HuggingFace Daily Papers (2026-05-07)
**Paper:** [arXiv 2604.20441](https://arxiv.org/abs/2604.20441) · [HF](https://huggingface.co/papers/2604.20441)
**Raw:** [raw](../../raw/huggingface/2026-05-07-medskillaudit-domain-specific-audit-framework-medical-research.md)

## TL;DR

Agent skills are now deployed as modular, reusable capability units. Medical research skills need safeguards beyond general-purpose evaluation. MedSkillAudit is a layered, pre-deployment audit framework that scored 75 medical research skills across five categories against two human experts. System-expert agreement (ICC = 0.449) exceeded the human inter-rater baseline (0.300), and 57.3% of skills fell below the Limited Release threshold. Protocol Design showed the strongest agreement (ICC = 0.551). Academic Writing showed a negative ICC (-0.567), revealing a structural rubric-expert mismatch.

## Why it matters

This is the first audit framework specifically targeting **agent skill release readiness**, not agent capability or agent safety. Skills are reusable units. A bad skill scales linearly with deployment. The 57.3% rejection rate at the Limited Release threshold is the data point that matters: the majority of skills audited under this framework would not have been deployed had the framework been applied.

The Academic Writing negative ICC is the more interesting finding. When a rubric and human experts disagree systematically, the rubric is measuring a different construct than the experts are. For high-stakes generative tasks like academic writing, rubric-based audit may be structurally inadequate. This is a useful negative result that the broader skill-audit community needs to hear.

## Connections

Pairs with the Marcus production-agent security study (05-06). Marcus measured what goes wrong **after** deployment (91% tool-chaining vulnerability, 89.4% goal drift). MedSkillAudit measures what should be caught **before** deployment. Together they form a deployment-pipeline gate: pre-deployment audit (MedSkillAudit) plus post-deployment monitoring (the kind that the Marcus paper argues is missing).

Connects to Ctx2Skill (05-05). Ctx2Skill builds skills via self-play; MedSkillAudit gates skills at release. The pipeline implied by both papers: self-play generates candidate skills, audit framework filters before release, production monitoring catches what slips through.

The negative-ICC finding intersects the wiki's tracking of **rubric-expert mismatch** in evaluation. ProgramBench (05-06) saw 0% on every model. AcademiClaw (05-05) saw 55%. PhysicianBench (05-05) saw 46%. The mismatch tightens at the high end of difficulty and at the open-ended end of task type. Academic Writing is open-ended; the negative ICC is consistent with the broader pattern.

## Research angle

A skill-audit framework that adapts its rubric to the negative-ICC categories is missing. The paper identifies the failure (Academic Writing rubric-expert mismatch) but does not propose a remediation. A natural next step: replace the rubric with a structured human-in-the-loop scoring protocol for the categories where rubric-expert agreement fails.

## Related

- [agent-benchmarks.md](agent-benchmarks.md)
- [2026-05-05-ctx2skill-self-evolving-skills.md](2026-05-05-ctx2skill-self-evolving-skills.md)
- [2026-05-05-physicianbench-ehr-agents.md](2026-05-05-physicianbench-ehr-agents.md)
