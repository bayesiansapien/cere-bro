---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.996619+05:30
arxiv_id: 2610.26030
url: https://huggingface.co/papers/2610.26030
arxiv_url: https://arxiv.org/abs/2610.26030
date: 2026-10-28
---

# Truncate or Not? A Scaling Study of Looped Transformers with Truncated Backpropagation

Looped transformers reuse a shared block of layers to increase computational depth without increasing the number of trainable parameters. They are trained with backpropagation through time (BPTT). To save training compute, BPTT is often truncated to the last few loops, but truncation yields biased gradients that may weaken the benefit of looping. In this work, we study the value of truncation in looped transformer training in a systematic way: we jointly vary model size, training tokens, and forward and backward loop counts across nearly 600 training runs and fit a unified scaling law that captures the effects of looping and truncation through effective parameters. Despite the training-compute savings of truncation, our fitted law favors full BPTT when forward and backward loop counts are jointly optimized. In matched-compute runs, full BPTT through fewer loops consistently outperforms truncated settings of the same compute. The law further shows that at fixed model size, the compute-optimal loop count and training-token budget both grow with compute. When model size is also free, the law identifies two fully trained loops as the best looped setting. Experimentally, this setting achieves lower validation loss than the compute-optimal non-looped model with about 27% fewer non-embedding parameters and only 8% more training compute.
