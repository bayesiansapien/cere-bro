---
source: farmer/huggingface
farmed: 2026-11-10T05:05:44.204415+00:00
arxiv_id: 2611.07025
url: https://huggingface.co/papers/2611.07025
arxiv_url: https://arxiv.org/abs/2611.07025
date: 2026-11-09
---

# LowRAM: Low-Rank Keys and Amortised Values for Composable KV Cache Compression at Test-Time

Autoregressive decoding relies on the KV cache, whose memory footprint grows linearly with context length and caps batch size and throughput. Existing post-training methods exploit redundancy across tokens, layers, and feature dimensions, or lower numerical precision. We identify a complementary axis: within each attention head, values are largely predictable from their corresponding keys. We exploit this with value cache amortisation, which fits a lightweight per-head predictor at test time and stores residuals only for the tokens it reconstructs worst, giving 4times near-lossless value compression. The predictor can be initialised by meta-learning for substantially reduced prefill overhead, or fitted from scratch in settings that allow a one-off cost, such as multi-query inference. We pair value amortisation with cross-layer low-rank key compression to produce LowRAM, an asymmetric compression pipeline that stays close to lossless across three model families. By reconstructing only a selected subset of KV pairs at each decoding step, LowRAM can keep decoding overhead minimal and achieve up to 5times higher peak decode throughput at 4times compression. LowRAM further composes with quantisation and eviction, reaching 26.9times compression at 94.5% of baseline performance on long contexts. These results show that treating keys and values as structurally distinct enables efficient, aggressive, and composable KV cache compression.
