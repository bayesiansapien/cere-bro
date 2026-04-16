---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13307
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13307
published: 2026-04-16
authors: Vutichart Buranasiri, James M. Murphy
---

# Deep Spatially-Regularized and Superpixel-Based Diffusion Learning for Unsupervised Hyperspectral Image Clustering

**arXiv:** https://arxiv.org/abs/2604.13307
**Authors:** Vutichart Buranasiri, James M. Murphy

## Abstract

arXiv:2604.13307v1 Announce Type: cross  Abstract: An unsupervised framework for hyperspectral image (HSI) clustering is proposed that incorporates masked deep representation learning with diffusion-based clustering, extending the Spatially-Regularized Superpixel-based Diffusion Learning ($S^2DL$) algorithm. Initially, a denoised latent representation of the original HSI is learned via an unsupervised masked autoencoder (UMAE) model with a Vision Transformer backbone. The UMAE takes spatial context and long-range spectral correlations into account and incorporates an efficient pretraining process via masking that utilizes only a small subset of training pixels. In the next stage, the entropy rate superpixel (ERS) algorithm is used to segment the image into superpixels, and a spatially regularized diffusion graph is constructed using Euclidean and diffusion distances within the compressed latent space instead of the HSI space. The proposed algorithm, Deep Spatially-Regularized Superpixel-based Diffusion Learning ($DS^2DL$), leverages more faithful diffusion distances and subsequent diffusion graph construction that better reflect the intrinsic geometry of the underlying data manifold, improving labeling accuracy and clustering quality. Experiments on Botswana and KSC datasets demonstrate the efficacy of $DS^2DL$.
