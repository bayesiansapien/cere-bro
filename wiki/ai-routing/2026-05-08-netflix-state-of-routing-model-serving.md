# State of Routing in Model Serving (Netflix Tech Blog)

**Source:** [Netflix Tech Blog (Medium)](https://medium.com/@netflixtechblog) — surfaced via Gmail Medium Daily Digest 2026-05-08
**Authors:** Nipun Kumar, Rajat Shah, Peter Chng (Netflix)
**Length:** 13 min read (per digest metadata)
**Tier:** 1 — ai-routing (user's #1 interest)

## Status: title-level signal only

The Gmail Medium Daily Digest captured the title, authorship, and engagement metrics (355 claps, 6 responses) but not the body. The article was not part of today's RSS or HuggingFace pull, so cere-bro does not have its content. The wiki page exists to ensure this entry is registered as a known-but-unread Tier 1 source, not lost.

## Why it matters even at title-level

- "State of Routing in Model Serving" is Tier 1 in two ways: ai-routing (the user's #1 attention area) AND model-serving infrastructure (adjacent to inference-efficiency).
- Netflix's Tech Blog is a high-signal source for production-scale model-serving practice. Their prior work has shaped industry patterns on streaming-aware caching, A/B routing, and shadow-traffic evaluation.
- The "state of" framing implies a survey or taxonomy piece, which is exactly the kind of source that becomes a reference page in cere-bro's [llm-routing concept page](llm-routing.md). High value as a fix-point for the field's vocabulary.

## What to read for

When the user reads this directly, the questions to answer for the wiki:
1. **What routing axes does Netflix taxonomize?** (latency vs capability vs cost vs reliability)
2. **Heuristic vs learned routers** — which does Netflix use in production?
3. **Numbers** — throughput, p99 latency, cost-per-token claims at production scale.
4. **Failure modes** — what happens when a route is wrong or a downstream model is overloaded?
5. **Comparison to TRACER** ([wiki](2026-04-17-tracer-llm-routing.md)) and [Ken Huang's routing chapter](2026-05-01-ken-huang-ch14-routing-provider-abstraction.md) — does Netflix's framing align or diverge?

## Action

Worth a manual read on next available reading window. After reading, this stub gets replaced with a proper summary page following the standard cere-bro template.
