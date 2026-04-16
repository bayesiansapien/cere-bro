---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.08046
category: cs.CL
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.08046
published: 2026-04-16
authors: Zhengyi Zhao, Shubo Zhang, Zezhong Wang
---

# Guaranteeing Knowledge Integration with Joint Decoding for Retrieval-Augmented Generation

**arXiv:** https://arxiv.org/abs/2604.08046
**Authors:** Zhengyi Zhao, Shubo Zhang, Zezhong Wang

## Abstract

arXiv:2604.08046v2 Announce Type: replace  Abstract: Retrieval-Augmented Generation (RAG) significantly enhances Large Language Models (LLMs) by providing access to external knowledge. However, current research primarily focuses on retrieval quality, often overlooking the critical ''integration bottleneck'': even when relevant documents are retrieved, LLMs frequently fail to utilize them effectively due to conflicts with their internal parametric knowledge. In this paper, we argue that implicitly resolving this conflict in a single generation pass is suboptimal. We introduce GuarantRAG, a framework that explicitly decouples reasoning from evidence integration. First, we generate an ''Inner-Answer'' based solely on parametric knowledge to capture the model's reasoning flow. Second, to guarantee faithful evidence extraction, we generate a ''Refer-Answer'' using a novel Contrastive DPO objective. This objective treats the parametric Inner-Answer as a negative constraint and the retrieved documents as positive ground truth, forcing the model to suppress internal hallucinations in favor of external evidence during this phase. Finally, rather than naive concatenation or using the DPO trained model directly, we propose a joint decoding mechanism that dynamically fuses the logical coherence of the Inner-Answer with the factual precision of the Refer-Answer at the token level. Experiments on five QA benchmarks demonstrate that GuarantRAG improves accuracy by up to 12.1% and reduces hallucinations by 16.3% compared to standard and dynamic RAG baselines.
