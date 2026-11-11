---
source: farmer/huggingface
farmed: 2026-11-11T05:06:31.325760+00:00
arxiv_id: 2611.08935
url: https://huggingface.co/papers/2611.08935
arxiv_url: https://arxiv.org/abs/2611.08935
date: 2026-11-10
---

# SkinMind: Equipping Agentic RAG with Human-Inspired Graph Probing for Reliable Dermatology AI

Reliable dermatology AI requires access to verifiable evidence distributed across heterogeneous textual and visual sources. However, conventional retrieval-augmented generation (RAG) typically relies on one-shot retrieval from flat corpora, limiting its ability to adapt retrieval granularity, explore multi-hop relations, and integrate multimodal clinical evidence. We introduce SkinMind, a multimodal agentic RAG framework that equips policy models with human-inspired graph probing for autonomous evidence seeking. SkinMind organizes retrieval as an iterative interaction between an orchestrator and a graph environment. Through eight hierarchical graph-probing tools, the orchestrator progressively identifies relevant entities, inspects node-level information, traverses relations and paths, and retrieves source-text and visual evidence. This progressive-disclosure design allows the model to adaptively determine the retrieval modality, exploration direction, and evidence granularity while constructing a query-specific evidence subgraph. To support autonomous graph probing, we construct SkinMind-KG from a 62M-token corpus of dermatology guidelines and textbooks and 423K images, guided by a dermatologist-informed schema and a conflict-resolution mechanism. The resulting graph contains over 1.0M nodes and 2.0M edges, unifying textual, relational, and visual evidence for retrieval. Across six dermatology VQA benchmarks and two policy-model settings, SkinMind improves the average score over direct answering by 8.70 and 8.89 points with GPT-5.4-mini and Gemini-2.5-Flash, respectively, while consistently outperforming competing RAG methods. Together, SkinMind and SkinMind-KG provide an effective foundation for evidence-grounded multimodal reasoning in dermatology.
