---
source: farmer/huggingface
farmed: 2026-05-19T09:55:00.432604+00:00
arxiv_id: 2605.16839
url: https://huggingface.co/papers/2605.16839
arxiv_url: https://arxiv.org/abs/2605.16839
date: 2026-05-19
---

# CompactAttention: Accelerating Chunked Prefill with Block-Union KV Selection

Chunked prefill has become a widely adopted serving strategy for long-context large language models, but efficient attention computation in this regime remains challenging. Existing sparse attention methods are primarily designed for one-shot prefill and do not translate efficiently to chunked prefill: block-sparse kernels lose efficiency when the query length is limited by the chunk size, while fine-grained pattern search becomes costly when repeated over the accumulated KV cache at every chunk. QUOKA, a recent method that directly targets chunked prefill, avoids sparse-kernel overhead but relies on query-subsampled, token-level KV selection, which can miss query-specific KV entries and introduce explicit KV-copy overhead. To address these limitations, we propose CompactAttention, a chunked-prefill attention mechanism based on Block-Union KV Selection. CompactAttention treats 2D block-sparse masks as KV-selection signals rather than direct sparse-kernel execution plans, and converts them into GQA-aware per-group KV block tables through Q-block union and intra-group union. This construction produces the minimal block tables that preserve all KV blocks selected by the input masks under paged execution constraints, enabling selected KV blocks to be accessed in place without explicit KV compaction. On LLaMA-3.1-8B-Instruct, CompactAttention maintains accuracy close to dense attention on the RULER benchmark while delivering up to 2.72times attention speedup at 128K context length under chunked prefill.
