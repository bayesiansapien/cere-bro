---
source: farmer/huggingface
farmed: 2026-09-29T05:05:53.599471+00:00
arxiv_id: 2609.31291
url: https://huggingface.co/papers/2609.31291
arxiv_url: https://arxiv.org/abs/2609.31291
date: 2026-09-28
---

# Softmax Reparameterization for Output-Head Quantization

Large vocabularies make output heads a substantial inference cost in small language models. We propose softmax reparameterization, a post-training method that selects a functionally equivalent output head before quantization. The method subtracts a scalar multiple of the vocabulary-row mean from every output row and selects the coefficient by validation KL separately for RTN, activation-weighted MSE, and full-Hessian GPTQ. This one-dimensional search includes the original head and fixed mean-centering, preserves the full-precision softmax distribution, and leaves the trained decoder unchanged; a rank-one correction handles nonlinear logit paths such as soft-capping. Across seven heads, W4 gains concentrate where baseline quantization substantially distorts predictions: on Phi-4-mini, AW-MSE KL falls from 0.936 to 0.256. The gains survive stronger GPTQ calibration and remain complementary to exact per-channel scaling and affine quantization. Across four heads and three W4 quantizers, frozen WikiText-selected coefficients also transfer to C4 and OpenWebMath, outperforming mean-centering in all 18 comparisons where the frozen coefficient differs from 1 and matching it in the remaining six. At W2, used as a compression stress test, benefits broaden across nearly the full model--quantizer matrix. Matched residual analysis shows that improved fidelity can accompany greater logit reconstruction error while reducing the residual's Fisher-weighted cost. For shift-compatible heads, reparameterization adds no inference operation and preserves packed W4 execution: with the decoder held in BF16, quantizing the Phi output head reduces batch-one generation latency by 10.8% relative to the BF16-head baseline.
