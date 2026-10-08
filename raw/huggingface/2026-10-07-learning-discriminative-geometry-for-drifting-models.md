---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.04703
url: https://huggingface.co/papers/2610.04703
arxiv_url: https://arxiv.org/abs/2610.04703
date: 2026-10-07
---

# Learning Discriminative Geometry for Drifting Models

Recently proposed Drifting Models shift iterative distribution refinement from inference to training, enabling effective one-step generation. However, their performance on complex image datasets depends strongly on the representation used to construct the drifting field: pixel-space drifting performs poorly, whereas pretrained feature spaces substantially improve sample quality for reasons that remain unclear. We trace this gap to the discriminative geometry of the representation, which determines sample weighting in kernel density estimation (KDE) and, consequently drift. We introduce persistent representation learning, which continuously learns a more discriminative representation geometry as the generator evolves across batches. We further establish a current-step gradient equivalence between the KDE ratio loss and drift regression loss under matched conditions, connecting density-ratio-based generator optimization to empirical drifting and motivating direct control of the drifting velocity. Across multiple datasets, our method learns effective discriminative representations directly from pixels and reduces FID by approximately 82-95% over the original pixel-space Drifting Models, without pretrained encoders. Adapting pretrained representations and applying velocity clipping provide further gains.
