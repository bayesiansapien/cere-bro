---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.218389+05:30
arxiv_id: 2610.12570
url: https://huggingface.co/papers/2610.12570
arxiv_url: https://arxiv.org/abs/2610.12570
date: 2026-10-12
---

# Contextual Correction of Parallel Draftsfor Speculative Decoding

Speculative decoding accelerates large language model inference by using a lightweight drafter to propose multiple tokens that are subsequently verified in parallel by the target model. Recent diffusion-based drafters make this paradigm particularly attractive: deep attention-based neural backbones provide strong predictions, while drafting multiple future positions in parallel avoids the sequential cost of autoregressive generation. This parallelism, however, comes at a cost. Tokens within a draft block are predicted without access to the realized identities of preceding draft tokens, removing intra-block dependencies that would naturally be available under autoregressive generation. We introduce DCOCO (DFlash Contextual Corrector), a lightweight mechanism that restores these dependencies while preserving parallel drafting. Rather than committing to each position's top prediction, DCOCO retains multiple candidate tokens and evaluates their contextual compatibility across adjacent draft positions in parallel, enabling contextually informed token selection at low additional cost. Across four verifier backbones and ten benchmarks, DCOCO achieves the highest average throughput in every evaluated configuration, spanning greedy and stochastic decoding with and without extended reasoning, with speedups of up to 6.6x over vanilla decoding. Its advantage persists under concurrent serving: DCOCO outperforms the strongest competing method by 6-23% across 4-32 concurrent requests, while other sequential correctors fall below uncorrected DFlash at these loads. These results demonstrate that recovering intra-block dependencies through parallel contextual scoring delivers consistent acceleration across decoding regimes and serving loads.
