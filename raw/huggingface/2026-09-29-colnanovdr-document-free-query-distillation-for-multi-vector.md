---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.932565+00:00
arxiv_id: 2609.34899
url: https://huggingface.co/papers/2609.34899
arxiv_url: https://arxiv.org/abs/2609.34899
date: 2026-09-29
---

# ColNanoVDR: Document-Free Query Distillation for Multi-Vector Visual Document Retrieval via Optimal Transport

Multi-vector retrievers built on vision-language models lead visual document retrieval (VDR), but they run a multi-billion-parameter query encoder on every search. Distilling this encoder into a small student that queries the teacher's existing index would remove the bottleneck. The standard recipe, however, matches the teacher's MaxSim scores and so requires encoding and caching every training page, which can reach terabytes of page tokens. NanoVDR avoids pages entirely by training on the teacher's query embeddings alone, but only for single-vector retrievers. We present ColNanoVDR, to our knowledge the first framework to bring this document-free distillation to multi-vector VDR. Its objective, OTW (Optimal Transport with Learned Weights), aligns the student's query tokens with the teacher's by entropic optimal transport, with a learned weight for each student token, and needs no correspondence between the two tokenizations. We prove that the resulting alignment cost bounds the MaxSim score difference on every page. Distilled from five state-of-the-art teachers, the 149M text-only students retain about 95% of their teachers' NDCG@5 on ViDoRe v1-v3 while encoding queries up to 26x faster. Under identical training, OTW matches score distillation while encoding no page and reading 12.6x less cached teacher data.
