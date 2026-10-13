# Decoupling the Brain from the Hands: Claude Managed Agents (Part 1 of 4), Anthropic

**Channel:** AI Engineer
**Published:** 2026-10-12
**Source:** https://www.youtube.com/watch?v=Uv0nAf_7tyU

Series: **Part 1** | [Part 2: Research Agent](2026-10-12-Claude-Managed-Agents-Part2-Research-Agent.md) | [Part 3: Scheduled Agents and Dreaming](2026-10-12-Claude-Managed-Agents-Part3-Scheduled-Dreaming.md) | [Part 4: Evals, CI/CD, Multi-Tenancy](2026-10-12-Claude-Managed-Agents-Part4-Evals-CICD-MultiTenancy.md)

## TL;DR
Priyanka (eng lead for Claude Managed Agents, CMA) and Gabe Semach explain why Anthropic threw away its first CMA architecture. Version 1 put session log, harness and sandbox in one container, which made each container a "pet": impossible to debug, holding customer data, and unable to reach customer VPCs. Version 2 splits the agent into three replaceable interfaces: an append-only **session log** (the only durable state), a stateless **brain** (harness plus Claude), and on-demand **hands** (sandboxes, MCP servers, customer VPCs). The core lesson: harnesses encode model-specific assumptions that go stale, so design interfaces that outlive them.

## Key Takeaways
- **Agent = model in a loop with tools. Harness = the code that patches what the model cannot do.** Example: Sonnet 4.5 had "context anxiety" (rushing to finish near the context limit), so harnesses added context resets. Opus 4.5 did not need them, so the resets became dead weight.
- **V1 (Dec 2025, early access) failed operationally, not functionally.** A dropped packet and a dead container looked identical; debugging meant websocketing into a container full of customer data; private MCP access required network peering or shipping the harness to the customer.
- **V2 makes everything cattle except the log.** Sandbox dies: the error returns to Claude as a normal failed tool call and Claude decides whether to respawn. Harness dies: a new instance replays the session log and resumes from the last event.
- **Credentials never enter the sandbox.** Outbound calls pass through a proxy that injects tokens at egress, so prompt injection cannot exfiltrate secrets Claude never saw.
- **Append-only log decouples storage from context policy.** Nothing is compacted destructively. Compaction is a read-time view (summarize all, last N events, etc.) and can be swapped without migrating data.
- **TTFT dropped ~90%** because inference starts immediately and the sandbox is provisioned lazily, only when a tool call needs it.
- **API primitives:** `v1/environments` (sandbox template: network allowlist, packages), `v1/agents` (name, model, system prompt, tools such as the base `agent_toolset` with bash/read/write/grep), `sessions` (agent ID + environment ID, idle until an event arrives). Events: `user.message`, custom tool use/result, `session.error`, `status.idle`, `interrupt`.

## Architecture & Optimization Mechanics
- **Event sourcing applied to agents.** The session is a write-ahead log; the harness is a pure function over it. This is the same pattern as stateless inference servers fronted by a durable KV/request log: any replica can pick up a request. Recovery cost is a log replay plus a prefix-cache-friendly re-prefill, not lost work.
- **Lazy sandbox provisioning is a latency optimization, not just a cost one.** Container cold start was on the critical path for first token. Moving it off-path is the agent-level analog of overlapping prefill with weight loading.
- **Read-time compaction** means context strategy becomes a tunable policy you can A/B per model generation. It also preserves the full trace for later offline analysis (which [Part 3's dreaming](2026-10-12-Claude-Managed-Agents-Part3-Scheduled-Dreaming.md) relies on).
- **One brain, many hands.** Sandboxes, MCP servers and customer VPC endpoints sit behind the same tool interface. That uniformity is what later enables self-hosted sandboxes and MCP tunnels without harness changes.
- **Opinion:** None of this is novel distributed systems theory. The value is that Anthropic absorbs the per-model harness churn. That is also the lock-in vector: you are outsourcing the part of the stack that encodes model quirks.

## Grounded Context (Web Enrichment)
CMA launched in public beta on April 8, 2026 behind the `managed-agents-2026-04-01` header, with Notion, Rakuten, Sentry and Asana as early adopters ([InfoWorld](https://infoworld.com/article/4156852/anthropic-rolls-out-claude-managed-agents.html), [noqta](https://noqta.tn/en/news/anthropic-claude-managed-agents-enterprise-ai-platform-2026)). The architecture in this talk mirrors Anthropic's engineering post "Scaling Managed Agents: Decoupling the brain from the hands" ([Anthropic Engineering](https://anthropic.com/engineering/managed-agents)). Secondary write-ups report the TTFT gain more precisely than the talk: roughly 60% lower p50 and over 90% lower p95 ([Towards AI](https://pub.towardsai.net/anthropic-split-the-agents-brain-from-its-hands-and-p95-time-to-first-token-fell-over-90-66efd33b5ad3)). So "90%" is a tail-latency number, not a median one.

Pricing is $0.08 per session-hour of active runtime (metered to the millisecond, idle time free) plus standard token rates, with no Batch API discount equivalent ([TrueFoundry](https://www.truefoundry.com/blog/claude-managed-agents-pricing), [Verdent](https://verdent.ai/guides/claude-managed-agents-pricing)). Competitors converged on the same split: OpenAI's Agents API (public beta, Sept 10, 2026) hosts the Codex harness with OpenAI-managed or bring-your-own sandboxes ([OpenAI](https://openai.com/index/introducing-the-agents-api/)), and AWS Bedrock AgentCore runs each session in a dedicated microVM billed per second of CPU/memory ([AWS docs](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)). The key difference: CMA and AgentCore differ on model choice. CMA is Claude-only.

## Real-World Application / Actionable Step
- **Adopt the log-as-truth pattern in your own eval and routing harnesses.** Store every agent step as append-only events. Then compaction, routing and replay become policies over the log, and you can re-score old trajectories against a new router without rerunning them.
- **Audit your harness for stale model assumptions.** List every workaround (context resets, retry prompts, forced summaries) and tag the model it was written for. Each new model release, ablate them. This is pruning applied to scaffolding, and it usually saves tokens.
- **Measure p95 TTFT, not mean**, for any agent stack you benchmark. Cold sandboxes and tool provisioning dominate the tail.
- **Cost model:** at $0.08/hr, runtime is negligible next to tokens for most workloads. Token spend and model choice per step remain the main lever, which is exactly where routing pays off.
