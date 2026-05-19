# CompactAttention: Accelerating Chunked Prefill with Block-Union KV Selection

**arXiv:** [2605.16839](https://arxiv.org/abs/2605.16839) · **HF:** [paper page](https://huggingface.co/papers/2605.16839) · **Tier:** 1 (KV cache, chunked prefill, serving)

## TL;DR

CompactAttention reframes 2D block-sparse masks as KV-selection signals rather than direct sparse-kernel execution plans, then converts them into GQA-aware per-group KV block tables via Q-block union and intra-group union. The resulting block tables are the minimal sets that preserve every KV block any input mask selected under paged execution, so selected blocks can be accessed in place without explicit KV compaction. On LLaMA-3.1-8B-Instruct it holds accuracy close to dense on RULER while delivering up to 2.72x attention speedup at 128K context under chunked prefill.

## Key findings

- Existing sparse attention designed for one-shot prefill does not translate efficiently to chunked prefill. Block-sparse kernels lose efficiency when the query length is limited by the chunk size; fine-grained pattern search becomes costly when repeated over the accumulated KV cache at every chunk.
- QUOKA, the prior method directly targeting chunked prefill, avoids sparse-kernel overhead but relies on query-subsampled, token-level KV selection. This can miss query-specific KV entries and introduces an explicit KV-copy step.
- CompactAttention's structural move is to decouple the mask (a selection signal) from the kernel execution plan (a block table). The 2D block-sparse mask is no longer the thing the kernel runs; it is the input to a union construction that produces a block table indexed per attention group under Grouped-Query Attention.
- The block-table construction is two unions: Q-block union (collect every KV block any Q-block in the current chunk selected) and intra-group union (collect every KV block any head in the same GQA group selected). The result preserves every selected block under paged execution while staying compact.
- Speedup reaches 2.72x at 128K context on LLaMA-3.1-8B-Instruct on the RULER benchmark with accuracy close to dense.

## Relationship to prior wiki entries

CompactAttention is the chunked-prefill specialisation in a thread the [kv-cache concept page](kv-cache.md) has been mapping. Make Each Token Count (2026-05-12, the paper that scored each cached entry with a small projection and showed selective retention can surpass the full cache) attacked eviction at the token level. UniPrefill (2026-05-11, the vLLM operator that does block-wise dynamic sparsification with extended continuous-batching scheduling and tensor parallel) attacked one-shot prefill at the serving-system level. MISA (2026-05-11, the head-axis Mixture of Indexer Sparse Attention) routed sparse attention on the head axis. CompactAttention attacks the third corner: the chunked-prefill regime where the chunk size caps the Q-length and where the prior block-sparse machinery does not translate.

CompactAttention also composes naturally with TurboQuant (2026-04-22, the ultra-low-bit KV-cache quantizer): the block table CompactAttention produces decides which blocks to read; TurboQuant decides how many bits per cell to read them at. The two axes are orthogonal.

## Why it matters

Chunked prefill is now the default serving pattern at long context: the controller breaks the prompt into chunks and incrementally extends the KV cache rather than computing prefill in one go. This is the regime where 128K-plus contexts actually live in production. The 2.72x attention speedup at 128K with near-dense accuracy is the second meaningful chunked-prefill kernel result the wiki has tracked, after UniPrefill. The structural insight (mask as selection signal, not execution plan) is the part likely to generalise: any sparse-attention method can run its existing mask-generation logic and then hand the mask to CompactAttention's union construction instead of running its own kernel.

## Research angle

- **Does the union construction's cost amortise at extreme context (256K, 512K)?** The paper reports 128K. Whether the 2.72x at 128K extends to 4x at 256K or saturates is the load-bearing extrapolation.
- **How does CompactAttention compose with head-role compression (Forcing-KV 2026-05-15) and learned eviction (Make Each Token Count)?** The composition produces a per-group, per-role, per-token KV plan. The diagnostic is whether the speedups stack or share a common bottleneck.
- **Per-token routing on the union output.** Could a learned router decide, per token, which Q-block union members to actually read? The current method reads all blocks in the union. A learned head-axis or token-axis filter on top would reduce the union further at some accuracy cost.

## Source

`raw/huggingface/2026-05-19-compactattention-accelerating-chunked-prefill-with-block-uni.md`
