---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2603.28554
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2603.28554
published: 2026-04-16
authors: Athos Georgiou
---

# Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model

**arXiv:** https://arxiv.org/abs/2603.28554
**Authors:** Athos Georgiou

## Abstract

arXiv:2603.28554v2 Announce Type: replace-cross  Abstract: Visual document understanding typically requires separate retrieval and generation models, doubling memory and system complexity. We present Hydra, a dual-head approach that provides both ColBERT-style late-interaction retrieval and autoregressive generation from a single vision-language model (VLM). A single LoRA adapter, trained only for retrieval, is toggled at inference: enabling it produces multi-vector embeddings; disabling it recovers the base model's generation quality -- byte-identical outputs in 100% of 10,500 greedy and stochastic samples, with max delta-ANLS = 0.0044 across 15,301 samples on four VQA benchmarks (three informative; ChartQA is near-zero for both models under greedy decoding) when compared against an independent base-model pipeline. We identify three engineering requirements (attention-mode restoration, lm_head preservation, KV-cache-aware decoding) whose omission silently breaks generation despite correct weight recovery. On ViDoRe V1, Hydra (4B) is within 1 percentage point of a controlled single-head baseline in a single training run, with higher aggregate scores on V2 and V3 that are concentrated on a subset of tasks; multi-seed experiments are needed to confirm these trends. The single-model design cuts peak GPU memory from 17.9 GB (two-model baseline) to 9.2 GB -- a 48% reduction, though adapter switching introduces throughput overhead under concurrent serving loads. An ablation shows that GritLM-style joint training provides no benefit within the LoRA-based (r=16) training regime. A proof-of-concept extension to Qwen2.5-Omni-3B demonstrates that the mechanism generalizes to audio retrieval and video embedding, with speech generation.
