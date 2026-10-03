---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.819228+00:00
arxiv_id: 2610.02160
url: https://huggingface.co/papers/2610.02160
arxiv_url: https://arxiv.org/abs/2610.02160
date: 2026-10-02
---

# 4Director: Controlling Video World Models with Rigid 3D Geometry

Precise control over camera and object motion is essential for professional video production. Existing methods control objects only coarsely, through image-plane cues that are ambiguous in depth and rotation or through 3D tracks and blobs that lack complete geometry and lose consistency across viewpoint changes. We introduce 4Director, a video world model conditioned on an explicit 4D scene representation: each object is reconstructed once from the input image as a canonical mesh and moved by one prescribed rigid transformation per frame. This representation provides an intuitive 3D control interface and prevents unobserved geometry from being regenerated independently in every frame. We render the controlled scene as a depth video and introduce a Motion Adapter that transforms this geometric scaffold into video while synthesizing view-consistent appearance, illumination, and non-rigid dynamics. For training, we construct RealCOD-Rigid, a new dataset of 20,774 clips annotated with rigid 3D scenes by our automatic pipeline. We further introduce Identity-Gated IoU (IG-IoU), which jointly evaluates adherence to prescribed object motion and preservation of object identity. Experiments demonstrate that 4Director consistently outperforms prior methods in visual quality and in camera and object control.
