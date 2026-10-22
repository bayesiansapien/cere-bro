---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.23600
url: https://huggingface.co/papers/2610.23600
arxiv_url: https://arxiv.org/abs/2610.23600
date: 2026-10-20
---

# Learning to Discriminate Scene Structures Makes Self-Supervised Depth Learning Scalable

Self-supervised monocular depth estimation is appealing for its potential to scale with unlabeled data, yet existing methods often degrade when trained on diverse scenes. This study finds that, under self-supervision, models tend to encode dataset-specific structural biases rather than transferable scene geometry, leading to cross-domain optimization conflicts. To address this issue, this study proposes the MaSS framework, aiming to make self-supervised depth learning scalable to diverse data. MaSS introduces a dedicated structural representation pathway explicitly decoupled from contextual features, which is guided by a novel scene-structure discrimination objective to learn generalized, layout-aware structural representations for depth decoding. Trained and evaluated on four diverse datasets, both individually and jointly, MaSS substantially outperforms prior self-supervised methods and is the first to consistently benefit from mixed-domain training. Zero-shot evaluation on eight additional datasets further demonstrates its remarkable generalizability, particularly on those entirely out-of-distribution scenes. The source code is publicly available at https://mias.group/MaSS.
