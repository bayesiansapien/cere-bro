# Paving the Road to Production: Governed Enterprise AI Agents (Harish Gaggar, Credit Karma)

**Channel:** AI Engineer
**Published:** 2026-10-14
**Source:** https://www.youtube.com/watch?v=tZycGA_Fbfo

## TL;DR
Agents fail in production because the foundation controls are missing, not because the model is weak. Credit Karma's answer is a "paved road": a dev portal that, from one agent registration, scaffolds a repo with five baked-in frameworks (LangGraph agent, memory, tracking/eval, PII blocking, context optimizer) and provisions the production resources (workload identity, memory DB, eval tables, secrets). All tool calls go through a central MCP gateway to internally reviewed MCP servers, with OTel/Tempo/Prometheus/Grafana monitoring and human-in-the-loop for writes. Solid reference architecture for a regulated fintech. Two weak spots: the headline "90% token savings" from the context optimizer is shown with zero quality measurement, and the gateway "unwraps the JWT and attaches the user token" to downstream calls, which sounds close to the token passthrough pattern the MCP spec forbids.

## Key Takeaways
- **Platform over agent.** Do not let teams ship agents with ad-hoc infra. One registration produces an agent ID and a repo pre-wired with all frameworks, so behavior and telemetry are consistent and centrally visible.
- **Lifecycle:** register, dev portal, scaffolded repo, local Docker build with SQLite/BigQuery traces, PR with two approvals, CI/CD registers the agent in a central registry, image scan, security approval, deploy to a K8s namespace with pre-bound workload identity (K8s SA to GCP SA).
- **Own your MCP servers** (FastMCP) in air-gapped or regulated settings. Every tool is security-reviewed; filters, limits and field blocking prevent data the LLM should not see from ever being returned.
- **MCP gateway flow:** client authenticates once, gateway stores session in Redis and returns a JWT; tool calls go to `/<namespace>/mcp` (e.g. GitHub, Artifactory) with the bearer; the gateway resolves the namespace, attaches the user's identity and forwards; responses are scoped to what that user may see. No direct endpoint access.
- **Gateway monitoring:** logs to ELK/Loki/CloudWatch (e.g. 401 spikes, OAuth refresh failures), traces to Tempo via OpenTelemetry (slow tool, agent vs IDE origin), metrics to Prometheus (P95 per tool, auth rejection spikes), visualized in Grafana.
- **LangGraph agent pattern:** interpret, classify (read vs modify vs delete/sensitive), plan subgraph (fetch evidence via gateway, validate), policy check. Reads execute; writes and sensitive ops wait for HITL approval. Everything, approved or rejected, goes to an audit log.
- **Memory:** thread per conversation, run ID per question, checkpoint per graph node. SQLite locally, Cloud Spanner in prod.
- **Tracking/eval from day one:** per agent, six tables (job tracking, quality checks with eight dimensions per run such as success, latency, cost, tool accuracy, safety; a 0 to 1 scoreboard; nested quality metrics; tool invocations; step-by-step trajectory). Aggregate across 100s of agents for executive ROI dashboards.
- **PII/secrets blocking:** typed detectors with severity; above ~90% severity, redact at ingestion so secrets never reach the LLM, memory DB, eval tables or traces.
- **Context optimizer:** select payload by token budget, re-rank by relevance, dedupe, compress. Demo: Artifactory query 24,000 tokens to 2,400; Slack bot 24,000 to ~1,500. Typical savings 70 to 78%.

## Architecture & Optimization Mechanics
- **Governance as scaffolding.** Pushing memory, eval, PII and context compression into the template is the key move: it converts per-team discipline into a platform default, and it is the only way the cross-agent ROI dashboard can exist (shared schema).
- **Read/write classification before planning** is a cheap, effective risk router: it decides the approval path, not the model. Same idea as cost-based routing, applied to blast radius.
- **Context optimizer = retrieval over tool output.** Budgeted selection, re-rank, dedupe, compress. Large wins come from verbose tool payloads (artifact listings, JSON dumps), which are highly redundant. These numbers are workload-specific and say nothing about answer quality.
- **Where the tokens actually go.** A 24k-token response to "list my artifacts" means raw API payloads are being dumped into context. Field projection at the MCP server (return only needed fields) would capture much of that saving deterministically, before any learned compression.

## Grounded Context (Web Enrichment)
The architecture lines up with where the MCP ecosystem landed in 2026: the spec makes MCP servers OAuth 2.1 resource servers, requires audience-bound tokens (RFC 8707), and explicitly forbids forwarding a client's token to downstream APIs; the 2026-07-28 revision adds mandatory `Mcp-Method`/`Mcp-Name` headers precisely so gateways can route without parsing bodies, and Enterprise-Managed Authorization (central IdP control of MCP access) reportedly went stable in June 2026. The correct pattern for "attach the user token" is RFC 8693 token exchange, minting a downstream-scoped token per server, not passing the user's token through. This is not academic: LiteLLM's CVE-2026-59822 (CVSS 8.8, on CISA's KEV list since 2 Sept 2026) let any fabricated bearer token get an authenticated MCP session through a passthrough fallback. If Credit Karma's gateway does exchange rather than forward, the talk undersold it; if not, it is the weakest link. See [[2026-10-12-AI-Engineer-Lethal-Trifecta-Token-Exchange-Keycard]] and [[2026-10-12-WorkOS-Auth-md-Agent-Registration]].

On the context optimizer, independent evidence says the quality cost depends on how you prune. On SWE-bench, structure-aware SWE-Pruner cut ~31% of tokens while improving success from 62% to 64%, whereas token-level LLMLingua-2 dropped success to 54%. A 90% cut without an eval gate is a claim, not a result, which is ironic given the talk's own emphasis on tracking and eval. Related: [[2026-10-06-AI-Engineer-The-Self-Improving-OSS-Agent-Stack-Langfuse]], [[2026-08-28-Productionizing-LLM-Gateways-Kanish-Manuja-Twilio]].

## Real-World Application / Actionable Step
- **Steal the template idea for research infra.** Any internal agent or eval harness should ship with tracing, per-run quality and cost tables, and PII scrubbing by default, not as optional add-ons.
- **Gate context compression with an eval.** Before claiming token savings, run the compressed and uncompressed pipelines on the same queries (use the ceiling-test design from [[2026-10-14-AI-Engineer-How-To-Actually-Tokenmaxx-OutRival]]) and require a non-negative lower bound on quality.
- **Fix tokens at the source first.** Add field projection and pagination to MCP tool outputs before adding a learned compressor. Deterministic, free, and auditable.
- **Route by risk as well as cost.** Add a read/write/sensitive classifier to agent routers: cheap model plus no approval for reads, stronger model plus HITL for writes.
- **Audit your MCP gateway auth:** confirm audience-bound tokens and token exchange, no passthrough fallback, and validate `iss` per the latest spec.
