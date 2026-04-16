---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13287
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13287
published: 2026-04-16
authors: Gabriel Afriat, Xiang Meng, Shibal Ibrahim
---

# MOONSHOT : A Framework for Multi-Objective Pruning of Vision and Large Language Models

**arXiv:** https://arxiv.org/abs/2604.13287
**Authors:** Gabriel Afriat, Xiang Meng, Shibal Ibrahim

## Abstract

arXiv:2604.13287v1 Announce Type: new  Abstract: Weight pruning is a common technique for compressing large neural networks. We focus on the challenging post-training one-shot setting, where a pre-trained model is compressed without any retraining. Existing one-shot pruning methods typically optimize a single objective, such as a layer-wise reconstruction loss or a second-order Taylor approximation of the training loss. We highlight that neither objective alone is consistently the most effective across architectures and sparsity levels. Motivated by this insight, we propose MOONSHOT, a general and flexible framework that extends any single-objective pruning method into a multi-objective formulation by jointly optimizing both the layer-wise reconstruction error and second-order Taylor approximation of the training loss. MOONSHOT acts as a wrapper around existing pruning algorithms. To enable this integration while maintaining scalability to billion-parameter models, we propose modeling decisions and introduce an efficient procedure for computing the inverse Hessian, preserving the efficiency of state-of-the-art one-shot pruners. When combined with state-of-the-art pruning methods on Llama-3.2 and Llama-2 models, MOONSHOT reduces C4 perplexity by up to 32.6% at 2:4 sparsity and improves zero-shot mean accuracy across seven classification benchmarks by up to 4.9 points. On Vision Transformers, it improves accuracy on ImageNet-1k by over 5 points at 70% sparsity, and on ResNet-50, it yields a 4-point gain at 90% sparsity.
