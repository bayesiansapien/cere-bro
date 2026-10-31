---
source: farmer/huggingface
farmed: 2026-10-31T08:06:35.156871+00:00
arxiv_id: 2610.40614
url: https://huggingface.co/papers/2610.40614
arxiv_url: https://arxiv.org/abs/2610.40614
date: 2026-10-30
---

# L3G-World: Real-Time Infinite World Generation with Latent 3D Gaussian Memory

Interactive world models generate visual content conditioned on user actions, yet maintaining spatial consistency over long-horizon exploration in real time remains challenging. Existing approaches rely on either temporal context or explicit 3D memory, both of which scale poorly because memory grows with the length of the generated stream. Moreover, explicit 3D memories condition latent video generators by re-encoding RGB renderings, which precludes real-time generation. In this paper, we introduce a Latent 3D Gaussian Memory (L3G) that combines the efficiency of feed-forward reconstruction with a compact, rapidly renderable scene representation. Building on this memory, we propose L3G-World, in which a memory updater and a video diffusion transformer (DiT) alternate autoregressively to generate spatially consistent worlds. The memory updater spawns Gaussians in newly observed regions and refines existing ones, so that the memory grows with scene extent rather than stream length. Each Gaussian further stores a VAE latent feature, allowing the memory to be rendered directly into the DiT's latent space without VAE re-encoding. Experiments show that L3G-World achieves state-of-the-art generation quality and long-horizon spatial consistency, with up to 38.6times fewer 3D primitives, 3.2times faster memory updates, and 359times faster memory rendering relative to the most efficient prior 3D-memory baseline for each metric, enabling real-time world generation at 9 FPS.
