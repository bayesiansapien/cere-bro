---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.645836
arxiv_id: 2610.07609
url: https://huggingface.co/papers/2610.07609
arxiv_url: https://arxiv.org/abs/2610.07609
date: 2026-10-21
---

# PhysLDM: Latent Diffusion for High-Fidelity Deformable Simulation

Neural simulation of high-fidelity deformable bodies is a foundational challenge in computer graphics and physical AI. Long-horizon prediction for high-resolution 3D volumetric meshes is hard: autoregressive methods are prone to error accumulation, while direct multi-frame prediction at native resolution is computationally prohibitive. This motivates a compact spatiotemporal latent representation, which is largely unexplored for mesh-based volumetric physics. Meanwhile, it remains unclear whether deterministic regression or generative diffusion is the more suitable predictive paradigm. To address these coupled challenges, we introduce PhysLDM, a unified latent-diffusion paradigm for one-shot deformable simulation. Its core is a holistic spatiotemporal VAE that avoids the "staircase" artifacts of standard temporal compression (e.g., video VAEs), achieving ~2.48 mm reconstruction precision on meter-scale scenes at up to 78x token compression. Based on this reliable latent space, we systematically compare regression and diffusion methods. Our experiments uncover a key modeling insight: complex deformable dynamics are often chaotic, and in this regime deterministic regression tends to produce non-physical averages, whereas diffusion better models their distribution. Accordingly, we employ a latent diffusion model that effectively learns from chaotic data to generate physically plausible trajectories. Trained purely kinematically on an Objaverse-scale dataset, a single PhysLDM generalizes zero-shot to unseen OOD datasets. Its differentiability further enables efficient solution of inverse problems and higher-order design optimization. To our knowledge, PhysLDM is the first high-fidelity spatiotemporal autoencoder and latent-diffusion paradigm for volumetric deformable dynamics, offering a scalable and robust approach to neural simulation. Project Page: https://yucrazing.github.io/physldm/
