---
source: farmer/huggingface
farmed: 2026-06-05T08:18:05.247595+00:00
arxiv_id: 2606.06477
url: https://huggingface.co/papers/2606.06477
arxiv_url: https://arxiv.org/abs/2606.06477
date: 2026-06-05
upvotes: 7
---

# Complexity-Balanced Diffusion Splitting

Standard continuous-time generative models rely on monolithic architectures that must navigate vastly different signal regimes, from isotropic noise to intricate data distributions. While scaling model capacity improves performance, deploying a massive network uniformly across the entire generative timeline is inherently inefficient. In this work, we propose Complexity-Balanced Splitting (CBS), a principled framework for temporal capacity allocation that distributes the generative workload across multiple specialized sub-networks. Grounded in function approximation theory and de Boor's equidistribution principle, CBS partitions the diffusion timeline into segments of equal approximation burden, allocating more representational capacity to regions where the generative dynamics are more difficult to model. To estimate this local complexity, we introduce two complementary and tractable monitor functions: a spatial measure based on the flow's Dirichlet energy, and a geometric measure based on the acceleration of the sampling trajectories. Using a lightweight auxiliary model to estimate these complexity profiles, our approach eliminates the need for heuristic temporal splits or computationally expensive search procedures. Extensive evaluation across multiple architectures (SiT, JiT, and UNet) and datasets demonstrates that CBS consistently improves synthesis quality without increasing per-step inference cost. In particular, CBS improves FID by ~35% on SiT-XL with CFG relative to naive temporal partitioning. Project page is available at https://noamissachar.github.io/CBS/.
