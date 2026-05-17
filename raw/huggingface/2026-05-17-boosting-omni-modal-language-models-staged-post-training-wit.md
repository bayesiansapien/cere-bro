---
source: farmer/huggingface
farmed: 2026-05-17T00:00:00Z
arxiv_id: "2605.12034"
url: "https://huggingface.co/papers/2605.12034"
arxiv_url: "https://arxiv.org/abs/2605.12034"
date: 2026-05-17
---

# Boosting Omni-Modal Language Models: Staged Post-Training with Visually Debiased Evaluation

Omni-modal language models are designed to jointly understand audio, visual inputs, and language, yet their benchmark gains do not necessarily reflect genuine omni-modal understanding: when visual evidence alone is sufficient, improvements can be driven by visual shortcuts rather than better omni-modal integration. We ask whether existing omni-modal benchmarks can separate such shortcuts from audio-visual-language evidence integration, and how post-training behaves under a visually debiased evaluation setting. To this end, we audit nine omni benchmarks with visual-only probing, remove visually solvable queries, and retain full subsets only when filtering is undefined or would destabilize score comparisons. This protocol audits 16,968 queries and yields OmniClean, a visually debiased evaluation view with 8,551 retained queries. On this testbed, we study OmniBoost, a three-stage post-training recipe based on Qwen2.5-Omni-3B: mixed bi-modal SFT, mixed-modality RLVR, and SFT on self-distilled data. After SFT on self-distilled data, the 3B model becomes comparable to larger open-source references and slightly exceeds Qwen3-Omni-30B-A3B-Instruct under OmniClean aggregate summaries.
