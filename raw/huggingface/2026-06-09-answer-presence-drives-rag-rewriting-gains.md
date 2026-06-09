---
source: farmer/huggingface
farmed: 2026-06-09T16:28:21
arxiv_id: 2606.05633
url: https://huggingface.co/papers/2606.05633
arxiv_url: https://arxiv.org/abs/2606.05633
date: 2026-06-09
---

# Answer Presence Drives RAG Rewriting Gains

Retrieval-augmented QA pipelines often route retrieved passages through an LLM rewriter before a smaller reader, lifting F1 by tens of points on multi-hop benchmarks; this gain is typically credited to improved evidence quality. We ask whether that lift is causally driven by the gold answer string appearing in the rewritten context rather than by curation per se, using a controlled intervention audit. For each rewritten context we re-run the reader after one of four controlled edits to the compile output: removing the gold answer span, replacing a length-matched random non-answer span (placebo), or injecting the gold into rewrites where it was absent (at the prefix or at a midpoint sentence boundary). Across twelve completed (cell, baseline) intervention runs spanning three reader families (Qwen2.5-7B, Qwen3.5-35B, GLM-4.7), two datasets (HotpotQA, 2WikiMultihopQA), and three compiler arrangements (MA-only, MB-only, MA+verify), removing the gold answer drops reader F1 by 28 to 64 points beyond the length-matched placebo on paired answer-in-compile strata, and prepending the gold into rewrites that lacked it raises F1 by +0.7 to +9.7 points in 10 of 12 (cell, baseline) combinations. A companion five-sentinel audit shows the conventional single-[MASK] probe is itself sentinel-fragile: on 2Wiki it reports a +4.12~F1 ``non-leakage residual'' that flips to -3.33 to -7.81~F1 under four alternative sentinels and fails an equivalence test for three of those four (1/4~pass). We do not propose a new rewriter or mitigation; we release the intervention runner and the sentinel panel so that other rewriter-gain claims can be tested against the same standard.
