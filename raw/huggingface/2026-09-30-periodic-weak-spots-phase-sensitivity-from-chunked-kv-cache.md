---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.36322
url: https://huggingface.co/papers/2609.36322
arxiv_url: https://arxiv.org/abs/2609.36322
date: 2026-09-30
---

# Periodic Weak Spots: Phase Sensitivity from Chunked KV-Cache Compression

Chunked KV-cache compression reduces the memory and attention costs of long-context inference by compressing windows of consecutive tokens into fewer cache entries at a fixed stride. Such compression also introduces a new positional coordinate: a token's phase, or its position relative to compression-window boundaries. We uncover a systematic asymmetry in models using such compression: the same information can be easy to retrieve at one phase and difficult at another. We call this periodic variation in retrieval performance phase sensitivity. In large open-weight models with such compression, long-context retrieval accuracy can differ by up to 40 percentage points across phases, revealing periodic weak spots that average benchmark scores can conceal.
  To investigate this behavior, we pretrain a family of transformers from scratch across multiple KV-compression designs, reproducing phase sensitivity across the variants. Mechanistic analysis using causal interventions in these models reveals phase specialization: different attention components contribute asymmetrically to retrieving information at different source phases. We further analyze idealized retrieval models, showing how gradient flow dynamics may favor sharp phase specialization. Evaluating models with chunked KV-cache compression thus requires measuring across compression phases: high average accuracy can coexist with systematic positional failures.
