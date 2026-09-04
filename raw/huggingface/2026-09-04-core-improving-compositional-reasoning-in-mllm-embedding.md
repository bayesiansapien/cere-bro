---
source: farmer/huggingface
farmed: 2026-09-04T10:50:04.492861
arxiv_id: 2609.04083
url: https://huggingface.co/papers/2609.04083
arxiv_url: https://arxiv.org/abs/2609.04083
date: 2026-09-04
---

# CORE: Improving Compositional Reasoning in MLLM Embedding via Reranker Distillation

MLLM-based embedding models remain limited in compositional retrieval, often failing to distinguish scenes containing the same concepts but different attribute-object bindings. Yet the same backbone can resolve such distinctions when used as a cross-attentive reranker, motivating us to distill its compositional judgments into the embedding model. We propose CORE, which synthesizes candidate lists spanning five compositional matching levels and introduces a Rank-KL objective that trains the embedding model to reproduce the reranker's fine-grained ranking. We further introduce a graded evaluation protocol and compare contrastive learning, pairwise CoSENT, and listwise Rank-KL under the same data and tuning budget. Our comparison shows that both CoSENT and Rank-KL use the multi-level supervision more effectively than contrastive learning, with Rank-KL achieving the strongest overall performance. Across three compositional reasoning benchmarks (COLA, SUGARCREPE++, NEGBENCH), CORE-RERANKER-8B achieves an 82.7% total average, outperforming Jina-Reranker by 10.7 points, while CORE-EMBED-8B achieves the best total average (0.666) among all evaluated embedding models. The improvements transfer to the MCMR benchmark without sacrificing retrieval performance on COCO and Flickr30K.
