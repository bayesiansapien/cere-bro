---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.385206+00:00
arxiv_id: 2611.26268
url: https://huggingface.co/papers/2611.26268
arxiv_url: https://arxiv.org/abs/2611.26268
date: 2026-11-20
---

# Accelerating Mixture of Block Attention via Dynamic Routing, KV-Centric Execution and Runtime Pipelining

Mixture of Block Attention (MoBA) reduces long-context computation by selecting key-value (KV) blocks for each query. FlashMoBA implements MoBA efficiently but retains a fixed Top-k budget and query-centric schedule. Fixed Top-k applies one budget across different score distributions and couples routing to task granularity; query-range ownership fragments K/V reuse when several ranges select the same column. We present LightningMoBA, which co-designs selection and execution through dynamic routing, KV-centric ownership, and runtime pipelining. Dynamic routing thresholds MoBA's per-query block scores and directly emits variable-cardinality sparse metadata. KV-centric ownership groups selected rows by (query head, KV block) column, splits high-fanout columns into bounded tasks, and reuses each task's loaded KV tile. On Hopper, pipelining overlaps regular K/V transfers and irregular query gathers with Tensor Core computation. Together, these mechanisms decouple retention from GPU scheduling granularity. At matched Top-16 retention across five checkpoints, LightningMoBA accelerates end-to-end generation by 1.20 to 1.60x while raising mean RULER score from 74.42 to 75.28.
