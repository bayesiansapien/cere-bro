---
source: farmer/huggingface
farmed: 2026-05-17T00:00:00Z
arxiv_id: "2605.14438"
url: "https://huggingface.co/papers/2605.14438"
arxiv_url: "https://arxiv.org/abs/2605.14438"
date: 2026-05-17
---

# BEAM: Binary Expert Activation Masking for Dynamic Routing in MoE

Mixture-of-Experts (MoE) architectures enhance the efficiency of large language models by activating only a subset of experts per token. However, standard MoE employs a fixed Top-K routing strategy, leading to redundant computation and suboptimal inference latency. Existing acceleration methods either require costly retraining with architectural changes or suffer from severe performance drop at high sparsity due to train-inference mismatch. To address these limitations, we propose BEAM (Binary Expert Activation Masking), a novel method that learns token-adaptive expert selection via trainable binary masks. With a straight-through estimator and an auxiliary regularization loss, BEAM induces dynamic expert sparsity through end-to-end training while maintaining model capability. We further implement an efficient custom CUDA kernel for BEAM, ensuring seamless integration with the vLLM inference framework. Experiments show that BEAM retains over 98% of the original model's performance while reducing MoE layer FLOPs by up to 85%, achieving up to 2.5x faster decoding and 1.4x higher throughput.
