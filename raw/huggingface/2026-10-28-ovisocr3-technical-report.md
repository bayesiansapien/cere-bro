---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.995618+05:30
arxiv_id: 2610.33066
url: https://huggingface.co/papers/2610.33066
arxiv_url: https://arxiv.org/abs/2610.33066
date: 2026-10-28
---

# OvisOCR3 Technical Report

We introduce OvisOCR3, a 0.8B model for a broad range of OCR-related tasks. OvisOCR3 unifies document parsing, general OCR, key information extraction (KIE), document figure captioning, and cross-page table reconstruction in a single model. We train the model on real and synthetic data through continued pretraining and use domain-balanced mid-training to balance supervision across tasks with different data volumes and response lengths. Multi-teacher on-policy distillation transfers expertise from five domain-specific 4B teachers into the shared model, followed by mixed-task reinforcement learning with domain-specific rewards. We compare OvisOCR3 with general-purpose vision-language models and specialized OCR models on public and in-house benchmarks covering all five task families. In these comparisons, it achieves an overall score of 96.74 on OmniDocBench v1.6 and the highest overall scores on PureDocBench, Real5-OmniDocBench, and MDPBench. On OCRBench v2, it ranks first, scoring 65.9 and 61.3 on the English and Chinese splits, respectively. It also outperforms the baselines on OCRBench and all four KIE benchmarks. On DocFigCapBench, it achieves the highest localization F1 and a caption score close to that of Qwen3.8-Max. For cross-page tables, it leads in Relation F1 on CrossTabBench and truncated-table TEDS on MPDocBench-Parse. These results demonstrate that a compact 0.8B model can achieve strong performance across diverse OCR-related tasks. OvisOCR3 is available at https://huggingface.co/ATH-MaaS/OvisOCR3.
