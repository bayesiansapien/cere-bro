---
source: farmer/huggingface
farmed: 2026-06-03T06:14:02Z
arxiv_id: 2606.01048
url: https://huggingface.co/papers/2606.01048
arxiv_url: https://arxiv.org/abs/2606.01048
date: 2026-06-03
---

# Decoupled Residual Denoising Diffusion Models for Unified and Data Efficient Image-to-Image Translation

We propose Decoupled Residual Denoising Diffusion models (DRDD) for unified and data-efficient image-to-image (I2I) translation. While diffusion models have advanced I2I translation in terms of quality and diversity, we uncover a previously under-explored property in diffusion models. Crucially, beyond its conventional role of manifold lifting (i.e., moving data off low-dimensional manifolds), injecting Gaussian noise facilitates domain harmonization by implicitly aligning feature distributions across domains, a property particularly advantageous for unified I2I translation. However, existing diffusion models prematurely erode this harmonization effect, as noise and residuals are simultaneously removed in a single coupled diffusion process. To address this, DRDD decouples the diffusion process into two sequential and independent diffusion stages: (1) a stochastic noise diffusion for domain harmonization and manifold lifting, and (2) a deterministic residual diffusion that learns the core semantic mapping entirely within the fixed-noise domain. This decoupling preserves harmonization and manifold lifting effects throughout the transformation, substantially simplifying the learning of unified mappings across diverse tasks and domains. Notably, the noise diffusion stage is trained exclusively on abundant, unpaired target-domain images, greatly improving data efficiency. Comprehensive theoretical and empirical analysis demonstrates that DRDD is broadly compatible with mainstream diffusion models and consistently delivers robust, unified I2I translation, even under limited paired data. Our code is available at https://github.com/HKU-HealthAI/DRDD.
