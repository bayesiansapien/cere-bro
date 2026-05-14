---
source: farmer/huggingface
farmed: 2026-05-14T10:39:11Z
arxiv_id: 2605.10977
url: https://huggingface.co/papers/2605.10977
arxiv_url: https://arxiv.org/abs/2605.10977
date: 2026-05-13
---

# PASA: A Principled Embedding-Space Watermarking Approach for LLM-Generated Text under Semantic-Invariant Attacks

Watermarking for large language models (LLMs) is a promising approach for detecting LLM-generated text and enabling responsible deployment. However, existing watermarking methods are often vulnerable to semantic-invariant attacks, such as paraphrasing. We propose PASA, a principled, robust, and distortion-free watermarking algorithm that embeds and detects a watermark at the semantic level. PASA operates on semantic clusters in a latent embedding space and constructs a distributional dependency between token and auxiliary sequences via shared randomness synchronized by a secret key and semantic history. This design is grounded in our theoretical framework that characterizes a jointly optimal embedding-detection pair, achieving the fundamental trade-offs among detection accuracy, robustness, and distortion. Evaluations across multiple LLMs and semantic-invariant attacks demonstrate that PASA remains robust even under strong paraphrasing attacks while preserving high text quality, outperforming standard vocabulary-space baselines. Ablation studies further validate the effectiveness of our hyperparameter choices. Webpage: https://ai-kunkun.github.io/PASA_page/.
