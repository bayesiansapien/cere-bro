# Harness Engineering: How to Build a Software Factory (Dru Knox, Tessl)

**Channel:** AI Engineer
**Published:** 2026-10-06
**Source:** https://www.youtube.com/watch?v=X6l4lpA0_NY

## TL;DR
Dru Knox (head of product, Tessl) defines a software factory as a system where agents produce all shipped code and engineers only build the factory. Progress is measured on three ordered axes: autonomy (how rarely humans correct the agent), automation (how much you skip review), and quality. The practice that gets you there is harness engineering, organized as three loops (inner, outer, meta) and three build layers (control plane, agent-readiness, improvement loops). The framework is clean and useful as a checklist, but the talk is a vendor pitch with zero numbers: no before/after takeover rates, no quality data, and the headline claim that factories eventually raise quality is asserted, not shown.

## Key Takeaways
- **Autonomy and automation are distinct.** An agent can one-shot tasks (high autonomy) while you still review every line (low automation). Build autonomy first; automation is earned trust.
- **Three loops, three cost tiers:**
  - Inner loop: pre-PR, cheap, run constantly by the agent (lint, unit tests). Drives autonomy.
  - Outer loop: on PR open, expensive, run once (agentic QA, mutation testing of the test suite). Replaces human review time.
  - Meta loop: outside dev entirely. Mines agent logs, PR comments, issue tracker, user feedback for escaped mistakes and patches the inner and outer loops. Drives quality.
- **Control plane first:** route all work through legible surfaces. Tessl's own flow: issue tracker ticket, headless agent in a sandbox, PR, humans comment on the PR. Local IDE sessions are invisible to optimization loops.
- **"Agent-readiness" is the unplannable grab bag:** CLI/API access, internal service auth, production log access (compliance), a runnable execution env, a written-down "company brain." Knox: "it's worse than you think."
- **Improvement loops are where time goes:** nightly/weekly repo sweeps (architecture, duplication, test quality, security), playbooks as skills, mining PRs for repeated chores (e.g., weekly flaky-test hunts) and turning them into scheduled skills.
- **Why teams fail at it:** knowledge churn (best practices go stale in weeks, some become anti-patterns), harness work is unplanned and competes with feature deadlines, and signal is trapped on laptops and in heads.
- **Factory KPIs:** manual takeovers down, human PR comments down, share of PRs initiated without human input up, quality held flat then raised.
- **Tessl product:** governed skills registry (security/quality scans, publish controls), Linear-to-GitHub connector, code-review tooling, Tessl Agent (mines PRs/issues for automatable work), one-click maintenance tasks, and `tessl launch` to run any skill as a sandboxed workflow on Codex, Claude Code, Gemini, or Tessl Agent.

## Architecture & Optimization Mechanics
The loop taxonomy is a cost-tiered verification cascade, the same shape as LLM routing: cheap checks on every iteration, expensive checks only at a gate, and a slow offline process that tunes both. The non-obvious design rule is placement by marginal cost per caught error. Mutation testing in the inner loop burns tokens and wall-clock on every edit; a cheap linter in the outer loop catches errors too late. Each check should live in the tier where its cost divided by errors-prevented is lowest.

The meta loop is effectively an online learning system over the harness, not the model. Its training signal is human corrections (PR comments, takeovers), and its parameters are skills, playbooks, and CI checks. That framing exposes the risk Knox skips: if the KPI is "fewer human PR comments," the loop can be gamed by reviewers trusting more, not by agents improving. Takeover rate and comment count are proxies; escaped-defect rate measured downstream is the real objective. The control-plane point is the strongest one in the talk: you cannot optimize what is not logged, and local agent sessions are dark data.

## Grounded Context (Web Enrichment)
The terminology is real and fast-moving, as Knox says. "Harness engineering" entered circulation in February 2026 (Mitchell Hashimoto, then LangChain's Deep Agents work), framed as Agent = Model + Harness. The evidence that harness matters is solid: LangChain moved its coding agent from rank 30 to top 5 on Terminal Bench 2.0 with no model change, and Anthropic's 2026 agentic coding report puts harness-only swings at 5+ points. A September 2026 arXiv source-code study of eleven coding-agent harnesses formalizes the discipline. The "loop engineering" rebrand Knox mentions is documented too, including an August 2026 arXiv paper. Note his inner/outer/meta loop naming differs from Andrew Ng's widely cited inner/middle/outer framing, where the outer loop is user feedback. Knox's "outer loop" is Ng's gated CI stage, so expect naming collisions across talks.

On Tessl, the claims check out: a governed registry advertising 3,000+ skills, Snyk security scores on every public skill since March 2026, and Task Evals that compare agent behavior with and without a skill. That last feature is the most credible piece and Knox barely mentions it. The weak claim is "quality goes up." Productivity evidence remains mixed: METR's 2025 RCT found experienced developers 19% slower with AI tools while believing they were 20% faster, and METR's early-2026 update only says speedups are likely larger now. Prior wiki pages from Factory and WorkOS on the same topic make the same point: most "software factories" today are still human-gated pipelines.

Sources: [Harness Engineering source-code study (arXiv 2609.00006)](https://arxiv.org/pdf/2609.00006), [Tessl: The Rise of the Harness Engineer](https://tessl.io/blog/the-rise-of-the-harness-engineer), [Faros: Harness engineering in 2026](https://www.faros.ai/blog/harness-engineering), [Loop Engineering (arXiv 2608.21884)](https://arxiv.org/pdf/2608.21884), [Tessl: Loop Engineering pattern](https://tessl.io/patterns/agentic-development-workflow/loop-engineering/), [Augment: What is loop engineering](https://www.augmentcode.com/guides/what-is-loop-engineering), [Ry Walker: Tessl research](https://rywalker.com/research/tessl), [Tessl Skill Evaluation Framework](https://codex.danielvaughan.com/2026/04/08/tessl-skill-evaluation-framework/), [METR update on developer slowdown](https://birchtree.me/blog/an-update-from-the-study-that-said-devs-were-actually-slower-with-coding-agents/), [LeadDev on METR study](https://leaddev.com/velocity/ai-doesnt-make-devs-as-productive-as-they-think-study-finds)

## Real-World Application / Actionable Step
- **Move experiment work onto a legible control plane:** kick off agent runs for quantization/pruning sweeps from issues, land results as PRs. Your corrections then become mineable data instead of terminal scrollback.
- **Tier your checks for research code:** inner loop = unit tests on kernel shapes and dtype paths, a tiny perplexity smoke test on a 100-sample slice. Outer loop = full eval harness (lm-eval, latency/throughput on vLLM) run once per PR. Do not let the agent iterate against the full eval.
- **Track two numbers for a month:** manual takeovers per PR and escaped regressions (accuracy or latency drops found after merge). If takeovers fall but escapes rise, the loop is gaming reviewers.
- **Mine your last 30 PRs for one repeated chore** (e.g., re-running calibration after a config change, regenerating GPTQ checkpoints, benchmark table updates). Turn it into a skill plus a scheduled GitHub Action. One per week.
- **Use with/without-skill evals** before trusting any shared skill: run the same 10 tasks with and without it and compare. Skip skills that do not move the metric.
