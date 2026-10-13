# Build a Research Agent with Claude Managed Agents (Part 2 of 4), Anthropic

**Channel:** AI Engineer
**Published:** 2026-10-12
**Source:** https://www.youtube.com/watch?v=FGftGOzfohc

Series: [Part 1: Brain vs Hands](2026-10-12-Claude-Managed-Agents-Part1-Brain-Hands.md) | **Part 2** | [Part 3: Scheduled Agents and Dreaming](2026-10-12-Claude-Managed-Agents-Part3-Scheduled-Dreaming.md) | [Part 4: Evals, CI/CD, Multi-Tenancy](2026-10-12-Claude-Managed-Agents-Part4-Evals-CICD-MultiTenancy.md)

## TL;DR
Hands-on build of "Research Desk", an SEC-filings analyst on Claude Managed Agents (CMA). It climbs a ladder: chat over an SSE event stream, then a coordinator with specialist sub-agents plus an SEC skill and a shared memory store, then asynchronous runs gated by **outcomes** (rubric-checked self-supervision by a separate grader), then a custom multi-session map-reduce harness driven by a `dispatch_analysis` custom tool. The Q&A surfaces the real boundaries: vault-based credential swapping, MCP tunnels, self-hosted sandboxes, no session forking, and (at recording time) no per-session budget caps.

## Key Takeaways
- **Console quick start**: describe the agent in natural language, Claude drafts name, prompt, model and toolset, then you attach an environment and run a session. Zero code.
- **Chat UI = SSE relay.** Backend posts `user.message` events and re-streams the session's SSE events to the browser. Stop here for a chatbot; CMA's point is long-running async work (hours to weeks).
- **Agent versioning.** Updating an agent creates a new version. Sub-agents are declared with their own prompts, tools and permissions, plus an optional **self-reference** so the coordinator can clone itself. Clones copy prompt and tool schemas, not the transcript.
- **Skills are live artifacts.** Updating the SEC skill (e.g. to parse a new form type) applies to every new session that references it.
- **Outcomes** = task description + rubric + `max_iterations`. When the agent thinks it is done, a grader sub-agent checks artifacts against the rubric; if unsatisfied, it iterates. Outcomes are defined only at the session level, not per sub-agent.
- **Observability**: console shows each sub-agent as a thread on a timeline. The NVIDIA demo spawned a financial extractor and a risk evaluator in parallel, wrote a memory note and a JSON scorecard, then passed grading. About 10 minutes per ticker.
- **Map-reduce across sessions**: the coordinator calls a custom tool, your server spawns one session per ticker (each with its own sub-agents, outcome and shared memory), then aggregates.
- **Vaults**: env vars hold placeholders; real secrets are swapped in at egress only for allowlisted hosts. Works for API keys and OAuth (e.g. Notion MCP).
- **Private data access**: MCP + vault, or MCP tunnels (no public exposure), or self-hosted sandboxes peered with your network (Vercel, Modal, Daytona, GCP, AWS).
- **Agent SDK vs CMA**: Agent SDK is headless Claude Code as a binary you run. CMA is a separate, generalized, fully hosted harness inspired by Claude Code.
- **Gaps admitted**: no loop/token guardrails beyond your own orchestration, no rewind or session forking (on roadmap), no out-of-the-box external memory providers. Multiple memory stores per session enable user-level plus org-level memory.

## Architecture & Optimization Mechanics
- **Two-level parallelism.** Intra-session: sub-agent threads augment context without bloating the coordinator. Inter-session: your custom harness fans out sessions. The second level is where you own scheduling, so it is where routing logic belongs.
- **Outcomes are generator-verifier loops with context isolation.** The grader runs in its own context window so it is not anchored by the worker's reasoning. This is the same principle as using a separate judge model in evals. Cost scales with iterations, so the rubric quality directly sets the token bill.
- **Memory as cache.** The prompt tells the agent to check memory before re-researching a ticker. That is a semantic cache over expensive tool work; hit rate determines cost per run.
- **Self-reference sub-agents** let the model choose its own fan-out topology. Anthropic's stance (repeated in [Part 3](2026-10-12-Claude-Managed-Agents-Part3-Scheduled-Dreaming.md)) is that model-chosen topology beats hand-designed graphs as models improve. Plausible for frontier models, unproven for cheaper ones.
- **Opinion:** Every thread, by default, runs the same model family. The demo never shows per-sub-agent model selection for cost. For a research desk where extraction is mechanical and risk evaluation is reasoning-heavy, that is money left on the table.

## Grounded Context (Web Enrichment)
Outcomes, multi-agent orchestration and memory went to public beta at Code with Claude on May 6, 2026; dreaming stayed research preview ([SD Times](https://sdtimes.com/ai/new-in-claude-managed-agents-dreaming-outcomes-and-multiagent-orchestration/)). Docs confirm the grader runs in a separate context and returns `satisfied`, `needs_revision`, `max_iterations_reached` or `failed` (rubric contradicts task) ([Claude docs: Define outcomes](https://platform.claude.com/docs/en/managed-agents/define-outcomes)). Third-party sources report `max_iterations` defaults to 3, max 20, and a 25-concurrent-thread ceiling per session. Self-hosted sandboxes (public beta) and MCP tunnels (research preview) shipped May 19, 2026 at Code with Claude London, with Cloudflare, Daytona, Modal and Vercel as providers ([Claude blog](https://claude.com/blog/claude-managed-agents-updates), [InfoQ](https://infoq.com/news/2026/05/claude-mcp-tunnels)). Memory stores mount at `/mnt/memory/`, version every write, and default to read_write; use read_only for shared stores because a poisoned writable store contaminates future sessions ([Claude docs: Memory](https://platform.claude.com/docs/en/managed-agents/memory), [aicodex](https://www.aicodex.to/articles/claude-managed-agents-memory)).

The "no budget controls today" answer is now outdated. Session budgets shipped around August 2026: an optional hard list-price ceiling set at creation, emitting `session.usage` events, pausing (not killing) the session with stop reason `budget_reached` ([Claude docs: Budgets](https://platform.claude.com/docs/en/managed-agents/budgets), [Cookbook](https://platform.claude.com/cookbook/managed-agents-cma-cap-session-spend)). Caveats: overshoot of one request per thread (up to 25), and the cap prices at list rates, not your negotiated rate ([eCorpIT](https://ecorpit.com/claude-session-budget-list-cost-gaps-deployment-per-run-2026/)).

## Real-World Application / Actionable Step
- **Put a router at the inter-session dispatch layer.** In your own `dispatch_analysis`-style tool, choose model per session by task difficulty (Haiku for filing extraction, Sonnet/Opus for synthesis). Log the choice plus outcome result to build a router training set with free labels from the grader.
- **Use outcome verdicts as router supervision.** `satisfied` on iteration 1 vs `needs_revision` x3 is a cheap, per-task quality signal. Iterations-to-satisfy is a strong proxy for "this model was too small for this query".
- **Always set a session budget** on fan-out runs and size it for the 25-thread overshoot.
- **Mount shared knowledge read_only**, give each run a separate writable scratch store, and merge through a reviewed process.
- **Try it:** clone the workshop repo, run `/workshop start` in Claude Code, swap SEC filings for arXiv papers on quantization to get a literature-monitoring desk.
