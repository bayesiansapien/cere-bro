---
source: farmer/huggingface
farmed: 2026-07-24T23:47:01.610703+05:30
arxiv_id: 2607.19604
url: https://huggingface.co/papers/2607.19604
arxiv_url: https://arxiv.org/abs/2607.19604
date: 2026-07-23
---

# Scaling Laws for Hypernetwork-Based Knowledge Injection in Large Language Models

Injecting factual knowledge into large language models (LLMs) reliably and at scale remains an open challenge. Hypernetworks provide a promising solution to large-scale knowledge injection. Although hypernetworks are typically applied for test-time adaptation, we explore their use in train-time knowledge injection, where, given a large corpus of facts, we train a hypernetwork to generate a fixed LoRA adapter that, when inserted into the target model, enable the model to answer questions about those facts. In this work, we investigate whether hypernetworks can be used to perform train-time knowledge injection and how this ability varies with scale. The scaling behavior of hypernetworks remains largely unstudied. Our design decouples the hypernetwork's injection capacity from the target model's general capability, enabling, for the first time, a rigorous study of scaling laws for hypernetwork architectures. We characterize how loss, reasoning accuracy, and out-of-distribution (OOD) generalization vary with hypernetwork depth, width, and target network size. We construct a large-scale dataset, called MegaWikiQA, containing tens of millions of multi-hop question-answer examples across 39 domains constructed from examples in Wikidata5M. Our results reveal: (i) hypernetwork-based injection exhibits broadly predictive power law scaling along all architecture axes; and (ii) hypernetworks are capable of reliable OOD generalization at increasing scales, suggesting that hypernetwork provides a promising alternative to other train-time adaptation methods such as LoRA finetuning and full fine-tuning, exhibiting steeper scaling exponents in all OOD evaluations. Together, these results establish hypernetworks as a principled and scalable substrate for train-time adaptation, and provide the first empirically grounded scaling laws to guide hypernetworks for factual reasoning in large language models.
