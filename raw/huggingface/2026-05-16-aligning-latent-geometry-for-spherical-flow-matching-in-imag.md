---
source: farmer/huggingface
farmed: 2026-05-16T03:36:10Z
arxiv_id: "2605.15193"
url: "https://huggingface.co/papers/2605.15193"
arxiv_url: "https://arxiv.org/abs/2605.15193"
date: 2026-05-16
---

# Aligning Latent Geometry for Spherical Flow Matching in Image Generation

Latent flow matching for image generation usually transports Gaussian noise to variational autoencoder latents along linear paths. Both endpoints, however, concentrate in thin spherical shells, and a Euclidean chord leaves those shells even when preprocessing aligns their radii. By decomposing each latent token into radial and angular components, we show through component-swap probes that decoded perceptual and semantic content is carried predominantly by direction, with radius contributing much less. We therefore project data latents onto a fixed token radius, use the radial projection of Gaussian noise as the spherical prior, finetune the decoder with the encoder frozen, and replace linear interpolation with spherical linear interpolation. The resulting geodesic paths stay on the sphere at every timestep, and their velocity targets are purely angular by construction. Under matched training, the method consistently improves class-conditional ImageNet-256 FID across different image tokenizers, leaves the diffusion architecture unchanged, and requires no auxiliary encoder or representation-alignment objective.
