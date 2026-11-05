# Without Caching, Your AI Agent Costs 10x More (George Cameron, Artificial Analysis)

**Channel:** AI Engineer
**Published:** 2026-11-03
**Source:** https://www.youtube.com/watch?v=prGP0huECPo

## TL;DR
In late 2026, agent cost is dominated by input tokens, cache hit rate and turns per task, not output or reasoning tokens. Artificial Analysis shows Opus 5.5 costing about $21 per knowledge-work task with caching and over $200 without it. Frontier and cheap-but-capable models now differ by two orders of magnitude in cost per task, so model and reasoning-effort selection against a task-specific Pareto curve is the main cost lever.

## Key Takeaways
- **Cost spread is ~100x.** Opus and Fable exceed $5 per task on the Intelligence Index; GPT-6 Luna runs about $0.07 per task and still beats original GPT-4.
- **Intelligence deflation is ~10x per year.** Once an intelligence tier (e.g. 30 or 50 on the AA Index) is first reached, the cheapest way to access it falls roughly an order of magnitude within 12 months.
- **Cost anatomy of an agent task (AA Briefcase benchmark, Opus 5.5 max):** answer tokens about $0.16, reasoning tokens a few cents, about $0.13 per LLM call, times 165 steps. Input tokens and cache hits dominate each call.
- **Caching is the single biggest switch.** Cache reads get roughly a 10x discount on input price. A 0% cache hit rate (e.g. a self-hosted vLLM stack without prefix caching enabled) pushes the $21 task past $200.
- **Reasoning effort compounds.** Higher effort adds reasoning tokens, changes the number of turns, and those tokens get re-fed as input through the message history. Opus 5.5 ranges from about $1 per task (low) to $21 (max).
- **Open weights stay 3 to 9 months behind** the proprietary frontier. GLM 5.3 Flash is the cited cheap, strong alternative.
- **Task taxonomy for routing:** "limited intelligence" tasks (lookup, e.g. "what did I spend on subscriptions?") have a quality ceiling, so buy the cheapest model that hits it. "Unlimited intelligence" tasks (open-ended analysis) scale with capability, so the question becomes budget.
- **Recommended process:** shortlist from the generalist Pareto, then build a custom benchmark on your own tasks before production. AA now sells this as "Optima."

## Architecture & Optimization Mechanics
- **Agent cost model:** `cost_per_task = turns × [uncached_input × p_in + cached_input × p_cache + (reasoning + answer) × p_out]`. Because context accumulates across turns, input tokens scale roughly quadratically with trajectory length, so cache hit rate multiplies against the largest term.
- **Prefix stability is an engineering property.** Cache hits depend on byte-identical prefixes. Anything that mutates early context (timestamps in system prompts, reordered tool schemas, history rewriting or summarization mid-trajectory) silently destroys hit rate.
- **Self-hosted inference:** vLLM automatic prefix caching and SGLang RadixAttention give the same economics on your own GPUs, but only if routing is prefix-aware. Load balancers that scatter a session across replicas cut hit rate even when caching is enabled.
- **Reasoning effort as a routing knob:** effort is a second dimension next to model choice. A router choosing (model, effort) pairs can capture most of the 20x Opus low-to-max spread without switching model families.
- **Limited vs unlimited tasks map directly to LLM routing:** a router should first classify whether the query has a capability ceiling, then pick the cheapest model above that ceiling.

## Grounded Context (Web Enrichment)
The talk's framing matches Artificial Analysis's own recent publishing. Its Intelligence Index v4.1 (June 2026) added cost, time and tokens per task for every model, and its Coding Agent Index notes that prompt cache hit rates vary by provider routing and materially change effective cost. Cameron's claim that AA publishes standalone cache-hit benchmarks is only partly visible publicly. Hit rates mostly appear as a per-task token breakdown on agent index pages rather than as a dedicated leaderboard.

Pricing moves since mid-2026 confirm cache price is now a competitive axis. Anthropic cut Claude Fable 5.1 cache-read pricing from $1 to $0.25 per 1M tokens, which AA estimates saves about $1.40 per task, yet Fable 5.1 still costs about 20% more per task than Fable 5 because it uses more tokens. GPT-5.6 Sol landed at about $1.04 per task at max effort with Fable-5-class intelligence at roughly a third of the cost, supporting the "10x per year" deflation curve. Third-party per-task numbers for the same model disagree (one blog says $3.76 for Fable 5.1, another $7.63), so per-task cost is highly harness-dependent. That is the strongest argument for the custom-benchmark advice.

## Real-World Application / Actionable Step
- **Instrument cache hit rate as a first-class metric** in every agent and serving stack you run. Log `cached_tokens / input_tokens` per turn. Below about 80% on long-horizon agents means money is leaking.
- **On self-hosted vLLM:** confirm `--enable-prefix-caching` is on, and use session-affine or prefix-aware routing (e.g. vLLM production-stack router, llm-d) so turns of one trajectory hit the same replica's KV cache.
- **Add effort level to your routing action space.** Treat (model, reasoning_effort) as the routing decision and evaluate cost per resolved task, not cost per token.
- **Add a "capability ceiling" classifier to the router.** Route lookup-style, tool-grounded queries to Luna- or GLM-Flash-class models; reserve frontier models for open-ended tasks.
- **Research angle:** KV-cache compression and quantized KV (FP8/INT4) directly raise the number of cached prefixes a GPU can hold, which raises hit rate. That links your quantization work to agent economics in a way worth benchmarking explicitly.
