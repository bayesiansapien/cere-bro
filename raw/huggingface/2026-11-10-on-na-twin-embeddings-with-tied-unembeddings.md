---
source: farmer/huggingface
farmed: 2026-11-11T05:06:31.326237+00:00
arxiv_id: 2611.10556
url: https://huggingface.co/papers/2611.10556
arxiv_url: https://arxiv.org/abs/2611.10556
date: 2026-11-10
---

# onóna: Twin Embeddings with Tied Unembeddings

Weight tying reduces the parameter cost of language models, but the usual tied output head is limited to a single softmax. We introduce onóna, a two-table parameterization that increases output expressiveness while preserving input-output weight sharing. The Transformer takes the average of two embedding tables as input, and the output head combines the softmax distributions defined by those same tables. A gate conditioned only on the current input token determines the mixture weight. Its values can be precomputed for inference, and the Transformer body remains unchanged. We evaluate onóna across Dense, Gated DeltaNet hybrid, mixture-of-experts, and Attention Residual architectures at 142M, 330M, and 1B scales. Under matched token budgets, onóna lowers final validation loss and external perplexity in 11 of 12 comparisons and raises the average accuracy over eight downstream tasks in 10 of 12. The one exception on loss is the 1B MoE model. The cost is one extra embedding table and one extra vocabulary projection.
