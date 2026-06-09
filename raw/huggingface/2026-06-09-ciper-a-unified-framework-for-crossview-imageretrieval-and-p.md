---
source: farmer/huggingface
farmed: 2026-06-09T11:13:01Z
arxiv_id: 2606.05011
url: https://huggingface.co/papers/2606.05011
arxiv_url: https://arxiv.org/abs/2606.05011
date: 2026-06-09
---

# CIPER: A Unified Framework for Cross-view Image-retrieval and Pose-estimation

Cross-view geo-localization estimates the geographic location of a ground image by matching it against an aerial image database. Existing methods tackle this through either large-scale retrieval or precise pose estimation, but not both: retrieval-based methods enable wide-area search at the cost of localization accuracy, while pose estimation methods achieve high precision within only a narrow search space. Naively cascading these pipelines introduces error propagation and inconsistent feature representations. We formulate cross-view geo-localization as a unified problem requiring simultaneous city-scale retrieval and precise 3-DoF pose estimation. We propose CIPER (Cross-view Image-retrieval and Pose-estimation transformER), a single architecture that jointly performs both tasks through mutually beneficial feature learning. CIPER uses a shared transformer encoder with task-specific tokens to disentangle global retrieval features from spatial localization cues. To bridge the large domain gap between ground and aerial views, we introduce a two-way transformer pose decoder that uses ground features as spatial queries for bidirectional cross-attention. A set prediction strategy further enables stable 3-DoF regression under a unified multi-task objective. Experiments on VIGOR, KITTI, and Ford Multi-AV demonstrate competitive performance, especially under limited field-of-view and arbitrary orientation conditions. Code is available at https://github.com/yurimjeon1892/CIPER.
