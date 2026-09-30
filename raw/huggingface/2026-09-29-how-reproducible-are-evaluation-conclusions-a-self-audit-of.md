---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.936817+00:00
arxiv_id: 2609.30074
url: https://huggingface.co/papers/2609.30074
arxiv_url: https://arxiv.org/abs/2609.30074
date: 2026-09-29
---

# How Reproducible Are Evaluation Conclusions? A Self-Audit of LLM-Inferred Prompt Structure

Evaluations of LLM systems routinely average over small prompt sets and report models as a ranked table. We ask how much confidence such a table deserves, using LLM-based prompt-structure inference as the case study: eight open model variants across five families and 8B to 675B parameters, caching disabled, 293 raw intermediate representations persisted. The measured phenomenon is unstable to begin with. Identical calls do not reliably recover identical structure, with mean node-set Jaccard from 0.39 to 0.96 and 72% of prompt-model cells never node-set-perfect. Auditing the evaluation weakens its conclusions further, and this is our main contribution. Under a joint cluster bootstrap over prompts, only the bottom of the ranking is firm: the two least reproducible models hold rank in 99% and 86% of replicates, the middle four in 27% to 48%, and the top two in 68% each, so the table identifies the worst model reliably but does not reliably identify the best. Two equally defensible rules for merging repeated campaigns change four of eight rows and move the study-wide headline by 7 percentage points. Checking the inferred structure against ground-truth annotations shows reproducibility cannot be read as accuracy. And four of the eight endpoints were withdrawn within ten weeks of measurement, so the study as specified can no longer be run. Small-sample LLM evaluations can therefore look far more definitive than their evidence supports. We recommend reporting rank stability, per-cell provenance, executed sensitivity comparisons, raw per-run outputs, and a measurement date alongside any ranking.
