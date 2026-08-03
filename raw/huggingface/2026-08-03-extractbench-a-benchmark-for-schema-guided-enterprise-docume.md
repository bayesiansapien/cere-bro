---
source: farmer/huggingface
farmed: 2026-08-03T12:36:11.005337+05:30
arxiv_id: 2607.29677
url: https://huggingface.co/papers/2607.29677
arxiv_url: https://arxiv.org/abs/2607.29677
date: 2026-08-03
---

# ExtractBench: A Benchmark for Schema-Guided Enterprise Document Extraction

Enterprise workflows increasingly rely on agents for schema-guided extraction: given a document and a user-defined schema, the agent faithfully follows the schema to produce the correct output with source evidence as grounding metadata. We present ExtractBench, a benchmark for schema-guided extraction and, to our knowledge, the first to score value accuracy, record completeness at scale, grounding, and measured cost together. The evaluation system contains 4,869 pages across 370 enterprise documents, 8 business domains, and 67 document types, with clear tags differentiating their challenge scenarios. The scalable schema and ground-truth curation pipeline combines independent-system agreement for real documents, known values for synthetic lists, and human verification for forms. We report order-insensitive value F1 for value accuracy, plus two grounding metrics for source traceability: word- and page-level F1. Commercial VLMs perform well on short documents but often truncate record lists on long ones, while coding agents retain higher accuracy at much higher cost. LlamaExtract Agentic Plus ranks first on all three metrics, with accuracy comparable to coding agents at a fraction of the cost. Dataset and evaluation code are available on https://huggingface.co/datasets/llamaindex/ExtractBench{HuggingFace} and https://github.com/run-llama/ExtractBench{GitHub}.
