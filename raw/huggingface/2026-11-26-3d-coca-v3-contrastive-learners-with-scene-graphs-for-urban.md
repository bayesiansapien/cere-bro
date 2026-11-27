---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.910134+00:00
arxiv_id: 2611.33835
url: https://huggingface.co/papers/2611.33835
arxiv_url: https://arxiv.org/abs/2611.33835
date: 2026-11-26
---

# 3D CoCa v3: Contrastive Learners with Scene Graphs for Urban Scene Understanding

Understanding large-scale 3D urban scenes requires representations that capture both multi-scale geometric structures and complex spatial relationships. However, existing 3D vision-language methods primarily emphasize global semantic alignment or object-level representations, leaving structured relational modeling underexplored within unified contrastive and generative frameworks. In this paper, we present 3D CoCa v3, a scene-graph-enhanced contrastive and generative framework for urban 3D scene understanding. Our framework features a Pyramid Vision Encoder for multi-scale geometric representation learning and a language-model-based decoder with question-guided caption retrieval and visual cross-attention. We further introduce MSG-based relational descriptions to enrich contrastive 3D-language alignment with structured spatial relationships. To support semantic and relational supervision, we construct City3D-9.6K, a multi-view urban vision-language dataset with aligned visual-geometric observations, scene captions, and scene graphs. Extensive experiments on City-3DQA demonstrate that 3D CoCa v3 achieves 88.35% and 64.79% overall top-1 accuracy on the sentence-wise and city-wise splits, surpassing 3D CoCa v2 by 20.88 and 3.57 percentage points, respectively. Furthermore, 3D CoCa v3 achieves the best performance on GeoEval3D, demonstrating its effectiveness in urban spatial reasoning and geometric understanding. Code is available at https://github.com/AIGeeksGroup/3DCoCav3.
