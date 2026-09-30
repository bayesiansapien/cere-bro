---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.933409+00:00
arxiv_id: 2609.34479
url: https://huggingface.co/papers/2609.34479
arxiv_url: https://arxiv.org/abs/2609.34479
date: 2026-09-29
---

# SentZero: An Enhanced Sentence-Centric Vision-Language Pretraining for Multi-Task Zero-Shot Chest X-Ray Analysis

Vision-language (VL) pretraining using paired chest X-ray (CXR) images and radiology reports has shown strong potential for medical image understanding. However, existing methods often remain dependent on task-specific finetuning because radiology reports are lengthy, clinically dense, and difficult to align with simple zero-shot prompts. Recent sentence-level approaches partially address this limitation using clinical phrases extracted by large language models (LLMs), but they largely overlook the intrinsic characteristics of radiology discourse. In particular, limited positive-pair diversity constrains further gains, while clinically equivalent sentences frequently recur across patients, creating false negatives in contrastive learning. To address these issues, we propose SentZero, an enhanced sentence-centric VL pretraining framework for zero-shot, multi-task CXR analysis. SentZero introduces LLM-based abstract-level sentence structuring and mapping to expand positive-pair diversity, together with an additional loss term to mitigate false negatives. We further introduce sentence-conditioned residual modulation of visual embeddings, enabling visual features to adapt to the semantic characteristics of each input sentence. Across diverse downstream tasks and datasets, SentZero improves zero-shot generalization and outperforms prior multi-task zero-shot methods.
