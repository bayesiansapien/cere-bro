---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.800462+00:00
arxiv_id: 2610.01352
url: https://huggingface.co/papers/2610.01352
arxiv_url: https://arxiv.org/abs/2610.01352
date: 2026-10-26
---

# MMVistaReason: Toward Open-Data and Post-Training Recipes for Multimodal Reasoning

Open multimodal reasoning models have benefited from large-scale reasoning supervision, yet reliable post-training remains challenging due to uneven data quality, inefficient supervision construction, imbalanced difficulty, and cross-domain interference. We introduce MMVistaReason (MVR), an open-data post-training recipe with three components: (1) broader capability coverage across complementary Analytical and Real-World reasoning groups, emphasizing structured reasoning versus visual perception and spatial grounding; (2) efficient SFT and RL data construction, standardizing heterogeneous open data through staged cleaning and annotation, combining difficulty-aware cascaded teacher distillation with answer-likelihood-based trajectory selection to construct MVR-SFT-528K, and applying scale-specific frontier filtering for MVR-RL-63K; and (3) specialize-then-integrate training, which trains complementary RL experts and consolidates their capabilities through multi-teacher on-policy distillation (MOPD). Our analyses reveal a capacity-dependent interaction between supervision difficulty, trajectory quality, and model capacity: smaller students benefit more from selected supervision, while larger students are robust to trajectory variation and mixed-domain interference. Mixed-domain RL introduces benchmark-level negative transfer, whereas MOPD provides consistent capability integration, with the preferred KL direction varying across model scales. Across 15 multimodal benchmarks, MVR-4B achieves an average score of 72.8, outperforming Qwen3.5-9B (Instruct) and MMFineReason-8B while using about 70% fewer samples than MMFineReason. Scaling to 9B improves the average to 74.4, surpassing Qwen3.5-35B-A3B (Instruct). Overall, MMVistaReason demonstrates that systematic open-data construction and capacity-aware post-training provide a practical and scalable path toward reliable multimodal reasoning.
