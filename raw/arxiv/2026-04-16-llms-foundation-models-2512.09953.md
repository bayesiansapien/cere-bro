---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2512.09953
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2512.09953
published: 2026-04-16
authors: Mohammad M Maheri, Sunil Cotterill, Alex Davidson
---

# ZK-APEX: Zero-Knowledge Approximate Personalized Unlearning with Executable Proofs

**arXiv:** https://arxiv.org/abs/2512.09953
**Authors:** Mohammad M Maheri, Sunil Cotterill, Alex Davidson

## Abstract

arXiv:2512.09953v2 Announce Type: replace-cross  Abstract: Machine unlearning aims to remove the influence of specific data points from a trained model to satisfy privacy, copyright, and safety requirements. In real deployments, providers distribute a global model to many edge devices, where each client personalizes the model using private data. When a deletion request is issued, clients may ignore it or falsely claim compliance, and providers cannot check their parameters or data. This makes verification difficult, especially because personalized models must forget the targeted samples while preserving local utility, and verification must remain lightweight on edge devices.   We introduce ZK APEX, a zero-shot personalized unlearning method that operates directly on the personalized model without retraining. ZK APEX combines sparse masking on the provider side with a small Group OBS compensation step on the client side, using a blockwise empirical Fisher matrix to create a curvature-aware update designed for low overhead. Paired with Halo2 zero-knowledge proofs, it enables the provider to verify that the correct unlearning transformation was applied without revealing any private data or personalized parameters.   On Vision Transformer classification tasks, ZK APEX recovers nearly all personalization accuracy while effectively removing the targeted information. Applied to the OPT125M generative model trained on code data, it recovers around seventy percent of the original accuracy. Proof generation for the ViT case completes in about two hours, more than ten million times faster than retraining-based checks, with less than one gigabyte of memory use and proof sizes around four hundred megabytes. These results show the first practical framework for verifiable personalized unlearning on edge devices.
