# RouteProfile: Elucidating the Design Space of LLM Profiles for Routing

**Source:** [HuggingFace Daily Papers](https://huggingface.co/papers/2605.00180) · [arXiv 2605.00180](https://arxiv.org/abs/2605.00180)
**Date ingested:** 2026-05-15
**Tier:** 1. LLM routing, profile design, generalization to new models
**Raw:** [farmer file](../../raw/huggingface/2026-05-15-routeprofile-elucidating-the-design-space-of-llm-profiles-for-rout.md)

## TL;DR

The routing literature has been preoccupied with the router (the dispatch function) and almost ignored the LLM profile (the structured description of what each candidate model is good at). RouteProfile treats LLM profiling as a heterogeneous-data integration problem and lays out a 4-dimensional design space: organizational form (per-domain bucket vs structured tree), representation type (text vs embeddings vs scalar scores), aggregation depth (raw, summary, deep abstract), and learning configuration (frozen vs trainable). Across three representative routers under standard and new-LLM-generalization conditions, three findings hold: structured profiles beat flat ones, query-level signals beat domain-level signals, and generalization to newly added models benefits most from structured profiles with trainable configurations.

## Why this matters for the wiki

The wiki has tracked five papers on the routing-decision axis in the last four weeks: [TraceR](2026-04-17-tracer-llm-routing.md) (query-level features), [CARE](2026-05-11-care-bi-level-routing-moe-continual-learning.md) (MoE bi-level), [Sakana Conductor](2026-05-11-conductor-sakana-orchestrating-frontier-models.md) (frontier orchestration), [Netflix State of Routing](2026-05-08-netflix-state-of-routing-model-serving.md), and yesterday's [MinT](../inference-efficiency/2026-05-14-mint-million-scale-lora-serving.md) (adapter catalog). All five focused on the dispatch function. None of them studied the *profile* the dispatcher uses to decide where to send a query.

RouteProfile is the first paper in the wiki to treat the profile as an independent design surface. The implication is that the same router can be a strong or weak system depending entirely on how its candidate models are described to it. The wiki's existing routing pages should be re-read with this in mind: a router that scores well at evaluation time may collapse under a profile shift even though the dispatch code is unchanged.

The new-LLM-generalization setting is the production-relevant one. Routing fleets add models monthly. If the profile representation is flat or domain-bucketed, every new model needs a fresh trial-period to populate its profile before traffic can be sent. Structured profiles with trainable configurations let the router cold-start a new model from a small description, then refine. This composes directly with MinT's million-adapter catalog: the routing decision for a 10^6-adapter fleet cannot wait for empirical trials on every new adapter.

## Key findings

1. **Structured > flat.** Profiles that encode taxonomic hierarchy (skill family → sub-skill → query type) consistently outperform per-domain flat profiles across all three routers tested. The ablation isolates organizational form from representation type; the gain is from structure, not from richer features.
2. **Query-level > domain-level.** A profile that summarizes a model's behavior on specific query patterns generalizes better than one that aggregates by domain (math, code, reasoning). Domain labels are too coarse to predict routing quality.
3. **Trainable configurations close the new-model gap.** When a new LLM is added without empirical traces, structured + trainable profiles maintain accuracy; frozen or flat profiles collapse.

## Connections to prior wiki pages

- [TraceR](2026-04-17-tracer-llm-routing.md) — used query-level features for the router but not for the profile. RouteProfile says the profile should also be query-level. The natural composition: a TraceR-style router using a RouteProfile-style profile.
- [Netflix State of Routing](2026-05-08-netflix-state-of-routing-model-serving.md) — Netflix's production routing pipeline is largely domain-bucketed. RouteProfile suggests this is the wrong default; query-level profiles are the production target.
- [MinT](../inference-efficiency/2026-05-14-mint-million-scale-lora-serving.md) — 10^6 adapter catalog is exactly the regime where domain-bucketed profiles fail. RouteProfile gives MinT the missing addressing layer.
- [llm-routing.md](llm-routing.md) — concept page should add "profile design" as a first-class research axis alongside router design.

## Research angle

Three threads worth pulling.

1. **Profile-router co-training.** RouteProfile keeps the router fixed and studies the profile. The natural extension is to co-train both: the profile changes the router's input distribution, and the router's gradient should flow through the profile representation. Joint optimization is the cleaner formulation.
2. **Profile compression.** A query-level profile for 10^6 adapters is hundreds of MB per adapter if naive. The compression problem (what's the minimum profile that supports correct routing?) is unstudied.
3. **Profiles for adapter routing, not model routing.** RouteProfile's experiments are on model fleets. Whether the same design choices transfer to adapter fleets (where the base is shared) is open. The four design dimensions may have different optima when the policy delta is sub-1%-of-base instead of a different model.

## Links

- [Paper](https://arxiv.org/abs/2605.00180)
- [HuggingFace](https://huggingface.co/papers/2605.00180)
- [Raw farmer file](../../raw/huggingface/2026-05-15-routeprofile-elucidating-the-design-space-of-llm-profiles-for-rout.md)
- Related: [llm-routing.md](llm-routing.md), [MinT](../inference-efficiency/2026-05-14-mint-million-scale-lora-serving.md), [CARE](2026-05-11-care-bi-level-routing-moe-continual-learning.md)
