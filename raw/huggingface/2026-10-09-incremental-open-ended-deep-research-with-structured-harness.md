---
source: farmer/huggingface
farmed: 2026-10-10T05:09:51.417903+00:00
arxiv_id: 2610.11566
url: https://huggingface.co/papers/2610.11566
arxiv_url: https://arxiv.org/abs/2610.11566
date: 2026-10-09
---

# Incremental Open-Ended Deep Research with Structured Harness

Existing Open-Ended Deep Research (OEDR) systems primarily generate reports from scratch, making them inefficient for scenarios where research reports need to be continuously maintained as new information emerges. We introduce Incremental Open-Ended Deep Research (Incremental-OEDR), a research setting that treats a report as an evolving research state and incrementally updates it by preserving valid knowledge, revising outdated or incomplete content, and incorporating newly available information. To support this setting, we propose Structured Harness, which represents reports as structured collections of outlines, sections, and supporting evidence, and provides structured retrieval, a persistent structured evidence pool, and structured generation for selective report updating and evidence reuse. We further establish a temporal evaluation framework spanning ten years, with Single-Step Task and Long-Chain Task to evaluate incremental updates over both individual transitions and long-term update chains. Extensive Experiments on DeepResearch Bench and DeepConsult under both the Open-source Configuration (OC) and Proprietary Configuration (PC) show that Incremental-OEDR maintains competitive report quality while substantially improving report continuity and reducing research costs. As shown in Figure~fig:profile, it achieves up to 0.51 higher content-level ROUGE-L F1, 0.63 higher outline-level EM F1, 33\% lower token consumption, and 61\% fewer search calls than OEDR on DeepResearch Bench. For more details, please refer to our project page: https://ioedr-project.github.io/.
