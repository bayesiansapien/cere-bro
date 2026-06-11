---
source: farmer/huggingface
farmed: 2026-06-11T08:27:36Z
arxiv_id: 2606.10479
url: https://huggingface.co/papers/2606.10479
arxiv_url: https://arxiv.org/abs/2606.10479
date: 2026-06-11
---

# ComBench: A Benchmark for Rigorous Proof Reasoning and Constructive Realization in Olympiad-Level Combinatorics

Combinatorics is central to Olympiad-level mathematical problem solving, requiring deep discrete reasoning, creative constructions, and rigorous structural insight. Recent evidence suggests that even today's strongest frontier models remain uneven on Olympiad combinatorics, revealing a gap in creative mathematical reasoning. We introduce ComBench, an Olympiad-level combinatorics benchmark for evaluating and diagnosing the combinatorial reasoning capabilities of large language models. ComBench contains 100 human-annotated competition-level problems organized around two complementary settings: analysis-centric problems, which primarily require rigorous mathematical arguments, and construction-centric problems, which require explicit constructions in addition to correctness justifications. The evaluation protocol combines rubric-guided proof grading with deterministic construction verification, exposing cases where proof quality and construction validity diverge. Experiments on frontier open- and closed-source models show that ComBench is far from saturated: the strongest model reaches 65.4% overall Avg. and 75.3% overall Best@4. We further find that Rigorous Proof Reasoning and Constructive Realization are distinct capabilities: Kimi-K2.6 trails GPT-5.5 on analysis-centric proof grading but surpasses it on construction-centric Best@4, while Existence and Construction problems remain consistently hardest across representative frontier models.
