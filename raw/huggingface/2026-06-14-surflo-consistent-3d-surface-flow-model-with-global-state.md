---
source: farmer/huggingface
farmed: 2026-06-14T07:38:18Z
arxiv_id: 2606.13644
url: https://huggingface.co/papers/2606.13644
arxiv_url: https://arxiv.org/abs/2606.13644
date: 2026-06-14
---

# Surflo: Consistent 3D Surface Flow Model with Global State

Geometry is invariant to viewpoint, which makes any collection of images a redundant encoding of a single 3D state. Existing feed-forward reconstruction models fail to exploit this: per-view methods emit overlapping, unaligned pointmaps that grow linearly with input count, while global-latent methods commit to a fixed, low-resolution output. We introduce Surflo, which compresses a variable number of unposed RGB views into K latent tokens-one global state-and decodes oriented 3D surface points by independently transporting them from noise onto the surface via flow matching. This frees the output from any fixed grid or token budget: the same latent yields from a few thousand to a million points in a single forward pass. To suppress the local inconsistencies inherent to independent per-point decoding, an inference-time guidance term correlates nearby points by injecting a photometric gradient during ODE integration. Surflo matches or surpasses feed-forward baselines on surface metrics, runs an order of magnitude faster than optimization-based methods that require hundreds of views, and is the only feed-forward approach to combine a global latent with arbitrary-resolution decoding.
