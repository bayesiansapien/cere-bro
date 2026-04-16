---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2603.01410
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2603.01410
published: 2026-04-16
authors: Yuchen Ying, Weiqi Jiang, Tongya Zheng
---

# GraphScout: Empowering Large Language Models with Intrinsic Exploration Ability for Agentic Graph Reasoning

**arXiv:** https://arxiv.org/abs/2603.01410
**Authors:** Yuchen Ying, Weiqi Jiang, Tongya Zheng

## Abstract

arXiv:2603.01410v2 Announce Type: replace  Abstract: Knowledge graphs provide structured and reliable information for many real-world applications, motivating increasing interest in combining large language models (LLMs) with graph-based retrieval to improve factual grounding. Recent Graph-based Retrieval-Augmented Generation (GraphRAG) methods therefore introduce iterative interaction between LLMs and knowledge graphs to enhance reasoning capability. However, existing approaches typically depend on manually designed guidance and interact with knowledge graphs through a limited set of predefined tools, which substantially constrains graph exploration. To address these limitations, we propose GraphScout, a training-centric agentic graph reasoning framework equipped with more flexible graph exploration tools. GraphScout enables models to autonomously interact with knowledge graphs to synthesize structured training data which are then used to post-train LLMs, thereby internalizing agentic graph reasoning ability without laborious manual annotation or task curation. Extensive experiments across five knowledge-graph domains show that a small model (e.g., Qwen3-4B) augmented with GraphScout outperforms baseline methods built on leading LLMs (e.g., Qwen-Max) by an average of 16.7\% while requiring significantly fewer inference tokens. Moreover, GraphScout exhibits robust cross-domain transfer performance. Our code will be made publicly available~\footnote{https://github.com/Ying-Yuchen/_GraphScout_}.
