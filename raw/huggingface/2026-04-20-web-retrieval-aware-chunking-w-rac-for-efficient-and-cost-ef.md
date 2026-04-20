---
source: farmer/huggingface
farmed: 2026-04-20T00:00:00
arxiv_id: 2604.04936
url: https://huggingface.co/papers/2604.04936
arxiv_url: https://arxiv.org/abs/2604.04936
date: 2026-04-20
---

# Web Retrieval-Aware Chunking (W-RAC) for Efficient and Cost-Effective Retrieval-Augmented Generation Systems

Retrieval-Augmented Generation (RAG) systems critically depend on effective document chunking strategies to balance retrieval quality, latency, and operational cost. Traditional chunking approaches—such as fixed-size, rule-based, or fully agentic chunking—often suffer from high token consumption, redundant text generation, limited scalability, and poor debuggability, especially for large-scale web content ingestion. In this paper, we propose Web Retrieval-Aware Chunking (W-RAC), a novel, cost-efficient chunking framework designed specifically for web-based documents. W-RAC decouples text extraction from semantic chunk planning by representing parsed web content as structured, ID-addressable units and leveraging large language models (LLMs) only for retrieval-aware grouping decisions rather than text generation. This significantly reduces token usage, eliminates hallucination risks, and improves system observability. Experimental analysis and architectural comparison demonstrate that W-RAC achieves comparable or better retrieval performance than traditional chunking approaches while reducing chunking-related LLM costs by an order of magnitude.
