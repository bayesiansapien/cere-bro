---
source: farmer/huggingface
farmed: 2026-11-14T05:10:36.533256+00:00
arxiv_id: 2611.14046
url: https://huggingface.co/papers/2611.14046
arxiv_url: https://arxiv.org/abs/2611.14046
date: 2026-11-13
---

# Structured Confidence Perturbation via Fisher Geometry for Adversarial Training

Adversarial training is often plagued by "pseudo-attacks", perturbations that significantly increase the loss value but fail to truly alter the model's confidence structure. To address this, we propose two complementary approaches to directly attack and defend against confidence structure deformation. First, building upon the traditional loss maximization perspective, we introduce a hybrid objective that integrates cross-entropy and KL divergence, encouraging adversarial examples to simultaneously disrupt prediction accuracy and distribution consistency. Second, we geometrically reconstruct adversarial training by generating perturbations that maximize the distribution distance on the confidence manifold. Theoretical analysis shows that the optimal perturbation direction aligns with the principal eigenvectors of the Fisher information matrix. We also propose an efficient algorithm to avoid high-dimensional matrix computations. Experiments on multiple datasets and model architectures demonstrate that our method outperforms existing methods in adversarial robustness and robust transferability, particularly excelling in structural perturbations within high-confidence regions.
