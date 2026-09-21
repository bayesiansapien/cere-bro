---
source: farmer/huggingface
farmed: 2026-09-21T05:24:18.050611+00:00
arxiv_id: 2609.19122
url: https://huggingface.co/papers/2609.19122
arxiv_url: https://arxiv.org/abs/2609.19122
date: 2026-09-21
---

# Training-Adaptive Convolutional Sparse Coding via Information Bottleneck for Robust Visual Representation

Visual signals require compact yet sufficient representations for robust downstream prediction. Convolutional sparse coding (CSC) provides an explicit mechanism for suppressing redundant components while preserving signal content, but its sparsity coefficient is typically fixed and manually selected. We propose a training-adaptive convolutional sparse coding framework for robust visual signal representation. Specifically, we unfold the CSC optimization with the Fast Iterative Shrinkage-Thresholding Algorithm (FISTA) and treat the sparsity coefficient as a differentiable variable jointly learned with the network parameters. From the information bottleneck perspective, this coefficient controls the trade-off between information retention and compression: the sparsity term promotes compact representations, while the reconstruction term together with task loss preserves task-relevant signal content. We further introduce a label-free post-training strategy that adjusts the compression strength for corrupted inputs with the main network parameters fixed. Experiments on CIFAR and ImageNet demonstrate competitive clean-data recognition and greatly improved robustness under different input perturbations.
