---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.02709
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.02709
published: 2026-04-16
authors: Yihong Dong, Jianha Xiao, Xue Jiang
---

# Evaluating the Formal Reasoning Capabilities of Large Language Models through Chomsky Hierarchy

**arXiv:** https://arxiv.org/abs/2604.02709
**Authors:** Yihong Dong, Jianha Xiao, Xue Jiang

## Abstract

arXiv:2604.02709v2 Announce Type: replace-cross  Abstract: The formal reasoning capabilities of LLMs are crucial for advancing automated software engineering. However, existing benchmarks for LLMs lack systematic evaluation based on computation and complexity, leaving a critical gap in understanding their formal reasoning capabilities. Therefore, it is still unknown whether SOTA LLMs can grasp the structured, hierarchical complexity of formal languages as defined by Computation Theory. To address this, we introduce ChomskyBench, a benchmark for systematically evaluating LLMs through the lens of Chomsky Hierarchy. Unlike prior work that uses vectorized classification for neural networks, ChomskyBench is the first to combine full Chomsky Hierarchy coverage, process-trace evaluation via natural language, and deterministic symbolic verifiability. ChomskyBench is composed of a comprehensive suite of language recognition and generation tasks designed to test capabilities at each level. Extensive experiments indicate a clear performance stratification that correlates with the hierarchy's levels of complexity. Our analysis reveals a direct relationship where increasing task difficulty substantially impacts both inference length and performance. Furthermore, we find that while larger models and advanced inference methods offer notable relative gains, they face severe efficiency barriers: achieving practical reliability would require prohibitive computational costs, revealing that current limitations stem from inefficiency rather than absolute capability bounds. A time complexity analysis further indicates that LLMs are significantly less efficient than traditional algorithmic programs for these formal tasks. These results delineate the practical limits of current LLMs, highlight the indispensability of traditional software tools, and provide insights to guide the development of future LLMs with more powerful formal reasoning capabilities.
