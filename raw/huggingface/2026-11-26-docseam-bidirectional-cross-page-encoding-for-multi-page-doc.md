---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.903515+00:00
arxiv_id: 2611.34420
url: https://huggingface.co/papers/2611.34420
arxiv_url: https://arxiv.org/abs/2611.34420
date: 2026-11-26
---

# DocSEAM: Bidirectional Cross-Page Encoding for Multi-Page Document Understanding

Multi-page document vision-language models encode each page independently, creating a feature-level discontinuity at page boundaries: visual tokens are formed without access to content on adjacent pages, and the language model must reason over these page representations formed in isolation. We introduce DocSEAM (Document Selective Enrichment via Anchored Masking), a lightweight module inserted between a pretrained vision encoder and the language model that injects the inductive bias of local cross-page context into visual representations. For each page, DocSEAM forms a local triplet with its two neighbors, applies center-anchored masked self-attention with directional salience gates to fuse information from neighbor pages, and returns only the enriched center-page tokens, leaving the visual token count unchanged. After a supervised cross-page warm-up and multi-page fine-tuning with DocSEAM frozen, our 9B-parameter model achieves state-of-the-art results among the evaluated open-weight models of up to 10B parameters on five multi-page document VQA benchmarks. We further show that under controlled re-pagination, DocSEAM reduces sensitivity to boundary placement and improves cross-page span localization
