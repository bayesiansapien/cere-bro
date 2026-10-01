---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.37441
url: https://huggingface.co/papers/2609.37441
arxiv_url: https://arxiv.org/abs/2609.37441
date: 2026-09-30
---

# Anisotropic Representations Improve Planning in JEPA World Models

Latent world models learn action-conditioned dynamics in representation space and often score candidate actions by Euclidean distance to a goal representation. Joint training typically regularizes the representation to prevent collapse, but the resulting representation geometry also determines how terminal errors are weighted during planning. We show that accurate prediction and noncollapsed representations do not guarantee a task-aligned latent planning cost: isotropic Gaussian regularization can induce a geometry that ranks feasible outcomes differently from the task cost. To address this mismatch, we introduce AnisoWM with ΛReg, which replaces the fixed isotropic Gaussian target with a learnable diagonal covariance under fixed-trace and anisotropy constraints. The prediction objective, predictor architecture, and Euclidean planner remain unchanged; the target is used only during training. Our analysis characterizes the prediction-driven allocation of target variance, its dependence on the training distribution, and the conditions under which the induced metric reduces planning regret. Across four visual control environments, AnisoWM improves planning success over LeWorldModel in all four. Its latent planning cost also shows better agreement with task outcomes. Project website: https://rkdrn79.github.io/AnisoWM-page/
