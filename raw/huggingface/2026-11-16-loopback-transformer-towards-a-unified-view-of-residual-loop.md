---
source: farmer/huggingface
farmed: 2026-11-17T08:29:01.998518+00:00
arxiv_id: 2611.07226
url: https://huggingface.co/papers/2611.07226
arxiv_url: https://arxiv.org/abs/2611.07226
date: 2026-11-16
---

# Loopback Transformer: Towards a Unified View of Residual Looped Transformers

Looped Transformers reduce parameter count by repeatedly applying shared blocks, but parameter sharing alone does not determine how the results of repeated computation are reused. We take the depth-memory view of residual connections and analyze which representation is stored after each block application and how later reads weight it. A full block output contains both its input and its new update, so weighting that output also reweights the history already carried by the input. Reading individual updates instead, with the shared stack's input kept on a separate path, gives separate controls over input strength, total update weight, and allocation across updates. The Loopback Transformer implements these controls: geometric decay sets the total update weight and supplies a recency prior, and attention learns how to allocate that weight. On ClimbMix, Loopback reaches lower validation loss than standard Transformer baselines with 40-75% of their Transformer parameters (excluding token embeddings and the output head) at reference scales from 191M to 3B, with training tokens and executed depth matched. It also has higher mean accuracy over thirteen downstream tasks at 1.4B and 3B. At 191M, 374M, and 778M, it has the lowest validation loss and the highest thirteen-task mean among the standard Transformer and seven looped residual designs.
