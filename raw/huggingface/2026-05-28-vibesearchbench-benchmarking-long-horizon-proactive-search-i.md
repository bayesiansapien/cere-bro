---
source: farmer/huggingface
farmed: 2026-05-28T03:40:35Z
arxiv_id: 2605.27882
url: https://huggingface.co/papers/2605.27882
arxiv_url: https://arxiv.org/abs/2605.27882
date: 2026-05-28
---

# VibeSearchBench: Benchmarking Long-horizon Proactive Search in the Wild

LLM-based agents score well on search benchmarks, yet real users consistently find results unsatisfying, revealing a persistent evaluation-experience gap. We attribute this gap to existing benchmarks' reliance on over-specified queries, single-turn interactions, and fixed-schema evaluation, none of which reflect real search behavior where users and agents collaboratively refine vague intent through multi-turn dialogue. We term this paradigm VibeSearch and introduce VibeSearchBench, a benchmark comprising 200 manually curated bilingual (Chinese and English) tasks across 20 domains, split into VibeSearch-Pro (professional) and VibeSearch-Daily (daily-life) subsets. Each task pairs a user persona with a schema-free ground-truth knowledge graph, and is evaluated through a progressive-disclosure user simulator and a graph-matching evaluation framework. We benchmark seven frontier models under both the ReAct framework and the OpenClaw agent harness. Results show that all models remain substantially inadequate for VibeSearch (best F1: 30.30), highlighting the need for fundamental advances in long-context reasoning, proactive intent elicitation, and structured knowledge construction.
