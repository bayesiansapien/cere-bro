---
source: farmer/huggingface
farmed: 2026-04-22T00:00:00
arxiv_id: 2604.17078
url: https://huggingface.co/papers/2604.17078
arxiv_url: https://arxiv.org/abs/2604.17078
date: 2026-04-22
---

# Understanding and Enforcing Weight Disentanglement in Task Arithmetic

Task arithmetic provides an efficient, training-free way to edit pre-trained models, yet lacks a fundamental theoretical explanation for its success. The existing concept of weight disentanglement describes the ideal outcome of non-interfering task composition but does not reveal its underlying cause. We introduce Task-Feature Specialization (TFS), a model's ability to allocate distinct internal features to different tasks, as the fundamental principle. We first prove that TFS is a sufficient condition for weight disentanglement. More importantly, we find that TFS also gives rise to an observable geometric consequence: weight vector orthogonality. We propose OrthoReg, a simple and effective regularization method that actively enforces an internal orthogonal structure on weight updates that constitute task vectors during fine-tuning. Extensive experiments demonstrate that OrthoReg consistently and significantly enhances the performance of various task arithmetic methods.
