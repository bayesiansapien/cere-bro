---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.00923
url: https://huggingface.co/papers/2610.00923
arxiv_url: https://arxiv.org/abs/2610.00923
date: 2026-10-06
---

# CANOPY: Adaptive-Granularity Evidence Compression for Multimodal RAG

Multimodal RAG retrieves text, tables, images, and videos, but choosing a retrieval granularity does not determine how much context to retain within each item. Coarse units include irrelevant content, while uniformly fine selection can remove context needed to interpret the evidence. Existing compressors address this trade-off with modality-specific mechanisms, leaving open a shared procedure for adapting the retained extent region by region across heterogeneous items. We introduce CANOPY (Canonical Projection over Hierarchy), a framework for adaptive-granularity post-retrieval evidence compression. CANOPY represents retrieved items as hierarchies and uses a node encoder fine-tuned on gold evidence to score regions against the query. Parent-relative refinement compares these scores to select multiple regions at different granularities without LLM calls for node-level pruning. Because compression cannot recover evidence that was never retrieved, a critic requests targeted follow-up retrieval when it judges the accumulated evidence insufficient; newly retrieved items are compressed before being added. Across five QA benchmarks over a 33M-item heterogeneous corpus, CANOPY achieves higher average answer accuracy than the evaluated retrieval baselines. Ablations indicate that additional retrieval drives the main accuracy gains on multi-hop QA. In the unrouted Qwen3-VL-8B-Instruct setting, compression reduces reader-input evidence tokens by 14.2-27.7% relative to the same iterative pipeline without compression, with comparable answer accuracy.
