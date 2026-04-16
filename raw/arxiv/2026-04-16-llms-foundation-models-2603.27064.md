---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2603.27064
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2603.27064
published: 2026-04-16
authors: Jovana Kondic, Pengyuan Li, Dhiraj Joshi
---

# ChartNet: A Million-Scale, High-Quality Multimodal Dataset for Robust Chart Understanding

**arXiv:** https://arxiv.org/abs/2603.27064
**Authors:** Jovana Kondic, Pengyuan Li, Dhiraj Joshi

## Abstract

arXiv:2603.27064v2 Announce Type: replace-cross  Abstract: Understanding charts requires models to jointly reason over geometric visual patterns, structured numerical data, and natural language -- a capability where current vision-language models (VLMs) remain limited. We introduce ChartNet, a high-quality, million-scale multimodal dataset designed to advance chart interpretation and reasoning. ChartNet leverages a novel code-guided synthesis pipeline to generate 1.5 million diverse chart samples spanning 24 chart types and 6 plotting libraries. Each sample consists of five aligned components: plotting code, rendered chart image, data table, natural language summary, and question-answering with reasoning, providing fine-grained cross-modal alignment. To capture the full spectrum of chart comprehension, ChartNet additionally includes specialized subsets encompassing human annotated data, real-world data, safety, and grounding. Moreover, a rigorous quality-filtering pipeline ensures visual fidelity, semantic accuracy, and diversity across chart representations. Fine-tuning on ChartNet consistently improves results across benchmarks, demonstrating its utility as large-scale supervision for multimodal models. As the largest open-source dataset of its kind, ChartNet aims to support the development of foundation models with robust and generalizable capabilities for data visualization understanding. The dataset is publicly available at https://huggingface.co/datasets/ibm-granite/ChartNet
