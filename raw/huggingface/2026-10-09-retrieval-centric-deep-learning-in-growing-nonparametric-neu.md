---
source: farmer/huggingface
farmed: 2026-10-10T05:09:51.416262+00:00
arxiv_id: 2610.03858
url: https://huggingface.co/papers/2610.03858
arxiv_url: https://arxiv.org/abs/2610.03858
date: 2026-10-09
---

# Retrieval-Centric Deep Learning in Growing Nonparametric Neural Networks

We investigate a general-purpose layer for deep learning that, instead of compressing arbitrary-size training data into fixed-size weight matrices, stores a new pair of key-value representations for every data point during training, and retrieves and recombines these representations through an attention mechanism at inference time - resulting in a growing neural net (NN). While Irie et al. (arXiv:2202.05798) have put forward this perspective from the classic duality expressing any linear layer in a deep NN trained by gradient descent as linear attention (LA) over the training data points, replacing LA by more powerful attention functions, as they suggest, turns out to be non-trivial: we show that naively applying learning rules from the LA case to advanced kernels does not lead to principled optimization. Here we fill this gap and develop functional gradient-based learning rules for kernelized attention layers, based on radial basis function (RBF) and softmax-like kernels - establishing the principled "retrieval-centric deep learning" (RCDL) paradigm. Empirically, we demonstrate the promising performance and learning-efficiency of RCDL on image classification and synthetic teacher-student learning tasks. Moreover, we show that replacing LA in the dual form of NNs by advanced LA variants, namely MesaNet/DeltaNet, yields a formal connection to recently proposed optimizers for conventional fixed-size NNs, offering a novel perspective on deep learning optimization.
