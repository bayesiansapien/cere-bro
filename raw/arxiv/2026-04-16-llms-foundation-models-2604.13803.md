---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13803
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13803
published: 2026-04-16
authors: Arya Shah, Vaibhav Tripathi, Mayank Singh
---

# Gaslight, Gatekeep, V1-V3: Early Visual Cortex Alignment Shields Vision-Language Models from Sycophantic Manipulation

**arXiv:** https://arxiv.org/abs/2604.13803
**Authors:** Arya Shah, Vaibhav Tripathi, Mayank Singh

## Abstract

arXiv:2604.13803v1 Announce Type: cross  Abstract: Vision-language models are increasingly deployed in high-stakes settings, yet their susceptibility to sycophantic manipulation remains poorly understood, particularly in relation to how these models represent visual information internally. Whether models whose visual representations more closely mirror human neural processing are also more resistant to adversarial pressure is an open question with implications for both neuroscience and AI safety. We investigate this question by evaluating 12 open-weight vision-language models spanning 6 architecture families and a 40$\times$ parameter range (256M--10B) along two axes: brain alignment, measured by predicting fMRI responses from the Natural Scenes Dataset across 8 human subjects and 6 visual cortex regions of interest, and sycophancy, measured through 76,800 two-turn gaslighting prompts spanning 5 categories and 10 difficulty levels. Region-of-interest analysis reveals that alignment specifically in early visual cortex (V1--V3) is a reliable negative predictor of sycophancy ($r = -0.441$, BCa 95\% CI $[-0.740, -0.031]$), with all 12 leave-one-out correlations negative and the strongest effect for existence denial attacks ($r = -0.597$, $p = 0.040$). This anatomically specific relationship is absent in higher-order category-selective regions, suggesting that faithful low-level visual encoding provides a measurable anchor against adversarial linguistic override in vision-language models. We release our code on \href{https://github.com/aryashah2k/Gaslight-Gatekeep-Sycophantic-Manipulation}{GitHub} and dataset on \href{https://huggingface.co/datasets/aryashah00/Gaslight-Gatekeep-V1-V3}{Hugging Face}
