---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2609.34117
url: https://huggingface.co/papers/2609.34117
arxiv_url: https://arxiv.org/abs/2609.34117
date: 2026-10-07
---

# SlimWise: Decoupling Expert Pruning Across Prefill and Decode for Efficient MoE Serving

Mixture-of-experts (MoE) models activate few experts per token, yet batched decoding can access nearly the entire expert pool, making expert-weight traffic a major bottleneck. Expert pruning reduces this traffic, but conventional approaches also prune compute-bound prefill, sacrificing model quality for little throughput benefit. We present SlimWise, a serving framework that tailors the expert pool to each inference phase. SlimWise performs prefill with the full model and decode with a pruned model that directly reuses the prefill-generated KV cache without conversion. Across two MoE backbones and three pruning criteria, this training-free KV cache handoff substantially narrows accuracy gaps relative to the full model in many settings. We also show that benchmark accuracy can conceal substantial pruning-induced changes in generation length. To address these distortions and residual accuracy loss, SlimWise introduces a low-cost distillation stage that trains the decoder to continue from full-model KV caches while updating only a small subset of parameters. Implemented in vLLM, SlimWise supports both prefill-decode (PD) disaggregation and PD-colocated serving. On Qwen3.6-35B-A3B, SlimWise improves decode throughput by up to 1.81x at 50% expert pruning with minimal accuracy loss.
