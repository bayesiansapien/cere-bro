# Dashboards Are Dead (Sarah Simionescu, Composio)

**Channel:** AI Engineer
**Published:** 2026-10-04
**Source:** https://www.youtube.com/watch?v=YiFqcu9YA38

## TL;DR
A Composio engineer argues that dashboards and per-tool query languages (Datadog syntax, JQL, Slack modifiers, SQL dialects) were only ever translation layers between humans and data, and that agents now make them obsolete. Raw MCP is not enough, because agents do not learn across sessions, drown in thousands of tool definitions, and cannot compose across isolated servers. Composio's pitch is an agent-native layer on top: a search tool that returns the right tools plus an execution plan per sub-task, and a remote sandbox that processes large intermediate results without loading them into context. The framing is right, but this is a product talk: the headline "better than native MCPs" result is unreleased, unquantified on stage, and the core techniques are now standard practice that Anthropic itself ships.

## Key Takeaways
- **Thesis:** "You never wanted a dashboard, you wanted the answer." Agents are a new user class that has no eyes and judges a product only on task completion.
- **Three MCP failure modes:** (1) no cross-session learning, (2) context bloat from tool definitions (Composio's GitHub toolkit alone has 200+ tools), (3) app isolation, so cross-app tasks fall on the user.
- **Fix 1, task-scoped tool retrieval:** the agent states its sub-tasks, and search returns relevant tools plus a dependency plan (e.g. resolve Slack channel ID before fetching messages).
- **Fix 2, keep data out of context:** intermediate results (PostHog user IDs) are saved, then a sandboxed "Remote Workbench" generates SQL against Metabase to join on them without the model ever reading the full list.
- **Demo claims:** Slack bug report to Sentry plus Datadog root cause to draft PR in under five minutes, with no custom skill or workflow.
- **Product lesson:** few companies have made their apps agent-usable; customers are now asking vendors for agent access, not dashboards.

## Architecture & Optimization Mechanics
Both fixes are context-budget optimizations, and they map directly onto routing. Tool search is retrieval-augmented tool selection: instead of a model attending over N tool schemas (cost and error both scale with N), a retriever narrows to k candidates, which is a routing decision made before the expensive model sees anything. The returned "plan" is a cached, precomputed dependency graph, effectively distilling past successful trajectories into a static hint so the model does not rediscover call ordering. The workbench pattern is code execution as a data plane: the LLM is the control plane emitting small programs, while bulky tensors of data (ID lists, query results) stay in the sandbox. This is the same principle as keeping KV cache or activations off the critical path; the model's context is the scarce resource, so move bulk data movement out of it. The unspoken weakness: retrieval quality now bounds agent quality, and a mis-retrieved tool is a silent failure.

## Grounded Context (Web Enrichment)
The diagnosis is well supported. Anthropic reported that tool-selection accuracy degrades significantly past roughly 30 to 50 tools, that a five-server MCP setup can burn about 55K tokens before the first user message, and that its own Tool Search (deferred tool loading) lifted MCP eval accuracy from 49% to 74% on Opus 4 and 79.5% to 88.1% on Opus 4.5 while cutting definition overhead by about 85%. RAG-MCP measured selection accuracy falling from 43% to under 14% as catalogs grew. Anthropic's "code execution with MCP" post showed a Drive-to-Salesforce workflow dropping from 150K to 2K tokens (98.7%), which is the same idea as Composio's Remote Workbench; independent measurements land closer to 75 to 80% savings, so treat 98.7% as best case.

So Composio's techniques are not unique; they are now built into Claude Code and the Agent SDK. Composio's real moat is breadth and managed auth (Tool Router as one MCP endpoint over 500+ integrations with token refresh handled), not the retrieval trick. "Dashboards are dead" is also overstated: dashboards remain the shared, auditable artifact for on-call and exec review, and the speaker's own anecdote (frozen in front of Datadog with a coworker watching) shows the human-legibility problem that pure agent access creates.

Sources: [Composio Tool Router overview](https://composio.dev/content/best-mcp-servers), [Composio Review 2026 (AI Agent Index)](https://theaiagentindex.com/agents/composio), [Anthropic brings MCP tool search to Claude Code (Tessl)](https://tessl.io/blog/anthropic-brings-mcp-tool-search-to-claude-code), [MCP Tool Search guide (Cyrus)](https://www.atcyrus.com/stories/mcp-tool-search-claude-code-context-pollution-guide), [Claude Agent SDK tool search docs](https://code.claude.com/docs/en/agent-sdk/tool-search), [More Tools Made AI Worse (DEV)](https://dev.to/rawveg/more-tools-made-ai-worse-po7), [Hybrid Semantic Tool Discovery (arXiv 2608.23992)](https://arxiv.org/pdf/2608.23992), [Code execution with MCP, 98.7% (Brightbean)](https://brightbean.xyz/blog/code-execution-mcp-efficient-ai-agents/), [Code execution with MCP caveats (Particula)](https://particula.tech/blog/code-execution-mcp-token-reduction-pattern)

## Real-World Application / Actionable Step
- Treat tool selection as a routing problem in your own research: a cheap retriever or small classifier choosing k of N tools before the large model runs. Measure accuracy versus k and token cost; this is a publishable-shape routing experiment with clean metrics.
- In your own agent setups, enable deferred tool loading (Tool Search) and push data-heavy steps into code execution so large results never enter context.
- Log successful tool-call trajectories and distill them into reusable plans or a small policy model; that is the "agents don't learn" fix Composio implies but does not explain.
- If you ship any internal tooling, expose an agent-friendly interface (narrow, well-documented tools with explicit dependencies) before building another dashboard.
