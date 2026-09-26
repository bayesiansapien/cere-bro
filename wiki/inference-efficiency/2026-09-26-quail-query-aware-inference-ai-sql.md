# Quail: planning the SQL query and the LLM inference together

**Source:** [Building an Ultra-High Throughput AI-SQL Engine](https://fsdatalab.github.io/blog/introducing-quail/) (Full Stack Data Lab, CMU, with Modal). Code: [fsdatalab/quail](https://github.com/fsdatalab/quail). Announced by [@sh_reya](https://x.com/sh_reya/status/2103207153821688056) and [@charles_irl](https://x.com/charles_irl/status/2103222839507652640); the day's most-viewed research post on the X home feed.
**Raw:** `raw/twitter/feed/2026-09-26-morning-ranked.json` (announcement); blog body read directly.

## TL;DR

AI-SQL lets you write a WHERE clause in English, such as `AI.IF("the review discusses the ending")`, and an LLM evaluates it on every row. A single query can mean millions of LLM calls, one per row for a filter or one per row pair for a join. Running them through vLLM as independent requests wastes the GPU twice: the CPU scheduler leaves it idle between requests, and the KV cache (the stored attention state of each document) gets thrown away and recomputed when the same document is needed again by the next operator. Quail (QUery Aware Inference Layer) treats the query plan and the inference plan as one optimization problem. It orders AI operators by cost and selectivity, keeps a document's KV resident in HBM for exactly as long as later operators need it, and for joins computes one shared anchor document's attention once for a whole group of partners. On one H100 running Qwen3 4B in FP8, its hardest benchmark query drops from 6.84 hours to 29 minutes, and cost from $27.03 to $1.93.

![Quail architecture](../../raw/assets/2026-09-26-quail-architecture.svg)

## How it works

- **Query planning with inference costs.** Classical rewrites (push filters and projections down) plus cost-based ordering of AI filters by estimated selectivity. For joins, a Selinger-style (System R) search picks both the join order and which side is the "anchor" whose KV gets reused. The planner sets the forward-pass token budget and per-GPU KV capacity from model size and HBM.
- **KV rewinding.** After evaluating a filter, Quail drops only the predicate-specific suffix of the cache and keeps the document's KV. If the document survives and a later operator needs it, the KV is still in HBM. If not, it is freed. When eviction is forced, it evicts short documents first, because attention cost grows quadratically, so long documents are the expensive ones to recompute.
- **Vectorized, pipelined execution.** A pull-based executor in the style of Apache DataFusion streams batches between operators instead of materializing tables. The CPU prepares the next batch while the GPU runs the current one, which removes the host-side idle gaps visible in vLLM's profile.
- **Tree attention for joins.** Partners that share an anchor are grouped. Attention runs as two FlashAttention-3 calls, one causal over each partner's suffix and one from all partner queries onto the shared anchor KV, merged with log-sum-exp (the online-softmax trick). Anchor KV is read once per group instead of once per partner, the same idea as SpecInfer and Hydragen prefix sharing.
- **Kernel and head trimming.** Custom Triton kernels fuse normalization with FP8 quantization and QK-norm with RoPE. The output head computes only the TRUE and FALSE token logits, not the full vocabulary.

## Key numbers

- **BIO-4 at full scale** (5,000 medical reports joined against 4,144 reaction terms): **29.3 minutes vs 6.84 hours, 14.0x faster**, $1.93 vs $27.03 per query. 19.0M requested input tokens per second vs 1.36M, which is the "1B+ tokens per minute" headline.
- **KV regret** (tokens recomputed because their cache was discarded too early) drops from 50.3M to 18.0M.
- **Across all 29 QUAIL-B queries** (scale factor 0.1): 1.84x geometric-mean speedup over stock vLLM, but **only 1.12x over pipelined vLLM**. Most of the broad-suite gain is removing host overhead. The KV-residency and join tricks matter most on join-heavy queries.
- **Against an API:** two sequential filters over 100,000 reviews cost $0.37 on Quail against about $1.75 on GPT-5 nano with cached tokens.
- **Distance from the limit:** Quail runs at about 2x its own speed-of-light estimate on BIO-4 (vLLM at 27.6x), and 9% to 32% of the ideal throughput depending on dataset.

## Limitations

- No automatic prefix caching across different documents with matching prefixes. On AGENT-1 Quail is **2.3x slower than stock vLLM** (239 s vs 103 s) for this reason.
- Multi-GPU is naive random partitioning. Only filters and joins are supported as AI operators.
- All results are single-H100, small models (4B and 32B, FP8).

## How this relates to prior wiki pages

- **A new workload class for the [kv-cache](kv-cache.md) page.** Every KV page so far assumes a chat or agent workload where the cache belongs to one conversation. Here the cache belongs to a *database row*, and its lifetime is set by the query plan. That makes eviction a planning problem with known future accesses, which is the situation where near-optimal (Belady-style) eviction is actually achievable.
- **Same move as [LM-CXD (09-24)](../hardware/2026-09-24-lm-cxd-cxl-ssd-prefix-cache.md)** and the KVMEM paged-memory work: treat KV as managed data with a lifecycle, not a per-request scratchpad.
- **Contrast with decision models.** The [llm-routing](../ai-routing/llm-routing.md) page's decision-model thread cuts cost by returning one typed answer per call. Quail's output head also returns only TRUE/FALSE. It gets the same single-token-output saving from a stock 4B model plus systems work, with no special model.
- **CPU tie-in.** Part of Quail's win is removing CPU scheduling overhead from the GPU's critical path, the host-side cost the [CPU shortage essay (09-25)](../hardware/2026-09-25-cpu-shortage-agents-and-rl.md) says is now scarce.

## Links

- Concept pages: [kv-cache](kv-cache.md) · [gpu-kernels](../hardware/gpu-kernels.md)
- Figure: `raw/assets/2026-09-26-quail-architecture.svg`, `raw/assets/2026-09-26-quail-join-attention.svg`
