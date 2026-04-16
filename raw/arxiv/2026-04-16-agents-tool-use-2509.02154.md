---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2509.02154
category: cs.AI
concept: agents-tool-use
url: https://arxiv.org/abs/2509.02154
published: 2026-04-16
authors: Aymene Mohammed Bouayed, Samuel Deslauriers-Gauthier, Adrian Iaccovelli
---

# Heavy-Tailed Class-Conditional Priors for Long-Tailed Generative Modeling

**arXiv:** https://arxiv.org/abs/2509.02154
**Authors:** Aymene Mohammed Bouayed, Samuel Deslauriers-Gauthier, Adrian Iaccovelli

## Abstract

arXiv:2509.02154v2 Announce Type: replace-cross  Abstract: Variational Autoencoders (VAEs) with global priors trained under an imbalanced empirical class distribution can lead to underrepresentation of tail classes in the latent space. While $t^3$VAE improves robustness via heavy-tailed Student's $t$-distribution priors, its single global prior still allocates mass proportionally to class frequency. We address this latent geometric bias by introducing C-$t^3$VAE, which assigns a per-class Student's $t$ joint prior over latent and output variables. This design promotes uniform prior mass across class-conditioned components. To optimize our model we derive a closed-form objective from the $\gamma$-power divergence, and we introduce an equal-weight latent mixture for class-balanced generation. On SVHN-LT, CIFAR100-LT, and CelebA datasets, C-$t^3$VAE consistently attains lower FID scores than $t^3$VAE and Gaussian-based VAE baselines under severe class imbalance while remaining competitive in balanced or mildly imbalanced settings. In per-class F1 evaluations, our model outperforms the conditional Gaussian VAE across highly imbalanced settings. Moreover, we identify the mild imbalance threshold $\rho < 5$, for which Gaussian-based models remain competitive. However, for $\rho \geq 5$ our approach yields improved class-balanced generation and mode coverage.
