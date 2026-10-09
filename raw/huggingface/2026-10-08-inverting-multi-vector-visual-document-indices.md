---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.305679+05:30
arxiv_id: 2610.09920
url: https://huggingface.co/papers/2610.09920
arxiv_url: https://arxiv.org/abs/2610.09920
date: 2026-10-08
---

# Inverting Multi-Vector Visual Document Indices

Prevailing multi-vector visual document retrievers store each page as about a thousand patch vectors, often in vector databases run by a third party. Since no one can read a page from its vectors, this index is easily treated as less sensitive than the page. However, because the index keeps one vector per patch in raster order, and each vector is computed by a vision-language model pre-trained to read documents, we hypothesize that whoever runs or breaches the store can reproduce a page from its index alone. We frame inversion as conditional document image generation and infer from the vectors what the attack needs: the encoder, the page shape and, for shuffled vectors, their order. On the ViDoRe v3 benchmark, pages inverted from raw indices recover 47% of the words and 45% of the sensitive tokens. Used as queries against the stored indices, they rank their source page first 98.4% of the time. We test two cheap protections, token pooling and shuffling, which both cut word recall to about 8%. A model that restores the order of a shuffled index raises the share of source pages ranked first from 3.8% to 93.5%, while inverting a pooled index remains open. To test generalisation, we apply the same attack unchanged to another multi-vector retriever: its inverted pages still rank their source page first 70.2% of the time, though its word recall stays below a nearest-neighbour baseline. Multi-vector visual document retrievers are therefore vulnerable to inversion through their stored index, which should be protected like the documents it encodes.
