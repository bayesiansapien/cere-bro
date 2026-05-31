---
source: farmer/huggingface
farmed: 2026-05-31T09:25:04Z
arxiv_id: 2605.29648
url: https://huggingface.co/papers/2605.29648
arxiv_url: https://arxiv.org/abs/2605.29648
date: 2026-05-31
---

# Verifiable Rewards Beyond Math and Code: Lightweight Corpus-Grounded Process Supervision for Factual Question Answering

Applying reinforcement learning to improve factual accuracy in knowledge-intensive question answering faces a reward design dilemma. Response-level rewards provide only coarse supervision and cannot distinguish correct from incorrect statements within a reasoning trace. Sentence-level alternatives offer finer-grained feedback, but typically rely on NLI verifiers, LLM judges, or knowledge-verification pipelines that are expensive to deploy at RL scale and often unreliable for rare-entity facts, where accurate reward signals are especially important. We propose CorVer (Corpus Verify), a lightweight, plug-in-ready process reward that replaces neural verifiers with a corpus-grounded signal derived from Wikipedia co-occurrence statistics. CorVer assigns sentence-level credit and maps it to token-level advantages via a simple alignment, requiring only a 0.5B extractor and a single corpus lookup per sentence. Across 30 (model, benchmark) cells spanning six instruction-tuned models (3B to 14B) and five QA benchmarks, CorVer improves over the raw baseline for every cell, with an average TriviaQA gain of +4.1 pp. It also outperforms four neural-verifier baselines in 18 of 20 cells under their feasible configurations, while training 4.8 to 8.4x faster.
