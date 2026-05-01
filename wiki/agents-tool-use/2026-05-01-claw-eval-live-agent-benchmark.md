# Claw-Eval-Live: Live Agent Benchmark for Evolving Real-World Workflows

**arXiv:** 2604.28139 · [paper](https://arxiv.org/abs/2604.28139) · [HF](https://huggingface.co/papers/2604.28139)
**Tier:** 2 — agent benchmarks, evaluation infrastructure
**Raw:** [../../raw/huggingface/2026-05-01-claw-eval-live-live-agent-benchmark-evolving-real-world-workflows.md](../../raw/huggingface/2026-05-01-claw-eval-live-live-agent-benchmark-evolving-real-world-workflows.md)

## TL;DR

Most agent benchmarks freeze a curated task set at release and grade only the final response. Claw-Eval-Live separates a **refreshable signal layer** (updated each release from public ClawHub Top-500 skill demand) from a **reproducible release snapshot** (frozen fixtures, services, workspaces, and graders). Each release: 105 tasks, 13 frontier models, deterministic + structured-LLM grading on execution traces, audit logs, service state, and post-run artifacts. Result: **leading model passes only 66.7%, no model reaches 70%.** HR, management, and multi-system business workflows are the persistent bottlenecks; local workspace repair is comparatively easier but unsaturated.

## Why this is the right benchmark format

Three mechanisms together:

1. **Refresh from public workflow-demand signals.** ClawHub Top-500 is the input — the benchmark tracks what users are actually asking agents to do, not what benchmark authors imagine.
2. **Reproducibility within a release.** The release snapshot freezes everything (services, fixtures, graders) so models can be compared apples-to-apples, even though the task population evolves across releases.
3. **Verifiable agent action.** Graders read execution traces, audit logs, service state, and post-run artifacts — not just the final response. This catches the "claimed success but didn't actually do it" failure mode that final-response grading misses.

The slogan is exactly right: **workflow-agent evaluation should be grounded twice — in fresh external demand and in verifiable agent action.**

## Key empirical findings

- **No model reaches 70%.** Frontier agents fail roughly one in three real workflow tasks. This is far below where reliable automation needs to be.
- **Failures are structured by task family and execution surface.** HR / management / multi-system business workflows are the persistent bottlenecks. Local workspace repair is easier.
- **Pass rate alone is insufficient.** Models with similar pass rates diverge in *overall completion* — task-level discrimination concentrates in a middle band. The implication: leaderboard rank doesn't tell you which agent to deploy.

## Connection to prior wiki

- **OccuBench (04-16) / GTA-2 (04-20) / DR3-Eval (04-18) / PRL-Bench (04-20)** all converged on the same pattern: frontier agents fail multi-step real-world tasks reliably. Claw-Eval-Live is the **fifth benchmark in three weeks** to find this. *The measurement is now a regularity, not a coincidence.* The agent benchmarks page should add this as a confirmed cross-benchmark pattern.
- **ClawGym (04-30)** is the *training* counterpart: ClawGym builds the synthesis + sandbox-parallel-RL pipeline to train workflow agents. Claw-Eval-Live is the *evaluation* counterpart on the same skill ontology (ClawHub Top-500). Together: a complete public stack for personal-workflow agents (synthesis, training, eval).
- **Workflow-grading via execution traces** is the same idea as Persistent Agent Infrastructure (04-23) — both treat the agent's *trajectory* as the unit of evaluation, not the final response. This is now the second major paper to say so, and it's becoming the agent eval default.

## Why it matters

The 66.7% ceiling is the headline number for "agents are not deployable for general workflow automation yet." For Amit's interest in *agent trajectory routing* (Tier 1), this matters: trajectory routers must be evaluated on trajectories, not on terminal correctness. Claw-Eval-Live is the first benchmark whose grading explicitly looks at the trajectory.

## Research angle

The middle-band discrimination finding is the most actionable: if models with similar pass rates diverge in overall completion, then **a router that picks the right model per task family** could outperform any single model. This is the cleanest argument yet for trajectory-aware multi-model routing. Claw-Eval-Live's task-family-level discrimination is the calibration data such a router would need.
