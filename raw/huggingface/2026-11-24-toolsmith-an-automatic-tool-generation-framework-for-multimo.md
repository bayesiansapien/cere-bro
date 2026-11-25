---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.924166+00:00
arxiv_id: 2611.31198
url: https://huggingface.co/papers/2611.31198
arxiv_url: https://arxiv.org/abs/2611.31198
date: 2026-11-24
---

# ToolSmith: An Automatic Tool-Generation Framework for Multimodal Search Agents

Recent multimodal search agents use reasoning, vision, and live web search across many turns to answer questions beyond parametric knowledge by orchestrating a small library of hand-crafted search and visual tools. However, the library is laborious to create and maintain, and frozen when new query types, evidence formats, and failure modes are encountered in the wild. Human practitioners, by contrast, cope with insufficient tools by fashioning new ones from familiar parts and reusing them across tasks. Inspired by this, we propose ToolSmith, an automatic tool-generation framework that grows and reuses modules on top of a lean base tool library. We evaluate ToolSmith on three in-domain multimodal search benchmarks and ten out-of-domain benchmarks under a VLM-as-a-Judge protocol. ToolSmith consistently improves over the base library across deployed agents of varying scales, with larger backbones reaping greater gains, demonstrating the scalability of the approach. Our code and data are available at https://threesr.github.io/toolsmith/.
