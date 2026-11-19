---
source: farmer/huggingface
farmed: 2026-11-19T11:13:13+05:30
arxiv_id: 2611.21644
url: https://huggingface.co/papers/2611.21644
arxiv_url: https://arxiv.org/abs/2611.21644
date: 2026-11-18
---

# MInfoVisQA: A Multilingual Benchmark for Information-Rich Visual Question Answering

Multimodal large language models (MLLMs) excel in vision-language tasks; yet, whether they maintain consistent understanding of information-rich visuals (InfoVis) when the surface language changes remains unclear. To quantify this capability, we introduce MInfoVisQA, a parallel benchmark with 8,960 QA configurations derived from 128 seed instances across 24 languages. We construct seed-matched, language-parallel visuals and QA pairs by disentangling numerical-structural data from text and programmatically synchronizing translated labels. We evaluate 25 MLLMs under two settings: Language-Aligned QA (LQA, matching visual-text languages) and Cross-Language QA (XQA, fixed QA language with varying visual languages). The results show that aggregate accuracy masks substantial robustness gaps: two models with comparable mean LQA accuracy (80.4\%) exhibit performance spreads of 7.8 and 20.3 percentage points across languages. Moreover, all 25 models score lower with non-English visuals under fixed English QA, underscoring the need for cross-language sensitivity metrics.
