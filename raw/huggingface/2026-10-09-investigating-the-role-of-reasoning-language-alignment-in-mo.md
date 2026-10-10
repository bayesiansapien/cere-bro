---
source: farmer/huggingface
farmed: 2026-10-10T05:09:51.419008+00:00
arxiv_id: 2610.03136
url: https://huggingface.co/papers/2610.03136
arxiv_url: https://arxiv.org/abs/2610.03136
date: 2026-10-09
---

# Investigating the Role of Reasoning-Language Alignment in Monolingual Retrieval-Augmented Generation

Reasoning traces improve large language models (LLMs), but current models are trained to reason mostly in English. It has been shown that forcing a model to reason in another language degrades accuracy, even when the reasoning language matches the language of the prompt -- but only for a setting where the model reasons over a short prompt. Here, we ask whether the same holds for retrieval-augmented generation (RAG), where the model must read and integrate a large amount of retrieved evidence in the target language. To study this, we build a fully monolingual German RAG question-answering testbed over the fictional world of the tabletop role-playing game The Dark Eye, a domain that is richly documented in German but too niche for the model to answer from memory, so that it has to rely on retrieval. Varying the forced reasoning language of an agentic RAG system on this testbed, we find that aligning the reasoning language with the language of the query and the retrieved documents helps. Forced German reasoning outperforms forced French, although the model benchmarks higher in French, so the benefit comes from alignment and not from language proficiency. The advantage grows when the retrieved context is richer and structure-aware. However, forced German only reaches the level of the model's native, unconstrained English reasoning without surpassing it, showing that native multilingual reasoning is needed. We publicly release the testbed and QA benchmark.
