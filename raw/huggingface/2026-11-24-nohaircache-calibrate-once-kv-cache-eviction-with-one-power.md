---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.929547+00:00
arxiv_id: 2611.29006
url: https://huggingface.co/papers/2611.29006
arxiv_url: https://arxiv.org/abs/2611.29006
date: 2026-11-24
---

# NoHairCache: Calibrate-Once KV Cache Eviction with One Power-Law Exponent

The decay exponent α in KV-cache eviction is an intrinsic property of the model: calibrated once on a single corpus, it transfers directly across domains. Attention-based accumulation (H2O) and recency-based sliding windows (StreamingLLM) are two dominant eviction frameworks, often treated as unrelated, but we show that they are the two endpoints of a single power-law family: by scoring each token as s_i = A_i cdot (t-i)^{-α}, where A_i is cumulative attention and α controls the age penalty, H2O and StreamingLLM correspond to α=0 and αtoinfty, respectively (with StreamingLLM additionally hard-coding an attention-sink patch).
  The no-hair mechanism of xiang2026nohair bounds the admissible range of α, and the measured exponents agree: calibrating once on WikiText yields [0.556, 0.822] for a representative model (Qwen2.5-1.5B-Instruct). The per-model ranges are consistent across five models (410M--1.5B) and independently match the optimal regions from perplexity sweeps.
  NoHairCache achieves the lowest perplexity across three datasets (WikiText, PG19, and arXiv) without per-dataset tuning, outperforming both H2O and StreamingLLM (p < 0.05 on all three datasets, with 0.06--0.10 PPL gains over StreamingLLM at budget 512). On downstream four-way multiple-choice QA, it matches or outperforms StreamingLLM across all nine (task, budget) cells, retaining 98.2% of full-cache accuracy on NarrativeQA at 25% retention versus 91.1% for StreamingLLM; per-cell McNemar tests are not significant, so QA is corroborating only. We release our calibration script and drop-in scorer upon publication.
