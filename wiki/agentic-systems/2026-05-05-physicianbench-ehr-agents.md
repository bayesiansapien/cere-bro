# PhysicianBench: Evaluating LLM Agents in Real-World EHR Environments

**Source:** HuggingFace Daily Papers, 2026-05-05
**Paper:** [arXiv:2605.02240](https://arxiv.org/abs/2605.02240) · [HF page](https://huggingface.co/papers/2605.02240)
**Raw:** [`raw/huggingface/2026-05-05-physicianbench-evaluating-llm-agents-real-world-ehr-environments.md`](../../raw/huggingface/2026-05-05-physicianbench-evaluating-llm-agents-real-world-ehr-environments.md)
**Tier:** 2 (agents, professional-domain benchmarks)

## TL;DR

100 long-horizon physician tasks pulled from real consultation cases, executed inside an EHR environment with vendor APIs, spanning 21 medical specialties. Each task averages 27 tool calls and requires data retrieval across patient encounters, clinical reasoning, action execution, and documentation. Best-performing model: 46% pass@1. Best open-source: 19%. Each task panel-reviewed by physicians.

## Why it matters

This is the eighth realistic agent benchmark in the wiki's tracker (after OccuBench, GTA-2, DR3-Eval, PRL-Bench, Claw-Eval-Live, InteractWeb-Bench, and AcademiClaw on the same day). All eight report frontier-agent failure rates of 30%+ on multi-step real tasks. PhysicianBench differs from the prior set in two ways. First, it uses *standard vendor EHR APIs*, not a wrapped sandbox — meaning the action space is exactly what a real medical agent would face. Second, the 27-tool-call average is the highest tool-call horizon in any of the eight benchmarks. Long-horizon credit assignment is the open problem.

The 46% ceiling on best-model performance, combined with Marcus's "very little evidence for LLMs benefiting patients" piece (2026-05-03) and Google DeepMind's blind-physician-test win (2026-05-01), gives a sharper picture: LLMs match or beat clinicians on knowledge-recall tasks (DeepMind), but they fail at clinical-workflow tasks (PhysicianBench). The gap is between *medical knowledge* and *EHR-mediated action*.

## Connections

- **Agent benchmarks cluster** — the eight-benchmark cluster (full list on the [agent-benchmarks concept page](agent-benchmarks.md)) now spans general workflows (Claw-Eval-Live), domain-specific science (PRL-Bench), web (InteractWeb-Bench), professional assistant tasks (OccuBench), academic challenges (AcademiClaw), and now medical clinical workflows (PhysicianBench). The cross-benchmark pattern: the model passes its capability evaluation but fails the workflow evaluation.
- **GTA-2 (2026-04-20)** — execution harness dominates model capability. PhysicianBench's 27-tool-call horizon is exactly where harness design dominates: a model with weaker raw capability but better trajectory awareness should outperform a stronger model with a naive harness. The natural follow-up: run Step-Level Optimization (05-02) cascades on PhysicianBench tasks.
- **InteractWeb-Bench (2026-05-01)** — graded clarification behavior. PhysicianBench has no equivalent grading dimension; given the safety stakes in clinical settings, an "ask for confirmation" dimension would be the highest-value extension.
- **Defense Trilemma (2026-05-04)** — the trilemma's persistent-unsafe-region result has direct relevance: clinical workflows have boundary-region inputs (atypical presentations, rare symptom combinations) where any wrapped LLM is provably non-complete. PhysicianBench surfaces those regions empirically.

## Research angle

1. **Step-Level Optimization on PhysicianBench.** Per-step routing in clinical workflows: a small model handles routine retrievals; a frontier model is escalated for diagnostic reasoning steps. Falsifiable: cost-vs-completion measurement on the 100 tasks.
2. **Multi-criteria scoring.** PhysicianBench reports pass@1 success rate. Clinical workflows have multiple correctness dimensions: completeness of documentation, accuracy of orders, appropriate referrals, safety of medications. Themis-style multi-criteria scoring (05-04) on PhysicianBench would expose dimension-specific failure modes.
3. **Trajectory-aware safety monitoring.** Each 27-tool-call task is a trajectory; per-step boundary monitoring in the trilemma's sense is a direct application. The first agent that runs PhysicianBench with Stuck/Milestone monitors and reports both completion rate and boundary-violation rate sets a new standard.

## Open questions

- The 27-tool-call average masks variance. How does the failure mode shift between short workflows (5–10 calls) and long ones (50+)? The benchmark presumably reports per-task data, but the abstract does not.
- Open-source model 19% ceiling is particularly low. Is the gap a capability gap or a tool-use-format gap (vendor-specific JSON schema)? If the latter, training open-source models on EHR tool-use traces should close it fast.
- The 21-specialty span allows specialty-conditional routing experiments: a router that dispatches dermatology tasks to one model and oncology to another could outperform a single best model. This has not been measured.
