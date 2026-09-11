---
source: farmer/huggingface
farmed: 2026-09-11T21:57:41.002444
arxiv_id: 2609.11808
url: https://huggingface.co/papers/2609.11808
arxiv_url: https://arxiv.org/abs/2609.11808
date: 2026-09-11
---

# Generative Late-Interaction Embeddings For Visual Document Retrieval

Late-interaction retrieval is the state-of-the-art for visual document search, but it pays for its accuracy in storage. Existing compression methods retain a subset or local average of the N~1,000 vectors per page. Under aggressive storage budgets, however, these methods degrade sharply, and alternatives require retraining the encoder. Investigating this degradation across three encoders, we found two consistent properties: the vectors lie exactly on the unit sphere and concentrate near a manifold of intrinsic dimension five to six. This geometry yields two insights. First, standard k-means centroids fall inside the sphere, causing systematic underestimation of MaxSim scores. Normalizing them to the surface is a free correction worth up to +0.093 nDCG@5 over raw centroids. Second, because the page manifold has few degrees of freedom, the full set of vectors can be regenerated from only a few. To this end, we introduce Generative Late-Interaction Embeddings (GLIE): k << N vectors per page learned from the normalized centroids to serve as both a lightweight index and a basis for regenerating the page's full embedding set. At query time, search runs exclusively on these k vectors, and a decoder expands only the top candidates back to all N vectors for exact rescoring. At four vectors per page on ViDoRe v1, GLIE retains nearly 80% of the uncompressed system's nDCG@5, against 70% for the best prior post-hoc method. These results use a 415K-parameter network fitted in under three GPU-minutes on just a thousand training pages. At a matched training budget, fine-tuning the encoder does not reach even the training-free stage of GLIE, and the full system beats it at every budget. These patterns hold across a second encoder and ViDoRe v2. By reconstructing evidence on demand rather than sampling it, GLIE opens a new axis for storage-efficient retrieval, with the decoder as its main design surface.
