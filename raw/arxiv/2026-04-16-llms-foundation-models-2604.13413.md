---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13413
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13413
published: 2026-04-16
authors: Zhengyu Fang, Zhimeng Jiang, Huiyuan Chen
---

# Dataset-Level Metrics Attenuate Non-Determinism: A Fine-Grained Non-Determinism Evaluation in Diffusion Language Models

**arXiv:** https://arxiv.org/abs/2604.13413
**Authors:** Zhengyu Fang, Zhimeng Jiang, Huiyuan Chen

## Abstract

arXiv:2604.13413v1 Announce Type: new  Abstract: Diffusion language models (DLMs) have emerged as a promising paradigm for large language models (LLMs), yet the non-deterministic behavior of DLMs remains poorly understood. The existing non-determinism evaluations for LLMs predominantly rely on dataset-level metrics under fixed inference configurations, providing limited insight into how model behavior varies across runs and evaluation conditions. In this work, we show that dataset-level metrics systematically attenuate non-determinism in diffusion language models by aggregating sample-level prediction quality across different runs. As a result, configurations with similar aggregate performance can exhibit substantially different behaviors on individual inputs, leaving fine-grained instability and distinct error patterns uncharacterized. To address this limitation, we conduct a fine-grained evaluation of non-determinism based on sample-level prediction differences across a range of model-related factors-including guidance scale, diffusion steps, and Monte Carlo sampling-as well as system-related factors such as batch size, hardware, and numerical precision. Our analysis reveals that non-determinism in DLMs is pervasive and structured, with code generation exhibiting markedly higher sensitivity to factor-level choices than question answering. To attribute sources of non-determinism evaluation, we introduce Factor Variance Attribution (FVA), a cross-factor analysis metric that decomposes observed non-determinism into variance attributable to different evaluation factor settings. Our findings highlight the need for fine-grained, factor-aware evaluation to enable reliable non-determinism assessment of diffusion language models.
