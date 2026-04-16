---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13048
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13048
published: 2026-04-16
authors: Twinkll Sisodia
---

# From Natural Language to PromQL: A Catalog-Driven Framework with Dynamic Temporal Resolution for Cloud-Native Observability

**arXiv:** https://arxiv.org/abs/2604.13048
**Authors:** Twinkll Sisodia

## Abstract

arXiv:2604.13048v1 Announce Type: cross  Abstract: Modern cloud-native platforms expose thousands of time series metrics through systems like Prometheus, yet formulating correct queries in domain-specific languages such as PromQL remains a significant barrier for platform engineers and site reliability teams. We present a catalog-driven framework that translates natural language questions into executable PromQL queries, bridging the gap between human intent and observability data. Our approach introduces three contributions: (1) a hybrid metrics catalog that combines a statically curated base of approximately 2,000 metrics with runtime discovery of hardware-specific signals across GPU vendors, (2) a multi-stage query pipeline with intent classification, category-aware metric routing, and multi-dimensional semantic scoring, and (3) a dynamic temporal resolution mechanism that interprets diverse natural language time expressions and maps them to appropriate PromQL duration syntax. We integrate the framework with the Model Context Protocol (MCP) to enable tool-augmented LLM interactions across multiple providers. The catalog-driven approach achieves sub-second metric discovery through pre-computed category indices, with the full pipeline completing in approximately 1.1 seconds via the catalog path. The system has been deployed on production Kubernetes clusters managing AI inference workloads, where it supports natural language querying across approximately 2,000 metrics spanning cluster health, GPU utilization, and model-serving performance.
