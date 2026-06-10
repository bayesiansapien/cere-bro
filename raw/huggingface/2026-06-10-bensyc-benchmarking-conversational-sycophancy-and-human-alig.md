---
source: farmer/huggingface
farmed: 2026-06-10T06:28:48Z
arxiv_id: 2606.10061
url: https://huggingface.co/papers/2606.10061
arxiv_url: https://arxiv.org/abs/2606.10061
date: 2026-06-10
---

# BenSyc: Benchmarking Conversational Sycophancy and Human Alignment in LLMs for Bengali Contexts

Large language models (LLMs) increasingly participate in emotionally sensitive social conversations, where responses may shift from balanced support toward excessive validation or escalatory alignment. Existing sycophancy research primarily focuses on factual agreement and instruction-following settings, leaving culturally grounded conversational sycophancy underexplored. We introduce BenSyc, the first benchmark for studying conversational sycophancy in Bengali social contexts. Starting from 11,840 Reddit posts and 170k comments collected from communities across Bangladesh and West Bengal, we construct a human-validated benchmark with binary labels and a fine-grained five-level taxonomy spanning Invalidation, Neutral, Support, Validation, and Escalation. We evaluate more than 15 open and proprietary LLMs on conversational alignment classification and response generation tasks. Results show that distinguishing empathetic support from reinforcement-oriented validation remains challenging even for frontier instruction-tuned models: the best system achieves only 61.8 Macro-F1 on binary detection and 61.7 Macro-F1 on five-class classification. In generation settings, several models frequently produce strongly validating or escalatory responses in emotionally charged situations. Our findings highlight substantial variation across model families and conversational behaviors, underscoring the importance of culturally grounded multilingual benchmarks for evaluating socially aligned conversational AI systems.
