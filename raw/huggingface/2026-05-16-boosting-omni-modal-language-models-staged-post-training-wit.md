---
source: farmer/huggingface
farmed: 2026-05-16T03:36:10Z
arxiv_id: "2605.12034"
url: "https://huggingface.co/papers/2605.12034"
arxiv_url: "https://arxiv.org/abs/2605.12034"
date: 2026-05-16
---

# Boosting Omni-Modal Language Models: Staged Post-Training with Visually Debiased Evaluation

Omni-modal language models are intended to jointly understand audio, visual inputs, and language, but benchmark gains can be inflated when visual evidence alone is enough to answer a query. We study whether current omni-modal benchmarks separate visual shortcuts from genuine audio-visual-language evidence integration, and how post-training behaves under a visually debiased evaluation setting. We audit nine omni-modal benchmarks with visual-only probing, remove visually solvable queries, and retain full subsets when filtering is undefined or would make comparisons unstable. This yields OmniClean, a cleaned evaluation view with 8,551 retained queries from 16,968 audited queries. On OmniClean, we evaluate OmniBoost, a three-stage post-training recipe based on Qwen2.5-Omni-3B: mixed bi-modal SFT, mixed-modality RLVR, and SFT on self-distilled data. Balanced bi-modal SFT gives limited and uneven gains, RLVR provides the first broad improvement, and self-distillation reshapes the benchmark profile. After SFT on self-distilled data, the 3B model reaches performance comparable to, and in aggregate slightly above, Qwen3-Omni-30B-A3B-Instruct without using a stronger omni-modal teacher. These results show that omni-modal progress is easier to interpret when evaluation controls visual leakage, and that small omni-modal models can benefit from staged post-training with self-distilled omni-query supervision. Project page: https://cheliu-computation.github.io/omni/
