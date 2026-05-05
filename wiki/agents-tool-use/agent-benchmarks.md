# Agent Evaluation & Benchmarks

A growing ecosystem of benchmarks specifically designed for agentic AI — measuring not just accuracy but exploration/exploitation, long-horizon task completion, tool use, robustness, and professional domain coverage.

## Current State (as of 2026-05-05)

Standard LLM benchmarks underserve agents. The field has been building agent-specific eval frameworks across several dimensions: decision-making quality, professional domain coverage, multimodal grounding, and robustness under fault injection. **Eight benchmarks (OccuBench, GTA-2, DR3-Eval, PRL-Bench, Claw-Eval-Live, InteractWeb-Bench, AcademiClaw, PhysicianBench) now report frontier-agent failure rates of 30–55% on realistic multi-step tasks.** This is no longer a coincidence: it is a consistent cross-domain measurement spanning general workflow (Claw-Eval-Live, OccuBench), web (InteractWeb-Bench), professional research (PRL-Bench), academic challenges (AcademiClaw, 2026-05-05), and clinical workflow (PhysicianBench, 2026-05-05).

## Key Benchmarks

**OccuBench (2026-04-16)** — 100 tasks across 65 professional domains using Language World Models (LWMs) to simulate environments. Key finding: no single model dominates all industries; implicit faults are hardest. → [summary](2026-04-16-occubench.md)

**Exploration/Exploitation Measurement (2026-04-16)** — Policy-agnostic metric for explore/exploit errors in LM agents on 2D grid environments. Reasoning models perform best; harness engineering meaningfully improves both dimensions. → [summary](2026-04-16-exploration-exploitation-lm-agents.md)

**GameWorld (2026-04-16)** — 34 browser games, 170 tasks, state-verifiable outcomes for MLLM game agents. Best models still far below human. → [summary](../multimodal/2026-04-16-gameworld-multimodal-game-agents.md)

**MERRIN (2026-04-16)** — Search-augmented agent benchmark with noisy multimodal web evidence. Average accuracy 22.3%; agents over-rely on text modalities. → [summary](../multimodal/2026-04-16-merrin-multimodal-retrieval.md)

**InfiniteScienceGym (2026-04-16)** — Procedurally generated scientific analysis benchmark. No model exceeds 45%; abstention on unanswerable questions is a key weakness. → [summary](../llms-foundation-models/2026-04-16-infinitesciencegym-benchmark.md)

**DR3-Eval (2026-04-18)** — Deep Research Agent benchmark. Static per-task corpus sandboxes with evidential sources, confounding documents, and noise. Reverse-constructed questions (derived from verified evidential docs) ensure every task is answerable. Multi-dimensional scoring: recall, factual accuracy, citation coverage, instruction following, depth. State-of-the-art models still struggle. → [summary](2026-04-18-dr3-eval-deep-research-benchmark.md)

**GTA-2 (2026-04-20)** — Two-tier benchmark: GTA-Atomic (single-step tool precision) and GTA-Workflow (long-horizon, open-ended multi-tool coordination). Key results: frontier models below 50% on atomic tasks; top models at 14.39% on workflows. Critical finding: execution harness design (Manus, OpenClaw) matters more than underlying model capability. Uses real user queries and deployed tools — not synthetic evals. Recursive checkpoint-based evaluation for open-ended tasks. → [summary](2026-04-20-gta-2-tool-agent-benchmark.md)

**PRL-Bench (2026-04-20)** — Physics Research by LLMs benchmark. 100 tasks from Physical Review Letters papers (Aug 2025+, post-training cutoff for most models). Covers 5 subfields: astrophysics, condensed matter, high-energy, quantum information, statistical physics. Tasks replicate authentic research: exploration-oriented formulation, long-horizon workflows, verifiable outcomes. All frontier models score below 50%. Expert-validated. → [summary](2026-04-20-prl-bench-physics-benchmark.md)

**Claw-Eval-Live (2026-05-01)** — First *live* workflow-agent benchmark. Refreshable signal layer (ClawHub Top-500 skills, updated each release) + reproducible release snapshot (frozen fixtures, services, graders). 105 tasks, 13 frontier models, deterministic + structured-LLM grading on execution traces, audit logs, service state, post-run artifacts. Best model: 66.7%; no model reaches 70%. HR / management / multi-system business workflows persistently fail. → [summary](2026-05-01-claw-eval-live-agent-benchmark.md)

**InteractWeb-Bench (2026-05-01)** — First benchmark to grade *clarifying behavior* explicitly. Four user-agent personas + persona-driven instruction perturbations from RE defect taxonomies. Unified agent action space: Clarify / Implement / Verify / Submit. Frontier MLLM agents remain trapped in **blind execution** — generating code that satisfies their misreading of the instruction without ever asking. → [summary](2026-05-01-interactweb-bench-blind-execution.md)

**AcademiClaw (2026-05-05)** — Bilingual academic-level benchmark, 80 multi-step tasks curated from 230 real student submissions across 25+ professional domains (olympiad math, linguistics, GPU-intensive RL, full-stack debugging). Docker sandbox per task; six-technique multi-dimensional rubric scoring + five-category safety audit. Best of six advanced models: 55%. Capability varies sharply across domains; **compute does not predict output quality** — argues against current "more thinking tokens equal better results" defaults. → [summary](2026-05-05-academiclaw-student-tasks.md)

**PhysicianBench (2026-05-05)** — 100 long-horizon physician tasks from real consultation cases inside an EHR environment with vendor APIs. 21 specialties; ~27 tool calls per task. Best closed-source model: 46% pass@1. Best open-source: 19%. Highest tool-call horizon in any of the eight benchmarks; the gap between knowledge tests (where LLMs match physicians) and EHR-mediated workflows (where they do not) is the load-bearing finding. → [summary](2026-05-05-physicianbench-ehr-agents.md)

## Patterns Across Benchmarks

- Reasoning models consistently outperform base models on agentic tasks
- Over-exploration is a common failure mode in strong models
- Professional/domain-specific tasks expose different weaknesses than general benchmarks
- Deterministic environment generation (OccuBench, InfiniteScienceGym) removes publication bias
- **Execution harness dominates model capability** (GTA-2): the scaffold around the model determines workflow completion more than model capability itself. Confirmed empirically by the Ridge Security pentester benchmark (2026-05-04) at constant model: belief state, evidence-as-invariant, and trust propagation account for >5x finding gaps between architectures using the same Gemini 3 Flash backbone.
- Eight benchmarks now converge on the same finding: frontier models fail realistic multi-step tasks reliably — this is a consistent, cross-domain measurement
- **Middle-band discrimination** (Claw-Eval-Live, 05-01): models with similar pass rates diverge in overall completion, suggesting per-task-family routing could outperform any single model
- **Blind execution** (InteractWeb-Bench, 05-01): a distinct, named failure mode where agents guess rather than clarify under ambiguous instructions — the first benchmark to grade this dimension explicitly
- **Compute-quality decoupling** (AcademiClaw, 2026-05-05): computational resource consumption does not predict output quality across 80 academic-level tasks. The compute-as-proxy default is empirically broken
- **Long-horizon tool-call gap** (PhysicianBench, 2026-05-05): 27-call average is the highest horizon in the cluster; the open-source vs closed-source gap (19% vs 46%) is largest at this horizon, suggesting tool-use trace data, not raw capability, is the bottleneck

## Related Pages

- [GUI Agents](gui-agents.md)
- [Multi-Agent Systems](multi-agent-systems.md)
