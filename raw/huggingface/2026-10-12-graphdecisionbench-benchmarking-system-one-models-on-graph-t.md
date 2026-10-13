---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.221213+05:30
arxiv_id: 2610.06354
url: https://huggingface.co/papers/2610.06354
arxiv_url: https://arxiv.org/abs/2610.06354
date: 2026-10-12
---

# GraphDecisionBench: Benchmarking System One Models on Graph Tasks

Large language models (LLMs) are increasingly explored for graph understanding and decision-making, while System One models such as Jev select directly from supplied options. However, the capabilities of System One models on graph-related tasks remain unclear. We introduce GraphDecide, a model-independent benchmark that combines structural task profiles, matched graph-text input contrasts and heuristic-proposal controls to diagnose graph decision performance. We evaluate Jev and related choice-based models alongside language-model baselines, covering fourteen model-interface configurations. Jev's results illustrate the benchmark's central distinctions: accurate adjacency recognition does not guarantee broader structural correctness, joint graph-text input does not consistently improve prediction, and feasible construction does not establish high solution quality. Its task contracts, candidate interfaces and scoring rules support comparison across native selectors and language-model adapters. Code and aggregate results are available at https://github.com/VictorYXL/JevGraphBench.
