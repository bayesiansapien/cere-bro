---
source: farmer/huggingface
farmed: 2026-09-04T08:38:35.484326+00:00
arxiv_id: 2609.04199
url: https://huggingface.co/papers/2609.04199
arxiv_url: https://arxiv.org/abs/2609.04199
date: 2026-09-04
---

# Compile by Training: Turning Natural-Language Specifications into Local Neural Functions

Many recurring text functions are easy to describe but difficult to implement with rules, while calling a large remote model for every input introduces repeated cost, latency, and dependency on a provider. We present compile by training, which turns a natural-language specification into a reusable neural function. At compile time, teacher models generate task-specific examples that are used to train a small adapter for a compact interpreter. The resulting function runs without the teachers and can be stored, versioned, and composed like ordinary software. On FuzzyBench-Hard, a subset on which the Program-as-Weights fast compiler produced no exact matches, compile by training reaches 83.6% semantic accuracy. This higher accuracy comes with a higher compile-time cost: roughly a minute rather than seconds for the fast compiler. We deploy the compiler in a public interactive service and demonstrate compiled functions in a multi-site website helper, a language-controlled 3D avatar, and a bidirectional English-Claudish translator.
