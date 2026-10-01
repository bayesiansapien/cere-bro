---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.33591
url: https://huggingface.co/papers/2609.33591
arxiv_url: https://arxiv.org/abs/2609.33591
date: 2026-09-30
---

# Pretraining Transformers with Quantized Softmax in Attention

Low-precision Transformer systems increasingly quantize attention matrix multiplications, while softmax often remains at higher precision. During pretraining, an approximate softmax changes the gradients that train the model as well as its forward computation. We study this interaction with K-interval attention, which approximates the exponential using K+1 grid values. We vary per-row grid calibration, interpolation versus hard rounding, and the placement of a straight-through surrogate relative to normalization. We derive the corresponding backward rules, including calibration derivatives, and compare these choices in pretraining experiments matched on model, data, and optimizer. Detaching the row extrema leaves the forward computation unchanged but produces a delayed increase in validation loss. With hard rounding at K=4, min-max calibration and a pre-normalization surrogate incur a large loss gap; changing either choice substantially reduces it. At 124M parameters and 2.5B training tokens, fixed-window calibration with a post-normalization surrogate yields a validation loss gap of +0.019 nats relative to softmax at K=4, and with a pre-normalization surrogate yields +0.004 nats at K=16.
