---
source: farmer/huggingface
farmed: 2026-04-22T00:00:00
arxiv_id: 2604.17632
url: https://huggingface.co/papers/2604.17632
arxiv_url: https://arxiv.org/abs/2604.17632
date: 2026-04-22
---

# Code-Switching Information Retrieval: Benchmarks, Analysis, and the Limits of Current Retrievers

Code-switching is a pervasive linguistic phenomenon in global communication, yet modern information retrieval systems remain predominantly designed for, and evaluated within, monolingual contexts. To bridge this gap, we present a holistic study of code-switching IR. We introduce the Code-Switching Retrieval benchmark-Lite (CSR-L), a human-annotated benchmark designed to capture natural mixed-language queries, and evaluate statistical, dense, cross-encoder, and late-interaction retrieval methods on it. The results show that code-switching is a persistent performance bottleneck, degrading even strong multilingual models. We further show that this failure is associated with substantial divergence between monolingual and code-switched query embeddings. To test whether the pattern generalizes beyond retrieval, we construct CS-MTEB, a benchmark covering 11 diverse tasks, where performance drops reach up to 27%. Finally, we examine lexicon-based vocabulary expansion and find that, while it yields partial gains, it does not close the gap to monolingual performance. These findings underscore the fragility of current systems and establish code-switching as a crucial frontier for future IR optimization.
