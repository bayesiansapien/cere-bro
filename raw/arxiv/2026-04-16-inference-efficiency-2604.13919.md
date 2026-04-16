---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13919
category: cs.LG
concept: inference-efficiency
url: https://arxiv.org/abs/2604.13919
published: 2026-04-16
authors: Anran Jiao, Wengyao Jiang, Xiaoyi Lu
---

# Nested Fourier-enhanced neural operator for efficient modeling of radiation transfer in fires

**arXiv:** https://arxiv.org/abs/2604.13919
**Authors:** Anran Jiao, Wengyao Jiang, Xiaoyi Lu

## Abstract

arXiv:2604.13919v1 Announce Type: cross  Abstract: Computational fluid dynamics (CFD) has become an essential tool for predicting fire behavior, yet maintaining both efficiency and accuracy remains challenging. A major source of computational cost in fire simulations is the modeling of radiation transfer, which is usually the dominant heat transfer mechanism in fires. Solving the high-dimensional radiative transfer equation (RTE) with traditional numerical methods can be a performance bottleneck. Here, we present a machine learning framework based on Fourier-enhanced multiple-input neural operators (Fourier-MIONet) as an efficient alternative to direct numerical integration of the RTE. We first investigate the performance of neural operator architectures for a small-scale 2D pool fire and find that Fourier-MIONet provides the most accurate radiative solution predictions. The approach is then extended to 3D CFD fire simulations, where the computational mesh is locally refined across multiple levels. In these high-resolution settings, monolithic surrogate models for direct field-to-field mapping become difficult to train and computationally inefficient. To address this issue, a nested Fourier-MIONet is proposed to predict radiation solutions across multiple mesh-refinement levels. We validate the approach on 3D McCaffrey pool fires simulated with FireFOAM, including fixed fire sizes and a unified model trained over a continuous range of heat release rates (HRRs). The proposed method achieves global relative errors of 2-4% for 3D varying-HRR scenarios while providing faster inference than the estimated cost of one finite-volume radiation solve in FireFOAM for the 16-solid-angle case. With fast and accurate inference, the surrogate makes higher-fidelity radiation treatments practical and enables the incorporation of more spectrally resolved radiation models into CFD fire simulations for engineering applications.
