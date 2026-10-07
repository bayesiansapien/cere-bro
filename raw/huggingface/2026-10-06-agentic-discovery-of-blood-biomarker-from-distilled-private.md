---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.04749
url: https://huggingface.co/papers/2610.04749
arxiv_url: https://arxiv.org/abs/2610.04749
date: 2026-10-06
---

# Agentic discovery of blood biomarker from distilled private health records

Routine complete blood counts (CBCs) could yield new biomarkers, but the private records needed to evaluate candidates cannot be shared with frontier language model agents that excel at discovery. We distilled the evidence held in the Clalit Health Services panel of over 5.4 million patients into a released scoring tool: for each of 13 immune-mediated diseases, a graph attention network was trained inside the data boundary to predict the case-control AUC of candidate CBC expressions, and only the trained weights were released. The tool grounds an agent's propose-score-refine loop in real-world data without exposing any patient data. In external validation, agent-discovered expressions improved on their literature-seeded starting points by a median of 4.18 AUC percentage points, and across three independent cohorts, reranking the candidates of three frontier research tools improved on their first choices in most comparisons, with gains that varied by cohort. The released scorer supports privacy-preserving biomarker hypothesis generation.
