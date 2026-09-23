---
source: farmer/huggingface
farmed: 2026-09-23T05:53:04.588715+00:00
arxiv_id: 2609.26774
url: https://huggingface.co/papers/2609.26774
arxiv_url: https://arxiv.org/abs/2609.26774
date: 2026-09-23
---

# StableVQ: Practical Guidelines for Stable Vector-Quantized Tokenizer Training

Vector Quantization (VQ) is fundamental to discrete visual tokenizers that power modern autoregressive and masked image generation models. While recent shared-projection codebook methods have substantially advanced codebook utilization, training stability remains a critical and underexplored challenge. We argue that the root cause lies in the entanglement of the Encoder--Decoder and Codebook training: because neither module can reliably fulfill its own responsibility in isolation, the system can only function when the two subsystems happen to cooperate---a fragile condition that breaks down precisely when training is most stressed. We propose StableVQ, which revisits the proper learning objective of each module and resolves the problems that arise when each is trained to fulfill its own role independently. Concretely, (1) Dynamic STE corrects the instability in the Encoder's learning objective, enabling it to robustly optimize the reconstruction space under discrete regularization even when codebook utilization is low. (2) Region VQ Loss reconceives the Codebook's learning objective so that it can independently guarantee full tracking of the encoder output distribution, without relying on encoder oscillations to drive activation. (3) Decoupled Schedule recognizes that the distinct responsibilities of the Encoder--Decoder and the Codebook demand distinct optimization dynamics, and assigns each an independent learning rate schedule to ensure robust system-level behavior. Built on top of shared-projection codebooks, StableVQ is lightweight and introduces no learnable parameters. Experiments on ImageNet demonstrate consistent improvements in training stability, codebook utilization, and reconstruction quality across diverse codebook sizes and initialization settings.
