---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.145053+00:00
arxiv_id: 2611.24941
url: https://huggingface.co/papers/2611.24941
arxiv_url: https://arxiv.org/abs/2611.24941
date: 2026-11-19
---

# UltraTex: Aligning Physical Knowledge for High-Fidelity PBR Texture Generation

Generating physically based rendering (PBR) texture maps for a 3D mesh from a single reference image is highly ambiguous, as the observed appearance entangles material identity, surface reflectance, and illumination. While current generative methods produce realistic albedo maps, they still struggle to infer accurate metallic and roughness attributes for relighting. We present UltraTex, a cascaded multi-view framework that moves beyond appearance matching by integrating physical knowledge into multi-view diffusion-based PBR generation. UltraTex first jointly predicts albedo and world-space shading normals to generate more detailed albedo maps, and then predicts metallic-roughness (MR) maps conditioned on the generated albedo, reference image, and material semantic priors. To inject material semantics, a lightweight adapter transforms hidden-layer features of a vision-language model (VLM) into intrinsic material representation tokens, providing part-level knowledge anchors for MR estimation. To model material-light interaction, photometric representation alignment guides intermediate diffusion features toward ground-truth material renderings under controlled lighting. This makes metallic and roughness variations observable through highlight intensity, specular sharpness, and local reflectance contrast, providing stronger guidance for fine-grained material prediction without explicit lighting supervision. Extensive experiments show that UltraTex generates high-quality textures and outperforms existing open-source and commercial methods in visual fidelity, material accuracy, and physical plausibility.
