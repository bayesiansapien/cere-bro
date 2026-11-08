---
source: farmer/huggingface
farmed: 2026-11-08T17:18:50.591604+00:00
arxiv_id: 2611.04894
url: https://huggingface.co/papers/2611.04894
arxiv_url: https://arxiv.org/abs/2611.04894
date: 2026-11-07
---

# VisSearch-Bench: Evaluating Long Horizon Visual Search in Multimodal Agents

Multimodal agents use web and image tools to answer questions beyond their internal knowledge. Some search tasks use images mainly to identify an initial entity, then rely on text retrieval. These tasks offer limited insight into how agents connect information across images, objects, and search steps. We therefore focus on visual context management. This involves organizing and using visual information and linking it to other findings during search. Visually intensive tasks require agents to combine object appearance, local details, or spatial relations with external information. We introduce VisSearch-Bench, with 204 human-written tasks across 7 main domains and 25 subdomains. It covers Set-wise Visual Search, Sequential Visual Search, Hybrid Wide-Deep Search, Competitive Visual Disambiguation, and Visual-Structure-Guided Search. Each task provides a reference answer, traceable evidence, and scoring rules. Accuracy measures complete task success, while Process Score measures the correctness and completeness of individual results and subquestion answers. Across 16 multimodal models, the best system fully solves only 26.47% of tasks, even with search tools. These results highlight the challenge of linking visual evidence with search results to produce complete answers.
