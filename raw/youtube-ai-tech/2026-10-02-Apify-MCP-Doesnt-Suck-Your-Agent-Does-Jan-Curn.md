# MCP Doesn't Suck. Your Agent Does. (Jan Čurn, Apify)

**Channel:** AI Engineer
**Published:** 2026-10-02
**Source:** https://www.youtube.com/watch?v=pAnLpiAG6Es

## TL;DR
The 2025-26 backlash against MCP ("MCP is dead, long live CLIs") blames the protocol for a harness bug. Naive clients dump every tool schema into context up front and pipe every result back through it. The spec says nothing about how a harness should do this. Čurn's fix is a split: MCP for remote access (auth, transport, sessions, standard semantics), CLI for the local agent interface (progressive discovery and code mode for free, because agents already know the shell). Apify's `mcpc` is the bridge: a thin, LLM-free CLI that exposes the whole MCP protocol through a single `bash` tool call.

## Key Takeaways
- **Real problem is eager tool registration.** 10 servers x 10 tools = 100 schemas in context before the first question. Up to a third of the window gone, plus result bloat, context rot, and cost.
- **Three known fixes, ranked:** (1) sub-agents, which isolate context but still pay the tokens and still leak sensitive values; (2) progressive tool discovery (Anthropic Tool Search Tool, Cursor), which loads schemas on demand; (3) code mode (Cloudflare), which treats tools as code the model writes and composes.
- **Why code beats tool calling:** tool-call syntax is a synthetic construct trained in post-hoc. Shell and code are native to pretraining, and labs can synthesize unlimited shell trajectories. Models grep, pipe and navigate code far better than they pick from JSON schemas.
- **CLIs get discovery and code mode by default.** Agents call `--help` only when needed and often know common tools by heart. But CLIs are local black boxes: no standard auth, no transport protocol, no credential injection, no enterprise observability. Nobody ships "CLI connectors" for remote services.
- **mcpc features:** stdio and HTTP, OAuth 2.1 with OS-keychain credential storage, persistent sessions shared across Claude Code and Codex, `grep` across all connected servers' tools (progressive discovery), `--json` on every command for `jq` piping, async MCP tasks with detach/reattach, server `instructions` (a spec primitive most clients still ignore), sandbox proxy, and x402 wallet support.
- **Most clients lag the spec.** Tasks, instructions, resources and prompts exist in MCP but most hosts do not implement them. The protocol evolved faster than the clients.
- **"Connector evals" (early):** flips the usual benchmark. Fix the agent (Claude Code + Sonnet 5), vary the connector. mcpc and native CLI land at similar cost and time. Raw MCP sometimes finishes faster but burns more tokens, and loses on the other tasks.

## Architecture & Optimization Mechanics
- **This is a context-budget routing problem.** Eager registration is the equivalent of loading every expert of an MoE into every token's compute path. Tool search is top-k expert gating over the tool library: pay only for the 1 or 2 tools the query activates.
- **Code mode moves intermediate data out of the KV cache.** When tool A's output feeds tool B inside a script, the large or sensitive payload never enters the prompt. Only the final filtered result does. That cuts prefill tokens, lowers KV memory per session, and closes a prompt-injection and credential-leak channel.
- **Crossover point matters.** Under roughly 10 tools, discovery overhead (an extra search turn, extra latency) outweighs schema savings. Above a few dozen, it dominates. Pick the strategy per tool-count, not by ideology.
- **Persistent sessions amortize handshakes.** Stateful sessions kept alive across agents remove repeated init/OAuth round trips, a small but real latency win for agent loops that make many calls.

## Grounded Context (Web Enrichment)
Čurn's history checks out. Cloudflare published Code Mode in September 2025 and later collapsed its entire API into two tools (`search()` and `execute()`) in about 1,000 tokens, a 99.9% input cut for that API. Anthropic's Tool Search Tool (November 2025) claimed an 85% token reduction. Independent tests show savings scale with tool count: at around 500 tools, input tokens per query fell from 1.15M to 83K. Anthropic's own docs say plain tool calling is better under about 10 tools, which supports the "harness choice, not protocol choice" framing.

His benchmark is the weak part. It is vendor-run, early, and he shows three charts with no task descriptions or variance. Third-party benchmarks paint a harsher picture of raw MCP: Scalekit and others report CLI at 10x to 35x fewer tokens and 100% vs 72% reliability on harder tasks, with almost the entire gap coming from injected schemas (44K tokens vs 1.4K for a trivial repo question). The same reports find gateway-side schema filtering recovers about 90% of the gap. So the data agrees with Čurn's diagnosis (schema bloat is a client problem) while showing that, as shipped today in most hosts, MCP really does cost more. `mcpc` is real, MIT-licensed on GitHub and npm (`@apify/mcpc`). Note the commercial angle: Apify sells a large MCP server, so it benefits directly if MCP survives. See also Čurn's earlier take on agent payments in [x402 Isn't Good Yet](2026-09-01-x402-Isnt-Good-Yet-Jan-Curn-Apify.md) and Cloudflare's sandbox side of code mode in [Dynamic Workers](2026-06-08-Cloudflare-Dynamic-Workers-Eval-Plus-Plus.md).

Sources: [apify/mcpc on GitHub](https://github.com/apify/mcpc), [Cloudflare: Code Mode](https://blog.cloudflare.com/code-mode-mcp/), [InfoQ: Cloudflare Code Mode MCP server](https://www.infoq.com/news/2026/04/cloudflare-code-mode-mcp-server/), [MCP.Directory: Context bloat fix 2026](https://mcp.directory/blog/mcp-context-bloat-fix-2026-tool-search-code-mode-progressive-disclosure), [Maxim: 92% savings at 500+ tools](https://www.getmaxim.ai/articles/cutting-mcp-token-costs-by-92-at-500-tools/), [Scalekit: MCP vs CLI benchmark](https://www.scalekit.com/blog/mcp-vs-cli-use), [MindStudio: 35x token gap](https://www.mindstudio.ai/blog/mcp-servers-35x-more-tokens-cli-tools-reliability-benchmark)

## Real-World Application / Actionable Step
- **Audit your agent's idle context.** In Claude Code, run `/context` with your normal MCP set loaded. If schemas take more than about 10% before the first prompt, turn on tool search or drop servers you rarely call.
- **Wrap your research tooling as a CLI with `--json`.** For quantization sweeps, eval runners and vLLM launchers, a `--help`-documented CLI with JSON output beats an MCP server for local agents. The agent composes `run_eval | jq` in one bash call and the raw logs never touch context.
- **Use MCP only where auth and remote state matter.** W&B, HF Hub, cluster schedulers: keep MCP, but consume it via `mcpc` so the agent sees a shell, not 40 schemas.
- **Steal the connector-eval idea for your router.** Hold the model fixed and vary the tool interface on your own tasks. Measure tokens per success, not tokens per call. The same cost-per-task logic applies to [harness-level model routing](2026-10-02-Kimchi-Cast-AI-Stop-Rationing-Tokens-Harness-Picks-The-Model.md).
