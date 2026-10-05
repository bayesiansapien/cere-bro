# An Interaction Is All You Need (Ivan Leo, Google DeepMind)

**Channel:** AI Engineer
**Published:** 2026-10-03
**Source:** https://www.youtube.com/watch?v=8aVbXXvJUY4

## TL;DR
A developer-relations pitch for two Gemini API primitives. The Interactions API replaces the old generateContent-style endpoints with one stateful call (`client.interactions.create`) that returns an `interaction_id`; pass it back as `previous_interaction_id` and the server holds the conversation, including the opaque thought signatures Gemini 3.x needs to keep reasoning quality. Managed Agents expose the Antigravity harness (the same agent behind AI Studio and the Antigravity IDE) as a remote agent with a persistent sandbox addressed by an `environment_id`. The real message is strategic: Google is moving state, harness and sandbox server-side, and new models will ship only on this API. Signal is moderate. Useful API shape, no benchmarks, and the "you only pay for the model" line is a preview-period perk.

## Key Takeaways
- **Two IDs carry all state.** `interaction_id` preserves context and cache; `environment_id` routes back to the same sandbox with installed packages and files intact.
- **Thought signatures are the forcing function.** Dropping or mangling them degrades Gemini 3.x performance, and startups were busting prefix cache with a single stray whitespace. Server-side state removes that failure mode.
- **Steps data model.** The legacy outputs array is replaced by a typed, discriminated list of steps (thoughts, function calls, signatures, content with `type` = text/audio/image/video). Multimodal chaining (Nano Banana image into Omni Flash video) reuses one interaction lineage.
- **Mixed built-in and custom tools in one call:** Google Search, URL context and a user function, with the model looping autonomously.
- **Managed Agents:** one API call boots a remote sandbox; sources can be GCS buckets, GitHub repos or inline files; local skills folders upload unchanged so local and cloud agents share harness and prompt. Demo burned 2M+ tokens analyzing a full repo.
- **Credential safety via MITM proxy.** Outbound requests have headers rewritten to inject secrets (e.g. GitHub token), so a prompt-injected agent never sees the raw token.
- **Named agents:** freeze a configured environment as a reusable agent; speaker claims up to 1,000 per project with no storage or sandbox charges.
- **Migration bait:** an "Interactions API skill" for coding agents so they stop defaulting to Gemini 2.x model IDs.

## Architecture & Optimization Mechanics
The cache point is the one that matters for inference economics. Prefix caching only pays off when the token prefix is byte-identical across turns, and client-managed history with encrypted reasoning blobs is fragile. Holding history server-side makes the provider's KV prefix cache hit deterministic, which is the same lever cache-aware routers use on the serving side. The cost is control: you cannot easily prune, compress or rewrite history for context engineering when the server owns it, and branching becomes "fork from an ID" rather than "edit the transcript."

The Antigravity harness is co-trained with Gemini, which is the clearest public statement yet that harness and weights are being optimized jointly. For routing research this means a Gemini call through Managed Agents is not comparable to the same model behind a generic harness; the harness is part of the model's effective capability. The MITM credential proxy is a sound pattern worth copying in any agent stack regardless of vendor.

## Grounded Context (Web Enrichment)
Official docs confirm the mechanics: `store` defaults to true, `previous_interaction_id` makes the server manage thought blocks and signatures, and Google markets implicit prefix caching, background execution without the 60 second timeout, resumable streams and branching as benefits. Managed Agents return both `interaction.id` and `interaction.environment_id`, environments can be forked into a saved agent via `client.agents.create(base_environment=...)`, and network credentials can be refreshed on an existing environment. Since the talk was recorded, Managed Agents default to Gemini 3.6 Flash (the talk still cites 3.5 Flash) and gained hooks, background tasks and remote MCP.

Two claims need qualifiers. "You don't pay for the sandbox" holds only for the Public Preview: remote environment CPU, memory and execution are unbilled during preview, while all agent-loop tokens, including intermediate reasoning, are billed at normal rates. A 2M-token repo analysis is therefore not cheap. The 1,000 named agents figure does not appear in public docs. Omni Flash video output runs about $17.50 per 1M video tokens (roughly $0.10/s) with no free tier, so the image-to-video demo has real cost. Lock-in is the unstated trade: default `store=true` means Google retains conversation state, which has data-governance implications for enterprise use.

Sources: [Interactions API overview](https://ai.google.dev/gemini-api/docs/interactions-overview), [Gemini 3 developer guide](https://ai.google.dev/gemini-api/docs/gemini-3), [Gemini thinking docs](https://ai.google.dev/gemini-api/docs/thinking), [Phil Schmid: Interactions API quick start](https://www.philschmid.de/interactions-api-quickstart), [Environments in managed agents](https://ai.google.dev/gemini-api/docs/agent-environment), [Building managed agents](https://ai.google.dev/gemini-api/docs/custom-agents), [Antigravity agent docs](https://ai.google.dev/gemini-api/docs/antigravity-agent), [Phil Schmid: Managed Agents guide](https://www.philschmid.de/gemini-managed-agents-developer-guide), [Google blog: Managed Agents 3.6 Flash, hooks](https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api-3-6-flash-hooks/), [Google blog: background tasks, remote MCP](https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api/), [The Rundown: Managed Agents pricing](https://www.therundown.ai/tools/gemini-managed-agents), [eesel: Omni Flash pricing](https://www.eesel.ai/blog/gemini-omni-flash-pricing)

## Real-World Application / Actionable Step
- If any routing or eval harness calls Gemini 3.x with function calling, verify thought signatures are round-tripped verbatim; otherwise you are benchmarking a degraded model and under-crediting Gemini in routing decisions.
- For routing experiments, treat "Gemini via Managed Agents" and "Gemini via raw API" as separate arms. Harness co-training means capability is not a property of weights alone.
- Measure cache-hit rate and cost per task with `previous_interaction_id` versus client-held history; if server state gives materially better cache hits, that is a cost term your router should model.
- Steal the MITM header-injection pattern for any agent with secrets in its sandbox.
- Use the free preview sandbox for throwaway repo-analysis jobs now, but budget tokens; do not build on the "sandbox is free" assumption past GA.
