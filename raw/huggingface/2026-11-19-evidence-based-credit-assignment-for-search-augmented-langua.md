---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.147323+00:00
arxiv_id: 2611.23824
url: https://huggingface.co/papers/2611.23824
arxiv_url: https://arxiv.org/abs/2611.23824
date: 2026-11-19
---

# Evidence-Based Credit Assignment for Search-Augmented Language Models

Reinforcement learning from terminal answer rewards enables search-augmented language models to interleave reasoning and retrieval without step-level annotations, yet outcome supervision assigns identical credit to every search in a trajectory regardless of whether it retrieved useful information. This limitation is especially severe when all sampled rollouts for a question fail, collapsing group-centered outcome advantages to zero even when trajectories gather markedly different evidence. We present Evidence-based Credit Assignment (ECA), which augments terminal outcome rewards with a training-only auxiliary signal measuring how retrieved documents improve the likelihood of a reference answer. Rather than scoring the full dialogue prefix, ECA queries a frozen snapshot of the current policy under an evidence-only prompt containing solely the question and the deduplicated documents observed so far, isolating the utility of retrieved passages from surface variations in generated thoughts or search queries. Within this framework, we compare two return formulations, ECA-Step (which accumulates step-clipped potential increments) and ECA-Horizon (which preserves the telescoping horizon gain in potential), paired with cross-fold group normalization, novelty gating, and search-local token assignment. Across seven Search QA benchmarks, ECA-Horizon improves strict macro exact match over an outcome-only GRPO baseline by 1.03 and 4.80 percentage points on Qwen2.5-3B- and 7B-Instruct, respectively, outperforming both RLOO and GiGPO. Zero-shot evaluation on MultiHop-RAG further demonstrates strong transfer to multi-hop inference queries.
