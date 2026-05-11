# CaRE: Scaling Continual Learning to 300+ Tasks with Bi-Level Routing Mixture-of-Experts

**arXiv:** [2602.03473](https://arxiv.org/abs/2602.03473) · **HF Daily Papers:** [page](https://huggingface.co/papers/2602.03473) · **Date:** 2026-05-11
**Tier:** 1 — Routing (bi-level MoE routing for continual learning)
**Authors:** Meng Lou, Yunxiang Fu, Yizhou Yu (HKU)
**Raw:** [farmer file](../../raw/huggingface/2026-05-11-scaling-continual-learning-to-300-tasks-with-bi-level-ro.md)

## TL;DR

Continual learning evaluations typically run 5 to 20 tasks. Real-world settings need 100, 300, or more. CaRE introduces Bi-Level Routing Mixture-of-Experts (BR-MoE) for class-incremental learning on top of pre-trained vision transformers, and scales it to over 300 non-overlapping tasks on a new benchmark, OmniBenchmark-1K. Two levels of routing: a router-selection stage that activates relevant task-specific routers, then an expert-routing stage that activates and aggregates the per-expert outputs. Each network layer gets discriminative and comprehensive representations injected, addressing the long-task-sequence stability-plasticity tradeoff that previous PTM-based CIL methods (MoE-Adapter, SEMA, EASE, MOS, TUNA) only handled at the 5-to-20 task regime.

## What is new

Three contributions.

**Bi-level routing.** Existing MoE-adapter CL methods (MoE-Adapter, SEMA) use a single learned router that picks experts directly from a shared pool. CaRE introduces a router-selection layer above the expert router. The first stage picks which task-specific router is appropriate for the current input, and the second stage runs that router over the expert pool. This gives the model a coarse task-level inductive bias before the fine-grained expert selection runs, which is what makes the architecture scale past the 20-task barrier where flat routing structures saturate.

**Bi-level activation, not just routing.** Each level activates and aggregates outputs (not just selects). The first level produces a task-router output that becomes input to the expert-routing stage. The second level produces an expert mixture that gets injected into the intermediate layer. The injection happens at every layer, not just at the output head. This is what makes the comprehensiveness side of the stability-plasticity tradeoff work: discriminative representations come from the task router, comprehensive ones from the per-layer expert aggregation.

**OmniBenchmark-1K.** The first CIL benchmark at the 100-to-300+ task scale that the wiki has tracked. Existing CL benchmarks have a regime mismatch with production needs.

## Why the bi-level structure matters

Flat MoE routers fail at long sequences for two reasons that are well known in the MoE literature: router collapse (a small subset of experts dominates) and stale-expert forgetting (experts that have not been activated recently drift). Adding a task-router selection layer above the expert pool gives the system a coarser, more stable inductive bias to ground the fine-grained routing in. The task router has many fewer choices to make and changes less often, so it can act as a stable scaffold for the expert pool below.

The architecture is structurally similar to the cross-axis routing the wiki has been seeing in inference efficiency papers. MISA (same day, [2605.07363](../inference-efficiency/2026-05-11-misa-mixture-of-indexer-sparse-attention.md)) routes the head axis of the indexer; CaRE routes the task axis of the expert pool. Both find that adding a second routing axis above an already-learned pool of specialists is the cheaper path than retraining the underlying pool.

## Relation to prior wiki coverage

This is the third routing paper this month with the same architectural shape: a learned router selects from a pool of specialists trained at a different time. The three are now:
1. **Step-level Optimization for Computer-Use Agents (05-02)** routes the model axis per agent step.
2. **MISA (05-11)** routes the indexer-head axis per query.
3. **CaRE (05-11)** routes the task-expert axis per layer.

The pattern is clear: routing is no longer the wrapper around the model, it is the architectural primitive inside the model. The wiki's [LLM Routing concept page](llm-routing.md) is now load-bearing in three directions (query-level, provider-level, trajectory-level) and these inference and training papers add two more: head-level and task-expert-level.

The Conductor paper (Sakana, [Twitter retweet](../../raw/twitter/2026-05-11-morning.md) and DAIR.AI weekly) is the model-level analogue. A 7B Conductor learned to orchestrate larger frontier models. CaRE is the layer-level analogue: a learned router orchestrates a per-task expert pool inside a single model.

## Research angle

**Composition with frozen pre-trained backbones.** CaRE is built on a PTM backbone that is itself frozen. The bi-level router activates adapters inserted on top of that backbone. This composes with adapter-based fine-tuning frameworks like APER-Adapter and MOS. Open question: can the expert pool inherit cross-task generalization from the PTM through a third level of routing that selects which adapter family to consult?

**Memory cost of long task sequences.** The paper does not report on the memory floor of running 300 task routers concurrently. Sparse activation at the task-router level is the obvious follow-up, but it would require lifelong eviction policies analogous to KV cache eviction. The wiki has been tracking content-aware KV eviction (Stream-T1, 05-07); a content-aware task-router eviction policy is the natural cross-pollination.

**Why OmniBenchmark-1K should become a standard.** Until benchmarks tested at 100+ tasks, CL papers reported gains that did not translate to deployment. CaRE's headline win is that the gap between CaRE and baselines grows as the task count grows, exactly the metric prior benchmarks could not measure.

## Links

- [arXiv 2602.03473](https://arxiv.org/abs/2602.03473)
- [HuggingFace](https://huggingface.co/papers/2602.03473)
- [LLM Routing concept page](llm-routing.md)
- [MISA (same-day head-axis routing)](../inference-efficiency/2026-05-11-misa-mixture-of-indexer-sparse-attention.md)
