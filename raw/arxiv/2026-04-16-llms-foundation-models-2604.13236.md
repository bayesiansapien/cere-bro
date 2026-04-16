---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13236
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13236
published: 2026-04-16
authors: Shivam Chand Kaushik
---

# SemiFA: An Agentic Multi-Modal Framework for Autonomous Semiconductor Failure Analysis Report Generation

**arXiv:** https://arxiv.org/abs/2604.13236
**Authors:** Shivam Chand Kaushik

## Abstract

arXiv:2604.13236v1 Announce Type: cross  Abstract: Semiconductor failure analysis (FA) requires engineers to examine inspection images, correlate equipment telemetry, consult historical defect records, and write structured reports, a process that can consume several hours of expert time per case. We present SemiFA, an agentic multi-modal framework that autonomously generates structured FA reports from semiconductor inspection images in under one minute. SemiFA decomposes FA into a four-agent LangGraph pipeline: a DefectDescriber that classifies and narrates defect morphology using DINOv2 and LLaVA-1.6, a RootCauseAnalyzer that fuses SECS/GEM equipment telemetry with historically similar defects retrieved from a Qdrant vector database, a SeverityClassifier that assigns severity and estimates yield impact, and a RecipeAdvisor that proposes corrective process adjustments. A fifth node assembles a PDF report. We introduce SemiFA-930, a dataset of 930 annotated semiconductor defect images paired with structured FA narratives across nine defect classes, drawn from procedural synthesis, WM-811K, and MixedWM38. Our DINOv2-based classifier achieves 92.1% accuracy on 140 validation images (macro F1 = 0.917), and the full pipeline produces complete FA reports in 48 seconds on an NVIDIA A100-SXM4-40 GB GPU. A GPT-4o judge ablation across four modality conditions demonstrates that multi-modal fusion improves root cause reasoning by +0.86 composite points (1-5 scale) over an image-only baseline, with equipment telemetry as the more load-bearing modality. To our knowledge, SemiFA is the first system to integrate SECS/GEM equipment telemetry into a vision-language model pipeline for autonomous FA report generation.
