---
source: farmer/huggingface
farmed: 2026-08-10T09:04:01.722687
arxiv_id: 2608.05597
url: https://huggingface.co/papers/2608.05597
arxiv_url: https://arxiv.org/abs/2608.05597
date: 2026-08-10
---

# Uncertainty-Aware World Model for Aerial Image-Goal Navigation

Aerial image-goal navigation requires an unmanned aerial vehicle (UAV) to reach a target location specified by a goal image. Existing world-model-based methods rank candidate trajectories using predicted futures, but typically rely on only one or a few point predictions, which is inadequate for large-scale outdoor environments with substantial future-state uncertainty. To address this limitation, we propose the Uncertainty-Aware Navigation World Model (UA-NWM), an efficient latent world model for aerial image-goal navigation, which formulates trajectory scoring as conditional out-of-distribution detection. UA-NWM represents plausible futures with an uncertainty subspace and decomposes the prediction--goal discrepancy into uncertainty-explainable and unexplainable components. Only the unexplainable residual is used for scoring, enabling robust selection without multiple future samples. Extensive experiments demonstrate that UA-NWM consistently outperforms existing navigation world models while maintaining low inference latency. Real-world UAV experiments further validate its practical applicability. Project page: https://duryi.github.io/UA-NWM-Project-Page
