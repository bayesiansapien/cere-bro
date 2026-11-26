---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.30963
url: https://huggingface.co/papers/2611.30963
arxiv_url: https://arxiv.org/abs/2611.30963
date: 2026-11-25
---

# Foresight Forcing: Learning Spatial Foresight for Robotic Manipulation

Robotic manipulation policies can improve action prediction by anticipating how objects move and how their spatial relationships change. World Action Models (WAMs) learn to predict future visual observations, but their training objectives typically leave the underlying 3D geometric transitions implicit. To alleviate this problem, we introduce Foresight Forcing (F^{2}), a WAM that learns a spatial transition representation from changes in a pretrained 3D feature space. During training, a frozen 3D foundation model extracts patch-wise feature differences from aligned current and future observations that provide dense supervision for geometry-aware feature transitions. We distill these targets into spatial transition queries, which are progressively refined from the current observation, language instruction, and proprioceptive state, and use them alongside current visual features to generate actions. At deployment, the policy predicts the queries without future observations or the 3D teacher. Experiments on LIBERO, LIBERO-Plus, and RoboTwin2.0 demonstrate strong manipulation performance and improved robustness, including 95.01% average success on RoboTwin2.0 Full. On six real-world manipulation tasks, F^{2} achieves a mean task score of 85.8%.
