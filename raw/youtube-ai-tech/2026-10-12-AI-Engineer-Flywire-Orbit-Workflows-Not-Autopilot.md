# Agents in Orbit: Workflows, Not Autopilot (Eduardo Simon & Javier Casal, Flywire)

**Channel:** AI Engineer
**Published:** 2026-10-12
**Source:** https://www.youtube.com/watch?v=rAUyRDOFyHU

## TL;DR
Flywire (PCI DSS and SOC 2 payments company, ~400 engineers, six language stacks) built Orbit, an in-house platform where every agent is a YAML-defined workflow: deterministic activities do the predictable work, and short, permission-scoped LLM steps (Claude Agent SDK inside) are called only where reasoning is needed, each with a strict JSON output schema. Six months in it runs ~11,000 executions a month at a reported 99% success rate, with the merge request as the human-in-the-loop unit of work. Nothing architecturally novel, but it is a clean, numbers-backed reference design for "crystallize procedure into code, rent intelligence per step," and it lands squarely on routing: each step declares its own model, and a cost-aware router is on their roadmap.

## Key Takeaways
- **Workflow shape:** trigger (GitLab webhook, Jira, Sentry, AWS, schedule, CLI/API, soon MCP) → deterministic fetch/classify/clone → read-only LLM step with strict schema → deterministic post-back. The model never owns control flow.
- **Build vs buy:** frontier coding models made a custom platform cheap to build, and keeping execution inside their existing PaaS (Victoria, on GitLab + AWS) avoided vendor security reviews for PCI/PII/PHI data.
- **Per-step least privilege, declared in YAML:** network reach, tools, skills, and MCP servers down to individual tools. Code review can read and search but not edit or push. Access is reviewed in merge requests like any code.
- **Skills first, workflows second:** a central skills repo is published as an internal Claude Code plugin marketplace. The same skill runs on a laptop and inside Orbit. Promote to a workflow only once a task proves worth automating.
- **Guardrails:** per-agent timeouts, aggressive default rate limits (a broken integration could spawn thousands of agents), and control-plane locks that drop duplicate executions.
- **Runtime evolution:** started on ECS Fargate with orchestrator and runtime in one container, then split orchestration, agent runtime, and session state. Added AWS Lambda MicroVMs per tech stack after their June launch. Full sandboxing (Docker-in-Docker, test execution) is still not done, which is why the ticket-to-MR implementer cannot reliably run builds or tests.
- **Evals:** vibe check to ship, then OpenTelemetry traces of every activity, model call, and tool call. Real traces become golden datasets versioned next to code. Evaluation is per LLM step by injecting exact historical state into a node, not end-to-end. No online evals yet.
- **30-day numbers:** 9,700+ code reviews (<3 min per MR), 159 dependency-vulnerability MRs, ~80 repos improved by the AI-readiness fixer, 413 projects fixed by the platform-linter fixer, 921 merge-conflict resolutions, 11,000+ total executions at 99% success.
- **Cost lesson:** cost control starts with model selection. Planning and implementation steps already use different models. Cost-aware router and model-agnostic, harness-agnostic orchestration are roadmap items.

## Architecture & Optimization Mechanics
- **Schema-constrained steps make routing tractable.** Because every LLM step has a fixed input context and a typed output, each step is an independently swappable, independently evaluable unit. That is the precondition for a per-step router: you can measure quality per node against golden traces and downgrade the model wherever the schema-validated output does not regress.
- **Isolated node evaluation is the right eval granularity.** End-to-end agent evals are noisy and expensive. Replaying recorded state into a single node is effectively a unit test for a model choice, and it is cheap enough to run across a candidate model ladder.
- **Validation failure as a routing signal.** Orbit retries or falls back on schema failure. A cascade router can use the same signal: try the small model first, escalate only on schema failure or low confidence.
- **"99% success" needs a caveat.** It almost certainly means execution completed without error, not that the review or fix was correct. Without online evals, quality is measured only by MR approval, which is a human-filtered metric.

## Grounded Context (Web Enrichment)
The Lambda MicroVMs timeline holds up. AWS launched Lambda MicroVMs on June 22, 2026: Firecracker-based isolated VMs for user-supplied and AI-generated code, with sessions up to eight hours (versus Lambda's 15 minutes) and suspend/resume that preserves state and stops compute billing while idle. Launch coverage notes limits that matter for Flywire's sandboxing goal: Graviton (Arm) only, a handful of regions, and network egress still needing explicit control. OpenAI's cookbook already uses MicroVMs as a sandbox for its Agents API, so this is becoming a common agent runtime rather than a Flywire quirk.

Flywire's Orbit itself has no public footprint beyond this talk, so the operational numbers are self-reported. The pattern matches what other enterprise talks in this wiki converge on (Perpetual's "deterministic control flow, intelligence for judgment" and Southbridge's split of designer vs worker models): the industry consensus for regulated environments in late 2026 is narrow LLM steps inside deterministic orchestration, not open-ended autopilot.

Sources: [DevClass: AWS debuts Lambda MicroVMs](https://www.devclass.com/devops/2026/06/24/aws-debuts-lambda-microvms-with-up-to-8-hours-runtime/5260139), [AWS What's New: Lambda MicroVMs](https://aws.amazon.com/pt/about-aws/whats-new/2026/06/aws-lambda-microvms/), [Noqta: Lambda MicroVMs for AI agents](https://noqta.tn/en/news/aws-lambda-microvms-firecracker-sandbox-ai-agents-2026), [OpenAI cookbook: AWS sandboxes](https://developers.openai.com/cookbook/examples/agents_api/sandboxes/aws/readme)

## Real-World Application / Actionable Step
- **Use Orbit-style workflows as a routing testbed.** Per-step typed I/O plus recorded traces is exactly the dataset a learned router needs: (step type, input features, model, schema-pass, downstream acceptance). If you are building a router, pitch it against this shape of workload, where the per-step model choice is explicit and the cost of a wrong downgrade is visible.
- **Build a per-node model ladder eval.** For any agent pipeline you own, replay golden node inputs across a small/medium/frontier ladder (and quantized variants served on vLLM) and record the cheapest model that passes schema and quality checks per node. That gives a static routing table today and labeled data for a dynamic router later.
- **Treat schema-validation failure as a free escalation trigger** in cascade routing experiments. It costs nothing to compute and correlates with the small model being out of its depth.
- **Low priority for compression work directly**, but read-only, short-context, structured steps like code-review classification are good candidates for distilled or quantized small models running on infrastructure you control.
