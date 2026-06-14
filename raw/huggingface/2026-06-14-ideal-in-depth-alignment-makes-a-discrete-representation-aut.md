---
source: farmer/huggingface
farmed: 2026-06-14T07:38:18Z
arxiv_id: 2606.11096
url: https://huggingface.co/papers/2606.11096
arxiv_url: https://arxiv.org/abs/2606.11096
date: 2026-06-14
---

# IDEAL: In-DEpth ALignment Makes A Discrete Representation AutoEncoder

Built on pretrained vision foundation models (VFMs), representation autoencoders (RAEs) have recently emerged as a promising approach for constructing semantically rich latent spaces for image generation. However, their reconstruction quality often remains suboptimal, largely because deep VFM representations do not preserve sufficient fine-grained visual detail. This limitation becomes even more severe after discretization, where missing low-level information is difficult to recover. In fact, we observe that shallow VFM features retain considerably richer local appearance and structural detail, which complements the high-level semantics carried by deep features used in existing RAEs. Motivated by this complementary property, we propose Ideal, an In-depth Alignment framework for discrete representation autoencoding. By jointly aligning quantized tokens with both shallow and deep VFM features, Ideal enables the resulting discrete visual tokens to preserve both visual fidelity and rich semantics. Extensive experiments demonstrate that Ideal yields superior reconstruction performance, achieving 0.61 rFID on ImageNet and outperforming the previous best method by 0.28. When used for autoregressive image generation, Ideal further produces a gFID of 1.89, establishing a new state of the art for autoregressive image generation.
