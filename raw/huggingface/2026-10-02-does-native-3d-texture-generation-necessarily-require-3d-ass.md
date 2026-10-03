---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.822308+00:00
arxiv_id: 2609.34621
url: https://huggingface.co/papers/2609.34621
arxiv_url: https://arxiv.org/abs/2609.34621
date: 2026-10-02
---

# Does Native 3D Texture Generation Necessarily Require 3D Assets for Training?

Native 3D texture generation synthesizes colors directly in 3D space for a given geometry, conditioned on multi-view reference images. It is generally believed that training such models requires large-scale, high-quality real 3D asset data, whose acquisition remains a long-standing and challenging problem. In this work, we propose Tex-Zero, demonstrating that a high-fidelity native 3D texture generation framework can be trained without 3D assets. Our key observation is that only high-quality and fine-grained color information is essential for 3D texture training, while the required geometric information is less critical and can be manually constructed rather than obtained from real 3D assets. This finding makes it possible to transform abundant, high-quality 2D images into effective training samples for 3D texture generation. Specifically, we convert high-quality 2D images into 3D training samples by representing each image as a plane in 3D space and applying patch-wise random rotations and aggregation to construct complex geometric structures. Using these constructed image data, we train the Tex-Zero VAE, which can reconstruct real 3D assets with high quality despite never observing them during training. Building upon the Tex-Zero VAE, we train the Tex-Zero DiT also exclusively on the constructed image data, where the conditioning 2D multi-view images are transformed into planes in 3D space and also encoded by the Tex-Zero VAE, thereby reducing the representation gap and improving generation quality. Extensive experiments show that Tex-Zero generates high-fidelity 3D textures with fine-grained details solely using images as training data, offering a promising perspective on the data paradigm for scaling 3D texture generation.
