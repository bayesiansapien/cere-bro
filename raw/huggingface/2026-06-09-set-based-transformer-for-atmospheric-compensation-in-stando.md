---
source: farmer/huggingface
farmed: 2026-06-09T16:28:21
arxiv_id: 2606.08324
url: https://huggingface.co/papers/2606.08324
arxiv_url: https://arxiv.org/abs/2606.08324
date: 2026-06-09
---

# Set-Based Transformer for Atmospheric Compensation in Standoff LWIR Hyperspectral Imaging

Passive long-wave infrared (LWIR) hyperspectral imaging under a standoff geometry depends on atmospheric absorption and emission, as well as reflected radiance, thus making atmospheric compensation essential to get knowledge of a target of interest. Despite its importance, this compensation has been largely overlooked due to its practical and modeling difficulty. In this paper, we present a lightweight set-based deep learning framework that takes multiple radiance measurements, collected at different standoff ranges, as input and jointly estimates transmittance, atmospheric path radiance, and a shared downwelling spectrum. We analyze the learned representation with a sparse autoencoder and observe that several latent features do activate on geographically coherent subsets of the test data despite the absence of location supervision. Experiments on a MODTRAN generated standoff LWIR dataset demonstrate low spectral distortion across all estimated products. The dataset and code is publicly available at: https://factral.co/SAE-LWIR/
