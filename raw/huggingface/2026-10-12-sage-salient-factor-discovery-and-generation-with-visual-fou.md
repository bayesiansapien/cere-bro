---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.224759+05:30
arxiv_id: 2609.39635
url: https://huggingface.co/papers/2609.39635
arxiv_url: https://arxiv.org/abs/2609.39635
date: 2026-10-12
---

# SAGE: Salient Factor Discovery and Generation with Visual Foundation Representations

Given a target dataset, such as faces with eyeglasses, and a background dataset, such as faces without, contrastive analysis separates salient factors specific to the target from common content shared by both. We aim for salient representations that capture target-specific detail in each image, such as the shape, color, and position of the glasses, so that they reveal subtypes without subtype labels and guide the generation of new examples of a discovered subtype, even one with no name or text description. We introduce SAGE, which learns both factors directly in the high-dimensional spatial latent of a frozen representation autoencoder and conditions a diffusion transformer on the learned salient representation of a reference image. On Digits-ImageNet and FFHQ eyeglasses, SAGE combines high-fidelity reconstruction (rFID below 2) with unsupervised subtype discovery, recovering the digits better than baselines (probe accuracy 0.950 vs.\ at most 0.281) and revealing eyewear types, finer sunglasses styles, and mislabeled images; salient-conditioned generation raises Digits-ImageNet subtype accuracy over the unfactorized latent (90.5% vs.\ 27.7%) and diversity on both datasets. On retinal OCT, SAGE's salient space separates three diseases using only normal/disease labels.
