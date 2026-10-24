---
source: farmer/huggingface
farmed: 2026-10-24T12:49:20.885661+00:00
arxiv_id: 2610.31198
url: https://huggingface.co/papers/2610.31198
arxiv_url: https://arxiv.org/abs/2610.31198
date: 2026-10-23
---

# Different Tasks, Different Timesteps: Temporal Task-Aware Quantization for Diffusion Language Models

Diffusion Language Models (DLMs) introduce unique quantization challenges due to their iterative denoising process. In this work, we reveal that quantization sensitivity is both taskand time-dependent, with different downstream tasks exhibiting distinct precision requirements across denoising steps. We further show that these patterns can be predicted without groundtruth labels or task-specific evaluation metrics. Building on these findings, we introduce T 2Quant, a task and time-aware mixedprecision quantization framework that uses a label-free sensitivity signal to optimally allocate activation precision across denoising steps under a fixed bit-width budget. Extensive experiments across three DLMs and six benchmarks demonstrate that T 2Quant consistently improves the average accuracy of existing quantization methods, achieving gains of up to 6.7 percentage points under the same budget.
