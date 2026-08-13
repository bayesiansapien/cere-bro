---
source: farmer/huggingface
farmed: 2026-08-13T03:36:17.258300+00:00
arxiv_id: 2608.11562
url: https://huggingface.co/papers/2608.11562
arxiv_url: https://arxiv.org/abs/2608.11562
date: 2026-08-13
---

# From Synthesis to Removal: Physics-Grounded Reflection Simulation and Diffusion-Based Video Dereflection

Videos captured through glass often contain reflections that degrade visual quality and interfere with downstream vision tasks. Although single-image reflection removal has been extensively studied, video reflection removal remains largely underexplored due to the lack of paired video data, temporally coherent removal models, and dedicated evaluation benchmarks. We present a closed-loop framework that unifies physics-grounded reflection simulation, diffusion-based video dereflection, and benchmark evaluation. Our S2R-Synthesis pipeline generates paired reflected and reflection-free videos by performing physics-grounded augmentation in the structure space and rendering realistic reflected videos with a trained video diffusion renderer; the augmentation models key glass-related effects including roughness-induced blur, thickness-induced ghosting, and reflectance variation. Based on the synthesized data, we introduce S2R-Removal, the first diffusion-based video reflection removal model, which adapts a pretrained video diffusion prior through reflection-aware latent adaptation and one-step pixel-geometric refinement, recovering the clean transmission in a single denoising step. We further build S2R-Bench, the first benchmark for video reflection removal, supporting both full-reference evaluation and real-world human perceptual assessment. Experiments on S2R-Bench and multiple public image benchmarks demonstrate state-of-the-art performance and faster inference than even non-diffusion baselines, and validate the effectiveness of S2R-Synthesis. Project page: https://codingwzp.github.io/VideoDereflection_S2R.
