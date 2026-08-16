---
source: farmer/huggingface
farmed: 2026-08-16T08:10:48.292809+00:00
arxiv_id: 2608.02870
url: https://huggingface.co/papers/2608.02870
arxiv_url: https://arxiv.org/abs/2608.02870
date: 2026-08-14
---

# Maglev: Sliding Recurrent Memory

We introduce , a recurrent Transformer architecture with fixed-size memory that generalizes sliding-window attention while remaining parallelizable during training.  consists of two coupled models: a prefiller Q, which leverages full attentionIn practice, we use interleaved full and sliding-window attention for Q, as this yields stronger performance. The essential requirement is that Q be more expressive than P, with access to the full history. to produce memory targets m'_t, and a decoder P, which uses only sliding-window attention and recurrent K/V injection to produce decoder memories m_t for next-token prediction. We train  with a memory consistency loss that aligns m_t with m'_t, allowing inference to use P alone. Empirically,  improves validation loss and downstream pretraining benchmarks over sliding-window and latent recurrent transformer baselines. Moreover, sharing parameters between P and Q reduces parameter memory while preserving most of the gains.
