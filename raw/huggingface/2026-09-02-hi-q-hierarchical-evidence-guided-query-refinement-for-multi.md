---
source: farmer/huggingface
farmed: 2026-09-02T13:31:46.243214
arxiv_id: 2608.30468
url: https://huggingface.co/papers/2608.30468
arxiv_url: https://arxiv.org/abs/2608.30468
date: 2026-09-02
---

# Hi-Q: Hierarchical Evidence-guided Query Refinement for Multi-Hop Question Answering

A central bottleneck in multi-hop Question Answering (QA) is that the granularity at which a question is expressed often differs from the granularity at which corpus evidence is retrievable. Existing methods address this mismatch by imposing fixed graph structures over the corpus, by iteratively reformulating the query, or by executing a generated program over it, but these strategies do not explicitly decide when a query unit is already supported by evidence and when it should be refined. We formulate this bottleneck as retrievable granularity discovery and introduce Hi-Q, an evidence-conditioned framework for hierarchical query refinement. At each query node, a resolution operator tests whether retrieved evidence supports the current query unit; resolved nodes terminate, while unresolved nodes are expanded by a dependency-preserving binary operator and checked by a semantic coverage verifier. Hi-Q therefore grows a query tree whose topology is determined by corpus support signals rather than by a fixed decomposition template or a pre-built graph. We evaluate Hi-Q on three multi-hop QA benchmarks, primarily under full-corpus retrieval, where dependent evidence must be located among open-domain distractors rather than within a small annotated pool. In this setting Hi-Q reaches 52.3 EM and 64.0 F1 averaged over the three benchmarks, ahead of the iterative retrieval baseline IRCoT by 15.1 EM / 18.2 F1 on that same average, and ahead of the graph-based RAG baseline PropRAG by 11.5 EM / 12.0 F1 on MuSiQue-full, without corpus-wide graph construction. In the restricted supporting/distractor setting used by prior work, Hi-Q likewise attains the best accuracy, with 57.9 EM and 69.3 F1 on average, ahead of PropRAG by 5.6 EM / 3.9 F1 and IRCoT by 13.7 EM / 15.8 F1. The project page is available at https://hi-q-project.github.io/.
