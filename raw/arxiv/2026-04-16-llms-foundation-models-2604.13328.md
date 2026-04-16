---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13328
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13328
published: 2026-04-16
authors: Jiahao Shao, Anam Nawaz Khan, Christopher Brett
---

# Multi-Task LLM with LoRA Fine-Tuning for Automated Cancer Staging and Biomarker Extraction

**arXiv:** https://arxiv.org/abs/2604.13328
**Authors:** Jiahao Shao, Anam Nawaz Khan, Christopher Brett

## Abstract

arXiv:2604.13328v1 Announce Type: new  Abstract: Pathology reports serve as the definitive record for breast cancer staging, yet their unstructured format impedes large-scale data curation. While Large Language Models (LLMs) offer semantic reasoning, their deployment is often limited by high computational costs and hallucination risks. This study introduces a parameter-efficient, multi-task framework for automating the extraction of Tumor-Node-Metastasis (TNM) staging, histologic grade, and biomarkers. We fine-tune a Llama-3-8B-Instruct encoder using Low-Rank Adaptation (LoRA) on a curated, expert-verified dataset of 10,677 reports. Unlike generative approaches, our architecture utilizes parallel classification heads to enforce consistent schema adherence. Experimental results demonstrate that the model achieves a Macro F1 score of 0.976, successfully resolving complex contextual ambiguities and heterogeneous reporting formats that challenge traditional extraction methods including rule-based natural language processing (NLP) pipelines, zero-shot LLMs, and single-task LLM baselines. The proposed adapter-efficient, multi-task architecture enables reliable, scalable pathology-derived cancer staging and biomarker profiling, with the potential to enhance clinical decision support and accelerate data-driven oncology research.
