# Sakana Fugu Ultra v1.1 — Model Router Claims to Beat Fable 5

**TL;DR.** Sakana AI updated its Fugu Ultra model router to v1.1, claiming up to 7.9-point gains over v1.0 and, more provocatively, that the router now beats Anthropic's Fable 5 on their evaluation *without Fable 5 in the routing pool*. The update adds a Claude Code-compatible endpoint. There is no independent verification yet, and the service is still unavailable in the EU.

## What it is

Fugu Ultra is a commercial LLM router: given a query, it picks (or blends across) a pool of underlying models to maximize quality per cost. v1.1 is an incremental quality bump. The headline claim is that routing across a set of non-frontier models can match or exceed a single frontier model (Fable 5) it does not even call, i.e. the ensemble-of-cheaper-models beats the expensive monolith on Sakana's benchmark.

## Why it matters (relation to prior wiki)

This lands squarely on the wiki's routing thread and Sakana's own prior work. [Conductor (05-11)](2026-05-11-conductor-sakana-orchestrating-frontier-models.md) was Sakana's RL orchestrator that treated routing as a learned policy over frontier models; Fugu Ultra is the productized descendant. The "beat the frontier model without including it" claim is the strongest public version of the [routing-as-substitute thesis](llm-routing.md): that a good router over commodity models can substitute for a single expensive one. It should be read against the [07-20 "When is routing meaningful"](2026-07-20-when-is-routing-meaningful.md) skepticism, which argued routing only pays off when the model pool is genuinely diverse in cost and capability. Sakana's claim is exactly the kind of assertion that thesis says to check, and the absence of independent verification is the caveat.

The Claude-Code-compatible endpoint is the more concrete signal: it means Fugu is positioning as a drop-in backend for agentic coding, competing with the flash-model price war (Ling 3.0 Flash, Grok 4.5) on economics rather than raw capability.

**Caveats.** Vendor benchmark, self-reported, no independent verification, EU-unavailable. The "7.9 points" and "beats Fable 5" figures are Sakana's own; treat as a claim to track, not a result.

- Source: [The Decoder](https://the-decoder.com/sakana-claims-its-ai-model-router-fugu-ultra-v1-1-now-beats-fable-5-without-even-including-it-in-the-pool/)
- Raw: `raw/rss/2026-07-24-the-decoder-sakana-claims-its-ai-model-router-fugu-ultra-v1-1-now-b.md`
- Related: [Conductor (Sakana)](2026-05-11-conductor-sakana-orchestrating-frontier-models.md) · [When is routing meaningful](2026-07-20-when-is-routing-meaningful.md) · [llm-routing](llm-routing.md)
