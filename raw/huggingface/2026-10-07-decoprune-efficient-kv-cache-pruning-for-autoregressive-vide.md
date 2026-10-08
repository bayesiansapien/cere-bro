---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2609.39096
url: https://huggingface.co/papers/2609.39096
arxiv_url: https://arxiv.org/abs/2609.39096
date: 2026-10-07
---

# DeCoPrune: Efficient KV-Cache Pruning for Autoregressive Video Diffusion via Denoising Consistency

Autoregressive video diffusion supports streaming generation and interactive control, but its KV cache grows continuously with the generated history. Existing compression strategies either discard history using fixed windows or select tokens through local attention and similarity signals, which do not directly measure whether the current chunk contributes information beyond the retained context. We introduce DeCoPrune, a training-free method that treats cache compression as a denoising-consistency problem. We find empirically that denoising difficulty provides a useful proxy for a token's value in long-term retention: tokens with larger step-to-final discrepancies tend to carry visual evidence that is less predictable from the retained context. DeCoPrune measures each current-chunk token's denoising difficulty using the discrepancy between its intermediate clean prediction and final denoised value, retaining high-discrepancy tokens in the long-term cache while pruning those with low discrepancy. To evaluate information retention, we introduce CMBench, comprising 58 approximately one-minute generated or real-world context episodes and 116 Reappear or Revisit continuation tasks that require recalling specific previously observed objects or scenes. Experiments with LingBot World v2 show that DeCoPrune preserves near-FullKV long-range recall while pruning over 85% of historical KV tokens and accelerating continuation generation by over 4times, substantially outperforming the evaluated compression baselines at comparable budgets. These results indicate that denoising consistency can serve as a model-intrinsic signal for retaining long-range information while reducing autoregressive inference cost. Our project homepage is https://decoprune.github.io. The code is available at https://github.com/DeCoPrune/CMBench, and the benchmark at https://huggingface.co/datasets/Aoraku/CMBench.
