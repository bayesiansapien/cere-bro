# MCP Integration: Claude Code vs Hermes (Ken Huang Ch 13)

**Source:** Ken Huang / Agentic AI Substack (2026-04-30)
**Link:** [Post](https://kenhuangus.substack.com/p/chapter-13-mcp-integration-connecting)
**Tier:** 2 — agent harness architecture
**Raw:** [../../raw/rss/2026-04-30-agentic-ai-chapter-13-mcp-integration-connecting-agents-to-the-wor.md](../../raw/rss/2026-04-30-agentic-ai-chapter-13-mcp-integration-connecting-agents-to-the-wor.md)

## TL;DR

Both Claude Code and Hermes implement MCP clients, but they make very different choices about lifecycle, server-initiated requests, and credential safety. Claude Code uses a **TypeScript-native, async-first, session-bound** integration where MCP clients are constructor-injected into the QueryEngine and tools are namespaced `mcp__server__tool`. Hermes uses a **Python-with-dedicated-asyncio-thread** approach because Python's threading + asyncio don't mix cleanly; it adds **automatic reconnection with exponential backoff, sampling support (server-initiated LLM calls), and an aggressive credential-stripping regex** on every error path.

## Five differences worth keeping

| Dimension | Claude Code | Hermes |
|---|---|---|
| Runtime | TypeScript async-first | Python sync agent loop + dedicated asyncio thread |
| Connection lifecycle | Session-bound; reconnect via session restart | Long-lived `MCPServerTask` with exponential backoff (5 retries, 1s→60s) |
| Tool naming | `mcp__server__tool` (double underscore) | `mcp_server_tool` (single underscore) |
| Sampling (server → LLM) | Not in scope | `SamplingHandler` callable; rate-limited (sliding-window RPM); model override per-server |
| Credential safety | Implicit via TS type system + permission gates | Explicit `_sanitize_error()` regex strip on every error path before LLM sees it |

## Why this is Tier 2

This is the most concrete cross-harness comparison published so far. Chapters 8 (memory, 04-25) and 12 (skills, 04-30) focused on how each system stores state. Chapter 13 is about how each system *connects to the outside world*. Together they map the full design surface of an agent harness.

The asymmetry of choices reveals each system's threat model:

- **Claude Code's session-bound design** is correct if the session is short-lived and restarting on disconnect is acceptable. This matches a coding-assistant deployment.
- **Hermes's long-lived MCPServerTask + reconnection** is correct if the agent is running long-horizon work where mid-session disconnects must be silently recovered. This matches an unattended-workflow deployment.
- **Hermes's sampling support + credential stripping** is correct if you expect untrusted MCP servers in the catalog. Claude Code does not have either, because its trust model presumes user-curated MCP servers.

## Connection to prior wiki

- **Claude Code memory systems (Ch 8, 04-25)** + **Skill system pattern (Ch 12, 04-30)** + **MCP integration (Ch 13, 05-01)** — Ken Huang's three chapters now constitute the most thorough public side-by-side of two production agent harnesses. The pattern: Claude Code is *minimal-by-design with safety delegated to humans*; Hermes is *first-class subsystems with safety delegated to scanners and sanitizers*. Each new chapter has reinforced this axis.
- **Eywa (05-01)** uses MCP-style language-mediated tool interfaces, but extends them across modalities. MCP + Eywa is the path to a heterogeneous multi-foundation-model agent stack.
- **Persistent Agent Infrastructure (04-23) / ClawGym (04-30)** — both faced the question of long-running connections to mutable external state. Hermes's MCPServerTask with reconnection is a concrete answer to that question for the MCP class of connections.

## Research angle

The most interesting open question raised by Ch 13: **how do agent-managed credentials flow across MCP servers in a multi-agent system?** Hermes's per-server credential stripping is per-call defensive; it does not prevent a *previous* tool call from leaking secrets into the conversation that a subsequent server then sees. A defense-in-depth proposal — typed credential capabilities scoped to specific (agent, server, time) tuples — would be the natural next chapter.

For Tier 1 routing: **MCP server selection is an explicit routing problem.** When 10 MCP servers expose overlapping capabilities, which does the agent call? Today the answer is "whichever the agent picked first." A principled router over MCP servers (latency-aware, cost-aware, capability-coverage-aware) is the obvious gap.
