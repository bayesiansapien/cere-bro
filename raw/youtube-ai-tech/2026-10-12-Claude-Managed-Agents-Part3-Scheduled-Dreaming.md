# Scheduled Agents, Dreaming and Q&A: Claude Managed Agents (Part 3 of 4), Anthropic

**Channel:** AI Engineer
**Published:** 2026-10-12
**Source:** https://www.youtube.com/watch?v=qJtcEDc_WJU

Series: [Part 1: Brain vs Hands](2026-10-12-Claude-Managed-Agents-Part1-Brain-Hands.md) | [Part 2: Research Agent](2026-10-12-Claude-Managed-Agents-Part2-Research-Agent.md) | **Part 3** | [Part 4: Evals, CI/CD, Multi-Tenancy](2026-10-12-Claude-Managed-Agents-Part4-Evals-CICD-MultiTenancy.md)

## TL;DR
The workshop finale adds two primitives to Claude Managed Agents (CMA). **Deployments** run sessions for an agent on a cron schedule with fixed initial messages and attached resources. **Dreaming** (research preview) spins up a CMA session whose sub-agents read the last N days of transcripts that used a memory store, find recurring failures and gaps, and write an improved memory store. In the demo it found gaps in the hand-written SEC skill and patched them via memory. The Q&A is the more useful half: Anthropic's "let Claude pick the topology" stance, thin harness vs thick skills, workspaces as the only isolation primitive, Claude-only models, no on-prem, and "run evals" as the answer to every confidence question.

## Key Takeaways
- **Deployment = agent + schedule + initial messages + resources** (memory stores, repos, files). Not a snapshot. Each trigger creates a new session; memory persists across them. Triggerable from console or API.
- **Dreaming input:** a memory store, a model, optional custom instructions, a time window (e.g. 30 days). **Output:** an updated memory store. Currently memory-only; skills, prompts and agent definitions are the stated next targets.
- **Observability:** every event is available via API (model call start/end gives latency). No native OTel export; build the connector yourself.
- **Long runs:** compaction is automatic; 10-hour production sessions observed. Scheduled agents can run indefinitely because state lives in memory stores, not one ever-growing session.
- **Topology:** no graph/workflow builder. Anthropic argues that hand-constrained topologies (e.g. "exactly 3 sub-agents") underperform letting Claude decide, and that guardrails get removed as models improve.
- **Thin harness, thick skills?** Skills are the right abstraction today; expect them to thin out as models get smarter. Multi-agent is, in Gabe's view, more durably useful.
- **Dreaming confidence:** Anthropic evals dreaming internally and reports customer eval uplift, but admits it is early and you need your own evals. No built-in eval-gated selection among multiple dream candidates.
- **Enterprise limits:** workspaces are the only tenancy and access primitive (RBAC on roadmap); Claude models only; no on-prem (being "seriously considered"); available on Claude Platform on AWS, not Bedrock console.
- **No scaling knobs.** No HPA-style config; create as many sessions as rate limits allow.
- **Production users:** Notion external agents and Atlassian Jira integrations run on CMA. Sonnet 5 supported.

## Architecture & Optimization Mechanics
- **Dreaming is offline trajectory distillation into context, not weights.** Many transcripts are compressed into a curated memory store that future sessions read. It is the in-context analog of distilling a teacher's rollouts into a student, with the memory store as the "student parameters". Consequence: improvements are cheap, reversible (memory versions) and model-portable, but bounded by context budget.
- **Why Part 1's append-only log matters here.** Dreaming needs full raw transcripts. Destructive compaction would have deleted the training signal.
- **Majority-vote failure mode.** An attendee raised the key risk: if 9 sessions do X wrong and 1 does it right, a naive consolidator learns the wrong lesson. Without outcome-labelled transcripts or eval gating, dreaming is unsupervised consolidation. Anthropic did not have a good answer.
- **Deployments plus memory = stateful cron.** Each run is a fresh, cheap session (runtime billed only while active) that inherits knowledge through memory. This avoids the cost and drift of one immortal session.
- **Opinion:** "Let Claude choose topology" is a reasonable default at Opus-tier, but it couples cost to model judgment. Without budgets (see [Part 2](2026-10-12-Claude-Managed-Agents-Part2-Research-Agent.md)) an over-eager coordinator is an unbounded fan-out.

## Grounded Context (Web Enrichment)
Dreaming was announced at Code with Claude on May 6, 2026, as a research preview requiring access requests; outcomes, multi-agent and memory went to public beta the same day ([SD Times](https://sdtimes.com/ai/new-in-claude-managed-agents-dreaming-outcomes-and-multiagent-orchestration/)). Per Arize's write-up, a dream takes an existing memory store plus 1 to 100 session transcripts, runs asynchronously, and produces a separate reorganized store while leaving the input store untouched ([Arize](https://arize.com/?p=29457)). That non-destructive output is exactly what you need to A/B old vs new memory under evals. Harvey's pilot reportedly saw roughly 6x higher task completion ([Let's Data Science](https://letsdatascience.com/news/anthropic-adds-dreaming-to-claude-managed-agents-3d6be7b5)). That is a vendor-relayed customer anecdote, not an independent benchmark; treat with skepticism.

Scheduled deployments are documented ([Claude docs: Scheduled deployments](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments)), and since August 2026 deployments accept a session budget applied per run, not per schedule, so a 1-hour cadence multiplies the cap 24x per day ([Claude docs: Budgets](https://platform.claude.com/docs/en/managed-agents/budgets), [eCorpIT](https://ecorpit.com/claude-session-budget-list-cost-gaps-deployment-per-run-2026/)). Sonnet 5 launched June 30, 2026 at $2/$10 per MTok and Sonnet 5.5 followed on September 28 at the same price per third-party trackers ([claudelog](https://claudelog.com/faqs/what-is-claude-sonnet-5/), [orcarouter](https://www.orcarouter.ai/he/blog/claude-sonnet-5-5)); confirm against anthropic.com/pricing. On model lock-in, OpenAI's Agents API and AWS AgentCore both now offer comparable hosted runtimes; AgentCore is model-agnostic, CMA is not.

## Real-World Application / Actionable Step
- **Gate dreaming with your eval harness.** Run dream to produce a candidate store; run a fixed eval set with old vs new store; promote only on a statistically significant win. Treat memory stores like model checkpoints.
- **Filter transcripts by outcome before dreaming.** Feed only `satisfied`-on-first-try sessions (positives) and separately the `max_iterations_reached` ones (negatives with labels). This fixes the majority-vote failure mode.
- **Use a cheaper model for the dreaming session.** Consolidation is summarization-heavy; test Haiku or Sonnet vs Opus on resulting eval uplift per dollar. That is a direct routing experiment.
- **Set up a weekly deployment** that scans new arXiv/GitHub releases on quantization, pruning, MoE serving and router papers, writes notes into a memory store, and posts a digest. Budget each run.
- **Do not build graph-based workflows** on CMA expecting them to persist; Anthropic is explicitly steering toward model-chosen topology.
