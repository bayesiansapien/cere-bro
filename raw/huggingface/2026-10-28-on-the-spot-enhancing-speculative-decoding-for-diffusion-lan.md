---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.994999+05:30
arxiv_id: 2610.22543
url: https://huggingface.co/papers/2610.22543
arxiv_url: https://arxiv.org/abs/2610.22543
date: 2026-10-28
---

# On the SPOT: Enhancing Speculative Decoding for Diffusion Language Models via Commit-Order Prediction

Diffusion language models (DLMs) promise parallel text generation, but in practice face an unresolved speed-quality trade-off. Exact decoding fills in only one masked position per model pass, while faster multi-token decoding schemes are lossy. Speculative decoding is the standard lossless acceleration for autoregressive models. However, it does not transfer directly to DLMs, which must choose both what to generate and where. We show that this order is the missing piece: the model's own predictions from the previous pass already give the right token at over 90% of positions, but not which position comes next. We introduce Speculating Positions Order Trajectory (SPOT), a 0.62M-parameter model that reads only the target's output distributions, predicts this order and proposes a tree of candidate continuations, which the target verifies in a single pass by state equality. Coupled-noise match, which shares Gumbel noise between drafter and target, keeps this verification exact at any temperature. This approach also inspired us to introduce SPOT-Sets for dynamic threshold decoding, where a pass commits several positions: SPOT-Sets drafts whole commit sets together with their tokens. Our comprehensive experiments show that SPOT cuts target passes by up to 6.8times and reaches up to 3.4times the throughput of standard decoding on SDAR-8B, matching or beating the calibrated and training-free drafting baselines in every task and budget at T=0 and T=1. In addition, we show that SPOT's learned drafter transfers across models, demonstrating successful transfer across six different DLMs; with a light calibration, the SPOT-Sets drafter transfers as well. On top of dynamic threshold decoding, SPOT-Sets improves the throughput of SDAR-8B by 59% on average over the threshold decoder alone. Project page: https://eliezer318.github.io/SPOT-dLLM/
