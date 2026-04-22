---
source: farmer/huggingface
farmed: 2026-04-22T00:00:00
arxiv_id: 2604.19254
url: https://huggingface.co/papers/2604.19254
arxiv_url: https://arxiv.org/abs/2604.19254
date: 2026-04-22
---

# ShadowPEFT: Shadow Network for Parameter-Efficient Fine-Tuning

Parameter-efficient fine-tuning (PEFT) reduces the training cost of full-parameter fine-tuning for large language models (LLMs) by training only a small set of task-specific parameters while freezing the pretrained backbone. However, existing approaches, such as Low-Rank Adaptation (LoRA), achieve adaptation by inserting independent low-rank perturbations directly to individual weights, resulting in a local parameterization of adaptation. We propose ShadowPEFT, a centralized PEFT framework that instead performs layer-level refinement through a depth-shared shadow module. At each transformer layer, ShadowPEFT maintains a parallel shadow state and evolves it repeatedly for progressively richer hidden states. This design shifts adaptation from distributed weight-space perturbations to a shared layer-space refinement process. Since the shadow module is decoupled from the backbone, it can be reused across depth, independently pretrained, and optionally deployed in a detached mode, benefiting edge computing scenarios. Experiments on generation and understanding benchmarks show that ShadowPEFT matches or outperforms LoRA and DoRA under comparable trainable-parameter budgets.
