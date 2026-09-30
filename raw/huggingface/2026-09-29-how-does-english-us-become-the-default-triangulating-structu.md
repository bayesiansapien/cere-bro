---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.936963+00:00
arxiv_id: 2604.04204
url: https://huggingface.co/papers/2604.04204
arxiv_url: https://arxiv.org/abs/2604.04204
date: 2026-09-29
---

# How Does "English (US)" Become the Default? Triangulating Structural Bias Towards American English Across the LLM Pipeline

Large language models (LLMs) are increasingly embedded in educational, professional, and public infrastructure, yet widely used platforms expose "English (US)" as a primary English setting despite the global diversity of English. We ask: How does "English (US)" become the default? We study this question as structural bias, examining how geopolitical histories of data curation, digital dominance, and linguistic standardization intersect with the LLM development pipeline. Using British English as a controlled reference, we construct a curated resource of 1,813 matched American English (AmE)--British English (BrE) variants and introduce DiAlign, a dynamic, training-free method for estimating regional alignment from distributional evidence. We triangulate the AmE preference across data exposure --> representation --> generation, jointly examining pretraining and post-training data, tokenizer behavior and provenance, model prediction cost, and generated language across developer countries, prompt conditions, domains and sources, linguistic categories, and registers. AmE is consistently favored across all six audited pretraining corpora and 21 post-training datasets, is generally represented more compactly by tokenizers, and receives lower prediction cost. It also remains the dominant generation default under neutral English prompting; British-English prompting shifts this preference toward BrE but does not consistently eliminate the AmE default. To our knowledge, this is the first rigorous pipeline-wide study of structural bias across major phases of LLM development. Our findings show that contemporary LLMs privilege AmE as the de facto norm, raising concerns about linguistic homogenization, epistemic injustice, and inequity in global AI deployment, while providing a rigorous basis for targeted component-level intervention.
