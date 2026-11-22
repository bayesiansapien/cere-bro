# Engineer Your Coding Agents Like Any Other System (Zach Lloyd, Warp)

**Channel:** AI Engineer
**Published:** 2026-11-20
**Source:** https://www.youtube.com/watch?v=0LeT996Hz3E

## TL;DR
Warp's CEO (ex-Google Docs eng lead) defines a software factory narrowly: a **code-defined, closed-loop system for continuously measuring and improving cloud coding agents**. Local, interactively prompted agents hit three limits: human throughput, cost and productivity opacity, and security and governance. The fix is a six-layer stack: factories-as-code (Terraform-style), central data capture of every agent run, sandboxed compute, a multi-model and multi-harness inference layer, orchestration, and API/MCP-first integration. On top sit the new "factory engineering" tools: online evals, self-improvement loops that open PRs against the factory definition, and replay benchmarks on your own data.

## Key Takeaways
- **What a factory is not:** a loose bag of automations, "AI teammates", a shared skills/MCP repo, or personal agent swarms. Those are primitives, not the system.
- **Factories as code** enable branching, A/B testing factory configs, rollback, and agents proposing changes to their own workflow.
- **Record everything:** conversations, artifacts, screenshots, videos. This trace data is the raw material for improving the factory.
- **Models and harnesses are degrees of freedom to test,** not religious choices. Claude Code, Codex, Pi, Warp, or a custom harness with org context.
- **Metrics:** DORA (cycle time) plus automation metrics: human interactions per PR, throughput, cost.
- **Online evals:** an agent scores completed sessions on a specific failure mode. His example is redundant test generation.
- **Self-improvement:** an agent clusters failed runs, finds patterns, and opens a PR against the factory definition.
- **Replay benchmarks:** build a benchmark set from your real tasks, replay against model, harness, or skill variants, and plot cost vs quality. Aim for the upper-left quadrant. Also ablate skills, since removing some may improve results.
- **New core skill:** evals, benchmarks, and A/B tests replace debuggers and profilers as the tools that separate great engineers from average ones.

## Architecture & Optimization Mechanics
- The stack is a **control system**: plant (agents) → sensors (trace capture + online evals) → controller (self-improvement agent) → actuator (PR to declarative config). Stability depends on eval quality. A bad eval produces a self-improvement loop that optimizes toward the wrong target (Goodhart).
- Treating the **inference layer as a test variable** is what makes model routing measurable. The replay benchmark is a per-org Pareto frontier of cost vs quality, which is exactly the input a router needs.
- Central capture is also **distillation fuel**. Logged agent trajectories on proprietary tasks are the dataset for fine-tuning smaller in-house models to replace frontier calls on routine factory stages (triage, spec, test writing).

## Grounded Context (Web Enrichment)
Warp launched Warp Factories on 2026-08-18 in closed beta, with up to $10K in usage credits for qualifying orgs. It is aimed at smaller companies that cannot build a factory from scratch ([Fortune press release](https://fortune.com/press-releases/warp-launches-warp-factories-automate-software-development-2026-08-18/), [TechCrunch](https://techcrunch.com/2026/08/18/warps-new-system-is-an-out-of-the-box-software-factory-for-ai-development/), [It's FOSS](https://itsfoss.com/news/warp-factories-launched/)). Warp says it automates about 30 to 35% of its own weekly tasks through factories. That is self-reported, not independently verified ([eWEEK](https://www.eweek.com/news/warp-ai-software-factory/), [Warp blog](https://warp.dev/blog/open-infrastructure-for-building-a-software-factory)). Lloyd predicts factories will become as common as CI/CD. Experts quoted by The New Stack agree on direction but doubt the timeline ([The New Stack](https://thenewstack.io/warp-software-factory-infrastructure/)).

Take it with a grain of salt: this is a vendor talk. The "drastically improved throughput and lower cost" claim comes with no numbers in the talk. The architecture is sound, and it matches Hanson's point in the Coxon/Hanson debate (2026-11-19 entry) that org-level bottlenecks, not individual coding speed, cap AI productivity. The factory pattern is the industry's attempt to engineer those bottlenecks away.

## Real-World Application / Actionable Step
- **Apply the replay-benchmark pattern to your routing research.** Log real agent tasks from your team. Replay them across frontier, mid-tier, and your quantized or distilled models. Plot the cost/quality frontier per pipeline stage. That gives you an empirical, org-specific routing table.
- **Define one online eval for a known failure mode** in your agent workflows (e.g. "agent edited kernels without running the perf benchmark"). Score historical sessions with it before you change anything.
- **Put your agent config in version control** (models, skills, MCPs, triggers). This lets you A/B test a quantized model in one factory stage with a clean rollback.
