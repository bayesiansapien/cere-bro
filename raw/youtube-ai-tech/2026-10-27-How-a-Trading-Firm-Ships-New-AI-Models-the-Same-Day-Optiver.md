# How a Trading Firm Ships New AI Models the Same Day (Noyan Tokgozoglu, Optiver)

**Channel:** AI Engineer
**Published:** 2026-10-27
**Source:** https://www.youtube.com/watch?v=aGIUg8zKI8A

## TL;DR
Optiver's head of AI engineering describes an on-prem, model-agnostic AI platform built for an environment where P&L impact shows up within hours. Their rule: any new frontier model released publicly should be benchmarked on internal golden sets and usable in production flows the same day. The enabling pieces are an inference gateway (routing, failover, per-team budgets), full trace logging piped automatically into evals, a "meta harness" that makes team configs portable across agent harnesses, and an agent gateway acting as a single ledger for multi-agent orchestration. The most transferable content is the cost story: spend spiked with summer frontier releases, and was pulled back by context hygiene (200k-token default sessions cut down via MCP tool search, CLI wrappers, cache tuning, knowledge bases), team-owned budget alerts, open-weight substitution, and early model routing. Light on numbers, strong on operational pattern.

## Key Takeaways
- **Same-day model adoption is an eval problem, not an integration problem.** Optiver partners with trading teams to collect their benchmarks into golden sets, runs every new model against them on release, and publishes a recommendation internally. External benchmarks are treated as insufficient because internal data distribution differs.
- **Inference gateway as the control plane.** All traffic (third-party APIs under zero-data-retention agreements, self-hosted open models, a fully isolated DMZ on-prem zone) goes through one gateway providing routing, provider failover, per-model spend tracking, and budgets. Downtime equals lost revenue, so provider redundancy is a first-class requirement.
- **Vendor lock-in kills speed.** They dropped a third-party inference gateway vendor because new-model support went through "GTM team and roadmap" queues. Owning the gateway is what makes same-day adoption possible.
- **Context bloat was the biggest waste.** Fresh sessions defaulted to roughly 200k tokens of context because self-service users stacked MCPs, knowledge bases, and giant system prompts. Fixes: MCP tool search (deferred tool loading), agent-facing CLIs wrapping groups of MCPs, auditing cache invalidation and TTL settings (possibly dynamic), and moving system-prompt content into retrievable knowledge bases.
- **These savings scale with token price.** Context hygiene is multiplicative on cost, so it becomes more valuable as teams move to pricier frontier models.
- **Visibility beats mandates.** Giving teams spend dashboards plus self-set alerts and limits produced sensible self-imposed caps.
- **Routing is still exploratory.** Approaches under test: send prompts dynamically to cheaper models, and a planner/executor split where a frontier model plans and smaller models implement subtasks. Open-weight models are already substituted where token cost per quality is competitive.
- **Eval replay is unsolved for stateful tools.** Every tool call is logged (OpenTelemetry) and fed to evals, but re-running an agent on a new model breaks when tools depend on world state at original run time. Backtest databases are point-in-time and trivially replayable. Slack and similar systems are not. Optiver attaches a "point-in-time confidence" score to each logged tool invocation and replays through an MCP proxy that serves snapshots where possible.
- **Scope agents narrowly.** Merging two teams' agents into one union agent caused tech debt and regressions where some skills improved while others degraded. Current answer: versioned, task-scoped agents that call each other through the agent gateway, keeping each one independently measurable.
- **Knowledge bases are underrated and unsolved.** Hybrid vector plus hierarchical markdown today. He is unhappy with it and wants to explore graph databases.

## Architecture & Optimization Mechanics
The architecture is a textbook example of the gateway-centric routing stack Amit's research targets, operated under real P&L pressure. Three layers matter:

