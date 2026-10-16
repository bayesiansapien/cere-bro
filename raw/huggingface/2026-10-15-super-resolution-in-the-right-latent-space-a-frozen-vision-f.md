---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.225655+05:30
arxiv_id: 2610.04781
url: https://huggingface.co/papers/2610.04781
arxiv_url: https://arxiv.org/abs/2610.04781
date: 2026-10-15
---

# Super-Resolution in The Right Latent Space: A Frozen Vision-Foundation Substrate

In an image latent space, the embeddings of high-resolution, natural, and sharp images form a manifold. Degradation of high-resolution images pushes their embeddings off this manifold. Real-world super-resolution (SR) then becomes the task of mapping the degraded embedding back onto this manifold --- not anywhere on the manifold, but to the point that preserves what the input still carries, both its semantics and pixel details. Every published method implements this mapping in a reconstruction-oriented latent space or pixel space. We claim these spaces are the wrong substrates for SR. Low-resolution and degraded images are embedded far from the manifold, making the mapping difficult and expensive. The lack of semantic information in these substrates also makes it difficult to navigate to the faithful point on the manifold, causing severe hallucination when degradation is heavy. Thus, restoring in a suitable latent space is crucial to the SR task. We show that the latent space of 23 fused layers of a frozen DINOv3-L is one such space that makes the SR task easier. Degraded images are embedded near the manifold. Moreover, this substrate contains a hierarchy of information, from pixel record to degradation robust semantics, guiding the model to find the faithful point on the manifold. On this substrate, a 415M decoder is trained under reconstruction and adversarial objectives to map the degraded embeddings back and decode to pixel space in one pass. The resulting model, RAESR, attains the best fidelity--perception trade-off among state-of-the-art adversarial and diffusion-based restorers on RealSR, DRealSR, LSDIR and DIV2K-Val, at 37 ms per 512 by 512 image on a single H20 GPU. Swapping the substrate for a VAE latent under an identical recipe loses on every metric.
