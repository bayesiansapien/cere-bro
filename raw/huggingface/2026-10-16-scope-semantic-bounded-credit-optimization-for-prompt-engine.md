---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.22264
url: https://huggingface.co/papers/2610.22264
arxiv_url: https://arxiv.org/abs/2610.22264
date: 2026-10-16
---

# SCOPE: Semantic Bounded Credit Optimization for Prompt Engineering in Text-to-image Generation

Reinforcement learning (RL) enables language models to improve text-to-image (T2I) generation by rewriting prompts for a frozen image generator. Existing methods typically apply a single signal derived from the image to individual subword tokens, although objects, counts, attributes, and relations form coherent semantic spans. We propose SCOPE, an objective based on Group Relative Policy Optimization (GRPO) that aligns update weighting with this structure. The rewriter jointly generates an enhanced prompt and its semantic partition. SCOPE pools shifts in policy log probabilities within each span to derive a shared coefficient for its token losses while retaining a single advantage for each completion. It requires neither separate span rewards nor additional image renders. Across Qwen-Image, SD3, and FLUX.1-dev, SCOPE achieves average relative gains over vanilla GRPO of 9.48% on GeneVal and 7.62% on T2I-CompBench. Ablation studies show that both semantic boundaries and pooling within spans contribute to these gains, supporting semantic structure as a practical inductive bias for prompt engineering with RL.
