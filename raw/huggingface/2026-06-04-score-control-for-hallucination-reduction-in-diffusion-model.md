---
source: farmer/huggingface
farmed: 2026-06-04T06:39:44Z
arxiv_id: 2606.00377
url: https://huggingface.co/papers/2606.00377
arxiv_url: https://arxiv.org/abs/2606.00377
date: 2026-06-04
---

# Score-Control for Hallucination Reduction in Diffusion Models

Diffusion models have emerged as the backbone of modern generative AI, powering advances in vision, language, audio and other modalities. Despite their success, they suffer from hallucinations, implausible samples that lie outside the support of true data distribution, which degrade reliability and trust. In this work, we first empirically confirm previously proposed hypothesis that score smoothness causes hallucinations in Image Generation diffusion models and provide a density-based perspective. We further formalize this notion by linking the hallucinations probability mass to lipschitz constant of the learned score function. Motivated by this, we introduce a Variance-Guided Score Modulation (VSM) strategy that controls the score Jacobian, in turn reducing score smoothness and better approximating the ground truth score that decreases hallucinations. Empirical results on synthetic and real-world datasets demonstrate that our approach reduces hallucinations (up to ~25%) while maintaining high fidelity and diversity, providing a principled step toward more reliable diffusion-based image generation. We also propose two benchmark datasets with extreme semantic variation for systematic hallucination evaluation. Code and Datasets are publicly available at https://github.com/bhosalems/VSM.
