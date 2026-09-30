# No, That's Not a Software Factory (Ryan Cooke, WorkOS)

**Channel:** AI Engineer
**Published:** 2026-09-27
**Source:** https://www.youtube.com/watch?v=HvboD89DyQ8

## TL;DR
"Sandbox + coding agent + prompt → PR" is not a software factory. WorkOS built exactly that on Cloudflare and found it was indistinguishable from engineers running Claude Code locally. The value came only after encoding the whole product-engineering process (PRDs, ticket dependencies, plan re-evaluation, bug triage) into the automation, and after building an internal MCP gateway ("context engine") that turned out to be the highest-leverage piece. Measure outcomes (features shipped, defect rate, time to recovery), not PR counts.

## Key Takeaways
- Output metrics (% of PRs by AI, PR count) can hide whether anything useful shipped. Track feature delivery, defect rate, MTTR, and voluntary adoption of the cloud factory over local harnesses.
- Two systems: **TARS** (user-facing agent in Slack, Linear, GitHub, driven by webhooks) and **Horizon** (infra orchestration, similar to Ramp's Inspect and Stripe's Minions) behind an MCP gateway.
- Webhook-driven autonomy: when a Linear ticket closes, TARS picks up the next unblocked ticket. Between tickets, it re-evaluates the project for missing tickets, so the plan stays current as work reveals gaps.
- A "PM agent" drafts the "hilltop" PRD (purpose, customer evidence, competitive analysis, milestones) from a few sentences. Humans cut scope, since the agent often overestimates it. It solves the blank-page problem.
- The MCP gateway connects Snowflake semantic tables, Linear, and more, with tool descriptions that explain how WorkOS organizes its data. It is now used across the company for Slack data analysis, well beyond coding.
- The same context layer serves Devin and local Claude Code. The factory does not lock in one agent.
- Next steps: own the sandbox infra for session-level control, an "evergreen" org memory layer, and mining agent sessions to find missing or stale skills (self-improving factory).
- Open problem they admit: authorization for agents.

## Architecture & Optimization Mechanics
- **Context engineering beats agent engineering.** The biggest win was a curated tool and schema layer, not a better agent loop. The model is swappable; the context is the moat.
- **Event-driven scheduling.** Webhooks turn a request-response agent into a workflow engine that walks a dependency DAG of tickets. Same pattern as Antigravity's sidecars.
- **Session telemetry as a training signal.** Owning the infrastructure lets them mine traces for failure modes and create or retire skills. This is a semi-online feedback loop, cheaper than fine-tuning.
- **Multi-agent routing by task.** Devin, Claude Code/Opus, and the in-house OpenCode router share one context layer. The routing decision is per task and made by humans today.

## Grounded Context (Web Enrichment)
The outcome-over-output argument is well supported. 2026 industry data shows AI agents raising PR volume 30 to 98%, but agentic PRs at the 75th percentile wait 5.3x longer for review pickup, and one analysis found main-branch throughput falling 7% even as feature-branch throughput rose 15%. The DORA 2026 AI report frames AI as an "amplifier" whose ROI runs through code review, with stability risks (change failure rate, rework) rising when teams lack observability. A vendor study (Larridin) claims agent adoption produced 10x more deployments but 83% more failures. The number comes from a vendor, so treat it as directional.

What the talk lacks is its own numbers. Cooke lists the metrics WorkOS wants to measure but shows no before/after data on feature lead time or defect rate. The claim that the factory beats local Claude Code is still unproven for WorkOS.

## Real-World Application / Actionable Step
- **Build a research "context engine" MCP server first.** Expose your experiment tracker, benchmark results tables, model registry, and GPU cluster queue with descriptions of how they are organized. Every agent (and colleague) then gets grounded answers like "which quantization configs regressed on MMLU last month."
- **Measure research outcomes, not agent activity.** For your team: experiments reaching a decision per week, and regressions caught before deploy. Ignore lines of code or PRs.
- **Adopt plan re-evaluation.** After each completed sub-experiment in a compression study, have an agent re-read the plan and propose missing ablations.

Sources: [Larridin: AI coding agent DORA metrics](https://larridin.com/blog/ai-coding-agent-dora-metrics), [Kodus: DORA 2026](https://kodus.io/en/dora-accelerate-state-of-devops/), [Ingenire: DORA 2026 AI amplifier](https://ingenire.com/blog/dora-2026-ai-amplifier), [Augment Code](https://www.augmentcode.com/guides/software-delivery-performance-ai)
