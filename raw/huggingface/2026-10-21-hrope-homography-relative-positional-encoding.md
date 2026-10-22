---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.647189
arxiv_id: 2610.28284
url: https://huggingface.co/papers/2610.28284
arxiv_url: https://arxiv.org/abs/2610.28284
date: 2026-10-21
---

# HRoPE: Homography Relative Positional Encoding

Geometric Relative Positional Encoding has become the primary mechanism for injecting spatial inductive biases into multi-view transformers. Existing designs condition attention on camera-level frustums or ray-marched depth, associating cross-view tokens through the sensor geometry. Such sensor-centric formulations, however, describe only where a token is observed from, leaving the rich surface geometry of the scene region depicted by the token. In this paper, we advocate a shift toward surface-aware positional encoding that explicitly grounds patch tokens in the geometry of physical surfaces. We introduce HRoPE, which represents the local geometry of each patch as a slanted 3D plane, following the slanted support-window assumption of classical multi-view stereo. We inject token-level, plane-induced homographies into attention as relative transformations. This equips the transformer with a geometric prior for rectifying perspective distortions and aligning patch features across viewpoints. Our encoding requires no ground-truth geometry: the plane parameters can be predicted end-to-end under a view-synthesis objective alone, or derived from foundation models. Extensive experiments on RealEstate10K, CO3Dv2, and DL3DV show that our best variant of HRoPE consistently outperforms the evaluated geometric positional encodings for novel view synthesis. Extensive ablations and analysis show the effectiveness of the proposed encoding. Please refer to our project page at: https://gaohchen.github.io/HRoPE
