---
source: farmer/huggingface
farmed: 2026-06-09T16:28:21
arxiv_id: 2606.04662
url: https://huggingface.co/papers/2606.04662
arxiv_url: https://arxiv.org/abs/2606.04662
date: 2026-06-09
---

# Why Muon Outperforms Adam: A Curvature Perspective

Muon improves training efficiency over Adam in large language-model training by about two times, but the local geometric source of this advantage remains unclear. Our work takes a first step toward demystifying Muon's superiority over Adam from a curvature perspective. First, we apply a second-order Taylor approximation to the training landscape and show that Muon achieves a larger one-step loss decrease than Adam at matched validation loss. The two optimizers have comparable first-order gains, but Muon consistently incurs a smaller second-order curvature penalty. Second, we decompose this curvature penalty into the squared update norm and Normalized Directional Sharpness (NDS). We find that Muon and Adam have comparable update norms, so Muon's smaller curvature penalty is driven by lower NDS, not update scale. Third, we study how training data and model structure shape Muon's NDS advantage. Using Zipf-Probabilistic Context-Free Grammar (PCFG) data with controlled imbalance, we show that data imbalance amplifies Muon's NDS advantage over Adam. A within-/cross-layer decomposition further shows that, in the middle and late stages of training, Muon's lower NDS is mainly sustained by smaller within-layer curvature. Beyond empirical evidence, we analyze stylized quadratic problems with heterogeneous curvature and gradient alignment toward high-curvature modes. We prove that Muon attains a smaller average NDS than GD by balancing update energy across curvature groups; when curvature heterogeneity is sufficiently strong, this also yields lower local quadratic loss after the same number of steps.
