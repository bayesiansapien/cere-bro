---
source: farmer/huggingface
farmed: 2026-07-24T23:47:01.610703+05:30
arxiv_id: 2605.09635
url: https://huggingface.co/papers/2605.09635
arxiv_url: https://arxiv.org/abs/2605.09635
date: 2026-07-24
---

# K12-KGraph: A Curriculum-Aligned Knowledge Graph for Benchmarking and Training Educational LLMs

Large language models are increasingly used in K-12 education, but existing benchmarks mainly test exam question answering rather than understanding how curriculum knowledge is structured and visually presented. We call this capability curriculum cognition. It covers prerequisite chains, concept taxonomies, experiment-concept links, pedagogical sequencing, and visual grounding. We introduce K12-KGraph, a curriculum-aligned knowledge graph extracted from official People's Education Press textbooks in mathematics, physics, chemistry, and biology across primary, middle, and high school. It contains nine node types and fourteen relation types covering curriculum structure and visual grounding. From this graph, we derive K12-Bench, a 23,640-question multi-select benchmark with five task families: Ground, Prereq, Neighbor, Evidence, and Locate. We also build K12-Train, a graph-guided supervised fine-tuning corpus of 7,335 samples, including 2,267 text-only QA pairs and 5,068 multimodal VQA pairs. On K12-Bench, Gemini-3-Flash achieves only 57 percent exact match and Gemma-4-31B-IT reaches 46 percent, with Prereq and Neighbor being the hardest tasks. Our training experiments show that domain-specific supervision can reduce this gap. Under a matched 2,300-sample budget, K12-Train-Text consistently outperforms equally sized subsets of eight mainstream instruction-tuning corpora on GaokaoBench and EduEval. For vision-language models, K12-Train-Full achieves the best overall results on Gaokao-MM, MDK12-medium, and K12Vista among all compared training configurations, despite using fewer samples than the full DataFlow and WizardLM baselines. It also surpasses both text-only and multimodal-only variants, showing that textual and visual supervision are complementary. We release the graph, benchmark, training data, and complete construction pipeline.
