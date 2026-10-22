# AI Cut Our Research Time From 7 Days to 15 Minutes (Gareth Yoder, Vanguard)

**Channel:** AI Engineer
**Published:** 2026-10-21
**Source:** https://www.youtube.com/watch?v=uA4ah-dVHvU

## TL;DR
Vanguard's cash ledger team (ACH, wires, internal transfers; ~30M service calls/day, ~500K ledgers/day, active-active multi-region) modernized a mainframe ledger to cloud. The single biggest lever was exposing the legacy codebase and migration docs to AI tools through an MCP server, which collapsed the "ask a mainframe engineer how this works" loop from 7 days to 15 minutes. Everything else in the talk is solid but conventional migration engineering: CDC, idempotency, schema registry, observability.

## Key Takeaways
- **Legacy code as an MCP resource is the win.** Research questions about data schemas and legacy behavior moved from a human bottleneck (scarce mainframe engineers) to a prompt. The 7d to 15min figure measures queue time removed, not analysis speed.
- **Migration docs served via MCP cut producer support load.** 35 producers onboarded by querying docs through their own AI tools instead of opening chats with the core team.
- **AI bridged semantic gaps.** Legacy opaque status codes were mapped to human-readable cloud enums; the AI tools translated intent across the two well.
- **Three parallel pillars:** data migration (CDC plus daily row-count and column-level audits), producer migration (gateway API over a common schema, idempotency, Snowflake-style IDs for multi-writer consistency), consumer migration (GraphQL for real-time, per-consumer warehouse data-share views for batch, Kafka at-least-once with idempotent consumers for streaming).
- **Business justification as metadata.** 50 consumers had to submit a use-case description with their app code. AI then aggregates this into "what business functions depend on us" and "what breaks, how fast, if the SLA is breached." Batch consumers give hours, real-time APIs give minutes.
- **Fix forward, not backward.** Fix decades-old bugs only in the modern stack so the fix becomes an incentive to migrate. Requires audit-log allowlisting.
- **90% daily AI tool use** in the cash program, with multi-agent workflows and a shared "team brain" knowledge base so new hires get the same prompt context as 5-year veterans.

## Architecture & Optimization Mechanics
- The pattern is retrieval over a frozen corpus (legacy code, wiki docs) exposed as a tool, not fine-tuning. It works because legacy code changes slowly, so the context is cheap to cache and reuse.
- The weak spot: no accuracy number was given. A 15-minute AI answer about mainframe semantics that is wrong 10% of the time can cost far more than 7 days in a regulated ledger. The talk does not mention how answers were verified beyond the daily data audits.
- The "team brain" is an accumulating, shared context store. This is the same structure as a semantic cache: expensive reasoning done once, served many times.
- Tying business-impact metadata into observability is effectively a routing signal for incident response: priority is a function of consumer type (batch vs real-time).

## Grounded Context (Web Enrichment)
Vanguard has publicly described a multi-decade legacy rebuild (30 to 40 years of tech, done with Deloitte, with AI layered on a flexible API stack), but nothing public confirms the cash ledger specifics or the MCP setup beyond this talk. The broader industry is converging on the same move: IBM's COBOL Upgrade Advisor now exposes MCP tools to its Bob agent, and community "COBOL Bridge" MCP servers parse programs and extract business rules. The 2026 consensus in modernization write-ups is that code conversion is only ~10% of the work and verification against production data dominates; Apex Systems specifically flags packed-decimal arithmetic as a regulator-visible failure mode. Vanguard's daily column-level audits are the right instinct, but the talk's headline metric says nothing about the correctness of AI-sourced answers, which is the claim that matters most.

Sources: [Vanguard tech stack article](https://corporate.vanguard.com/content/corporatesite/us/en/corp/articles/rebuilding-our-tech-stack-for-the-next-era-of-innovation.html), [Apex Systems whitepaper](https://www.apexsystems.com/sites/default/files/documents/_ai-for-mainframe-modernization-whitepaper.pdf), [IBM CUAZ agent mode](https://www.ibm.com/docs/en/SSVA0IS/cuaz-agent-mode.html), [COBOL Bridge MCP](https://glama.ai/mcp/servers/iist6q50iw)

## Real-World Application / Actionable Step
- Expose your own "legacy" knowledge (old eval harnesses, past pruning/quantization experiment logs, kernel notes) via an MCP server so agents can answer "what did we try and why did it fail" in minutes. This wiki is already halfway there.
- When you measure the win, measure answer accuracy against a held-out set of questions with known answers, not just latency. Report both.
- Borrow the "business justification per consumer" idea for routing work: tag every caller of a routed endpoint with its latency tolerance (batch vs interactive). That metadata is free routing signal for cheaper model selection on tolerant traffic.
