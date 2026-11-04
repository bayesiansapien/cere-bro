---
source: farmer/huggingface
farmed: 2026-11-04T11:17:37.426675+00:00
arxiv_id: 2610.41296
url: https://huggingface.co/papers/2610.41296
arxiv_url: https://arxiv.org/abs/2610.41296
date: 2026-11-03
---

# Self-Improvement with Auxiliary Rewards: Learning from Verified Traces and Evaluating Transfer

Answer-level rewards cannot distinguish reasoning traces with equally correct outcomes. We study whether auxiliary trajectory preferences improve small-language-model self-improvement and transfer under limited supervision. We compare confidence-based (SC) and entropy-based metrics (UID-Conj.), which combines global entropy variation and local smoothness, through online reward augmentation and offline training on correct responses. Online experiments adapt Qwen3-1.7B on 30 AIME problems without reference answers; offline experiments use historical AIME problems. UID-Conj. improves the online macro-average across the adaptation benchmark and three transfer benchmarks by 2.08 percentage points over unmodified TTRL. The strongest evidence comes from offline weighted SFT: UID-Conj. exceeds uniform weighting on the same response pool by 1.93 points, with a paired prompt-bootstrap 95\% CI of [0.44, 3.44]. Benefits are task-dependent: SC rewards judged trace quality and instruction following, while UID-Conj. rewards yield stronger training outcomes in several settings. We find that auxiliary preferences can expose learning value among equally correct traces not captured during inference time, motivating their evaluation through downstream gains.
