# AcademiClaw: When Students Set Challenges for AI Agents

**Source:** HuggingFace Daily Papers, 2026-05-05
**Paper:** [arXiv:2605.02661](https://arxiv.org/abs/2605.02661) · [HF page](https://huggingface.co/papers/2605.02661)
**Raw:** [`raw/huggingface/2026-05-05-academiclaw-when-students-set-challenges-for-ai-agents.md`](../../raw/huggingface/2026-05-05-academiclaw-when-students-set-challenges-for-ai-agents.md)
**Tier:** 2 (agent benchmark, academic-level coverage)

## TL;DR

OpenClaw ecosystem extension: 80 multi-step tasks curated from 230 real student submissions across more than 25 academic domains, spanning olympiad math, linguistics, GPU-intensive RL, and full-stack debugging. Each task runs in a Docker sandbox with multi-dimensional rubric scoring (six techniques) plus a five-category safety audit. Best of six advanced models: 55% success rate. Capability varies sharply across domains; computational resource consumption does not predict output quality.

## Why it matters

AcademiClaw widens the agent-benchmark cluster into academic-level tasks: not assistant productivity (OccuBench) or clinical workflow (PhysicianBench), but the kind of work a senior undergraduate or graduate student would face. The 55% ceiling is consistent with the wiki-tracked cross-benchmark pattern: frontier agents fail multi-step real tasks at 30–50% rates regardless of domain. The "compute does not predict output" finding is the load-bearing one — it argues against the current default that more thinking tokens equal better results.

## Connections

- **Agent benchmarks cluster** — eighth benchmark in the cluster (after OccuBench, GTA-2, DR3-Eval, PRL-Bench, Claw-Eval-Live, InteractWeb-Bench, PhysicianBench). The compute-decoupling finding is novel relative to the prior seven.
- **PRL-Bench (2026-04-20)** — physics research benchmark, also derived from real expert work. AcademiClaw is the broader-domain analogue. The shared methodology (real human work as ground truth) is a contrast with synthetic benchmark generation.
- **InteractWeb-Bench (2026-05-01)** — blind execution failure mode. AcademiClaw's open-ended student tasks are a natural setting for blind execution: students often write underspecified problem statements, and an agent that does not clarify will guess wrong. Whether AcademiClaw grades this dimension is not clear from the abstract.
- **Compute-quality decoupling** — connects to Marcus's "code that compiles is not correct code" thesis (05-01), the ARC-AGI-3 systematic-errors paper (05-03), and the Pi/Pragmatic Engineer "vibe slop" theme (04-29). All four observations cluster around the same complaint: compute-as-quality-proxy fails.

## Research angle

1. **Domain-conditional routing on AcademiClaw.** "Significant capability variations across task domains" is a routing signal: a router that dispatches olympiad math to one model and full-stack debugging to another should beat any single best model. The benchmark's 25+ domains make this measurable.
2. **Compute-decoupling investigation.** If compute does not predict quality, what does? Trajectory shape, tool diversity, or some other measurable trajectory feature. AcademiClaw's task-level resource data should permit a regression study.
3. **Safety-audit-as-routing-input.** The five-category safety audit produces a per-task safety profile. A router that consults this profile could allocate safety-critical tasks to safer models.

## Open questions

- 80 tasks is small for cross-domain analysis at 25+ domains: 3 tasks per domain on average. Statistical power for per-domain claims is limited.
- The "behavioral patterns" finding is intriguing but underspecified in the abstract; the model-cards section presumably has details on which models exhibit which patterns.
- Whether AcademiClaw is *contaminated* with task material that overlaps with student internet writing is the standard challenge for "real student submission" benchmarks.
