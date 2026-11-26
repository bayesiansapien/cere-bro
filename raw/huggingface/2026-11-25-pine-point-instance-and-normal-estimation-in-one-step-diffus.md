---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.29389
url: https://huggingface.co/papers/2611.29389
arxiv_url: https://arxiv.org/abs/2611.29389
date: 2026-11-25
---

# PINE: Point, Instance and Normal Estimation in One-Step Diffusion Model

Understanding a scene requires both geometry and semantics: geometry recovers its spatial structure, and semantics separates it into objects. Current models obtain the two from separate networks or separate passes. We present PINE, a one-step Omni Diffusion Transformer that predicts the point map, the surface normals, and the instance map of an image in one forward pass. PINE treats each map as a token stream, and a stream mask decides which streams interact. A camera-aware ray encoding positions every token by its camera ray rather than its pixel. Grounding attention adds the affinity of pretrained DINOv3 features to the attention logits. Trained on only 139K synthetic images for geometry, PINE achieves state-of-the-art point maps whether or not intrinsics are given and the best average rank on surface normals. It also exceeds SAM on large objects with less than 1 percent of its training images, and it predicts all three maps 5.7x faster than MoGe-3 with SAM.