1. **Gateway layer (routing substrate).** A single choke point that sees every request, logs it, and attaches cost. This is exactly the data asset a learned router needs: production prompts paired with model, cost, and (via eval pipelines) quality labels. Optiver has the plumbing but admits routing is still exploratory. The gap between "we log everything" and "we route on it" is where a cost-quality router earns its keep.
2. **Eval layer (router training signal).** Golden sets per trading team give per-domain quality estimates for each new model on release day. That is effectively a routing table refreshed on every model launch. The planner/executor decomposition is a form of cascade routing at the subtask level, where frontier compute is spent only on high-entropy planning tokens.
3. **Context layer (input-side compression).** Cutting a 200k default context is a larger, cheaper win than any model swap. Prompt tokens dominate agentic cost, and prefix stability decides cache hit rate. Tool search and CLI wrapping are input pruning. Moving static instructions into retrieval is lazy loading. Cache TTL tuning is the KV-reuse problem at the API billing level.

The opinionated read: the talk confirms that in enterprise agent deployments, **input-token reduction and cache-prefix discipline currently beat model routing on ROI**, and routing is the next frontier once logging and evals are in place. The world-state replay problem is also a direct threat to offline router evaluation. Counterfactual "what if model B handled this" replays are only valid for tool calls with high point-in-time confidence, so router training data needs that same confidence filter.

## Grounded Context (Web Enrichment)
Optiver's direction is corroborated by its own hiring. A current posting for a Head of AI Engineering in Shanghai describes a mix of hosted and open-weight models and evaluation tooling that informs routing decisions, matching the talk's platform. No independent writeup of the specific numbers (200k default contexts, spend curves) exists, and the talk deliberately shows no figures, so treat the cost-control claims as directional. The "Claude Code moment" in December and the summer spend spike line up with the broader 2026 pattern of agentic coding driving enterprise token spend.

The MCP-versus-CLI claim holds up, with a caveat. Vendor benchmarks (Scalekit via Apideck, Firecrawl) report MCP using 4x to 35x more tokens than CLI equivalents in naive setups, but these come from CLI-leaning vendors. Checkly argues the gap has narrowed since harnesses now defer MCP tool loading, which is the "tool search" fix Optiver adopted. Anthropic's Tool Search still injects the full schema when a tool is fetched (roughly 121 tokens per tool), so deferred loading reduces cost without eliminating it. StackOne's point is the key one for Amit: caching makes stable-prefix tokens cheaper to bill but they still occupy the context the model reasons over, so cache tuning and context pruning are complementary rather than substitutes.

## Real-World Application / Actionable Step
- **Instrument before you route.** If your routing experiments lack production-like traces, copy Optiver's pattern: one gateway, every call logged with model, tokens in/out, cache hits, and cost, auto-forwarded to an eval store. A router is only as good as this labeled dataset.
- **Build a release-day eval harness.** Maintain per-domain golden sets and a one-command script that scores any new model (frontier or a compressed variant of your own) on cost and quality. Output a Pareto table. This doubles as the evaluation protocol for pruned and quantized models versus frontier APIs.
- **Measure context before model swaps.** Profile the median input token count of your agent sessions and the cache-hit rate. If defaults sit above roughly 50k tokens, prune tools (deferred loading, CLI wrappers) and move static prompt content into retrieval before you spend effort on routing. Expected ROI is higher and it compounds with any later routing gains.
- **Test planner/executor cascades.** Run a frontier planner plus small or quantized executors on your agent benchmarks and compare against single-model baselines on cost per solved task. This is a clean, publishable routing experiment.
- **Filter router training data by replay fidelity.** When building counterfactual datasets for "would the cheaper model have succeeded," tag each trajectory's tool calls with point-in-time replayability and exclude or down-weight low-confidence ones to avoid biased router labels.

Sources:
- [Optiver: Head of AI Engineering, Shanghai](https://optiver.com/join-us/jobs/technology/shanghai/head-of-ai-engineering-shanghai/)
- [Apideck: Your MCP Server Is Eating Your Context Window](https://www.apideck.com/blog/mcp-server-eating-context-window-cli-alternative)
- [Checkly: CLIs are more token-efficient than MCP. Or are they?](https://www.checklyhq.com/blog/mcp-vs-cli-token-efficiency/)
- [Firecrawl: MCP vs CLI](https://firecrawl.dev/blog/mcp-vs-cli)
- [StackOne: MCP tool bloat and the stateless spec](https://www.stackone.com/blog/mcp-tool-bloat-stateless-spec/)
- [MCP Schema Bloat and System Prompt Tax](https://codex.danielvaughan.com/2026/04/23/mcp-schema-bloat-system-prompt-tax-tool-definition-performance/)
