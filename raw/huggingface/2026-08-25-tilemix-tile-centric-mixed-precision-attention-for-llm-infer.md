---
source: farmer/huggingface
farmed: 2026-08-25T14:22:16.352902
arxiv_id: 2608.17336
url: https://huggingface.co/papers/2608.17336
arxiv_url: https://arxiv.org/abs/2608.17336
date: 2026-08-25
upvotes: 2
authors: ["Hanzhi Zhang", "Qiao Zhang", "Qinglei Cao", "Heng Fan", "Yan Huang", "Kewei Sha", "Yunhe Feng"]
---

# TileMix: Tile-Centric Mixed-Precision Attention for LLM Inference Acceleration

**Upvotes:** 2
**Authors:** Hanzhi Zhang, Qiao Zhang, Qinglei Cao, Heng Fan, Yan Huang, Kewei Sha, Yunhe Feng

Long-context prefill in large language models (LLMs) incurs substantial computation and memory traffic because dense self-attention computes quadratic query-key scores. Existing methods either use a uniform low-precision path or select token interactions, leaving spatial precision routing over hardware-aligned score tiles outside fused dense attention. We introduce TileMix, a tile-centric precision-routing kernel that makes numerical precision an executable spatial decision over score-tile groups within fused dense attention. TileMix partitions the attention matrix into hardware-aligned score tiles, packs routing decisions into compact bitmasks, and dispatches each tile group through FP16 or INT8 score computation while both paths update a shared online-softmax state. Scalable precision grouping lets each routing bit govern multiple adjacent key tiles, preserving hardware-aligned compute tiles and compact metadata at long contexts. By routing all legal tile groups, TileMix preserves dense token connectivity, requires no training, and supports grouped-query attention, variable-length batches, and INT8 key/value caches. Across LongEval, LV-Eval, and A100 prefill benchmarks on LLaMA, Qwen, and Vicuna, TileMix recovers long-context quality lost under uniform INT8 and improves prefill throughput over FP16, yielding a controllable accuracy-efficiency frontier across model families. The implementation is available at https://github.com/HanzhiZhang-Ulrica/TileMix.
