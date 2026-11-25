---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.926184+00:00
arxiv_id: 2611.27319
url: https://huggingface.co/papers/2611.27319
arxiv_url: https://arxiv.org/abs/2611.27319
date: 2026-11-24
---

# SAVIOR: Sample-efficient Adaptation of Vision-Language Models for OCR Representation

Optical Character Recognition (OCR) pipelines and vision-language models exhibit high accuracy on standard OCR and document-understanding benchmarks, yet they systematically underperform on document patterns that are operationally critical in financial workflows. These patterns include vertical or rotated text, logo-embedded vendor names, fine-print regulatory clauses, degraded scans, and complex multi-column layouts. While underrepresented in public datasets, they constitute a substantial portion of real-world failure cases. We introduce SAVIOR, a sample-efficient data curation methodology that targets such high-impact failure scenarios to adapt vision-language models for robust financial OCR. We further propose PaIRS, a structure-aware evaluation metric that measures layout fidelity by comparing pairwise spatial relationships between tokens. Fine-tuning Qwen2.5-VL-Instruct with SAVIOR-Train achieves a word recall of 0.93. When the resulting layout-aware OCR output is used as context for document question answering, it attains an F1 score of 0.89, outperforming both open- and closed-source models such as GPT-4o, Mistral-OCR, PaddleOCR-VL, and DeepSeek-OCR.
