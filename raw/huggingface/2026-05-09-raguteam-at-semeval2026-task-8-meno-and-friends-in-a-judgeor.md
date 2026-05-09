---
source: farmer/huggingface
farmed: 2026-05-09T03:37:34Z
arxiv_id: 2605.04523
url: https://huggingface.co/papers/2605.04523
arxiv_url: https://arxiv.org/abs/2605.04523
date: 2026-05-09
---

# RaguTeam at SemEval-2026 Task 8: Meno and Friends in a Judge-Orchestrated LLM Ensemble for Faithful Multi-Turn Response Generation

We present our winning system for Task B (generation with reference passages) in SemEval-2026 Task 8: MTRAGEval. Our method is a heterogeneous ensemble of seven LLMs with two prompting variants, where a GPT-4o-mini judge selects the best candidate per instance. We ranked 1st out of 26 teams, achieving a conditioned harmonic mean of 0.7827 and outperforming the strongest baseline (gpt-oss-120b, 0.6390). Ablations show that diversity in model families, scales, and prompting strategies is essential, with the ensemble consistently beating any single model. We also introduce Meno-Lite-0.1, a 7B domain-adapted model with a strong cost-performance trade-off.
