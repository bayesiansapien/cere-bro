---
source: farmer/huggingface
farmed: 2026-05-22T10:21:55.060746+00:00
arxiv_id: 2605.21981
url: https://huggingface.co/papers/2605.21981
arxiv_url: https://arxiv.org/abs/2605.21981
date: 2026-05-21
---

# RiT: Vanilla Diffusion Transformers Suffice in Representation Space

Flow matching with x-prediction -- regressing the clean data point rather than the ambient velocity -- is known to exploit low-dimensional manifold structure effectively in pixel space li2025back. We ask whether a pretrained representation space, while containing a low-dimensional data manifold of comparable intrinsic dimensionality, offers a distribution more favorable for flow-matching learning. Comparing pixel, SD-VAE, and DINOv2 features along four geometric axes, we find that pixel and DINOv2 share nearly identical intrinsic dimensionalities (both d!approx!33) yet DINOv2 exhibits 7.3times higher effective rank, 35times better covariance conditioning, 11.5times lower excess kurtosis, and 1.7times lower on-manifold interpolation error; SD-VAE latents are consistently intermediate, indicating that the advantage stems from representation-learning objectives rather than mere compression. These statistical properties render the flow-matching regression well-conditioned and remove the need for the specialized prediction heads or Riemannian transport used by prior DINOv2 diffusion methods. We propose the Representation Image Transformer (RiT): a vanilla Diffusion Transformer trained by x-prediction on frozen DINOv2 features, augmented only by a dimension-aware noise schedule and joint [CLS]-patch modeling. On ImageNet 256{times}256, RiT attains FID 1.45 without guidance and 1.14 with classifier-free guidance, outperforming DiT^DH-XL with 19% fewer parameters (676M vs.\ 839M). The resulting ODE is efficiently solvable at coarse discretizations: with classifier-free guidance, 5 Heun steps already reach FID 2.0 and 10 steps reach 1.25, without distillation or consistency training. Code at https://github.com/lezhang7/RiT.
