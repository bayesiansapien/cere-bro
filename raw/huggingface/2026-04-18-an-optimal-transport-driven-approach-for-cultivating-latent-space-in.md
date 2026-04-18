---
source: farmer/huggingface
farmed: 2026-04-18T00:00:00Z
arxiv_id: 2211.16780
url: https://huggingface.co/papers/2211.16780
arxiv_url: https://arxiv.org/abs/2211.16780
date: 2026-04-18
---

# An Optimal Transport-driven Approach for Cultivating Latent Space in Online Incremental Learning

In online incremental learning, data continuously arrives with substantial shifts in distribution, creating a significant challenge since previous samples have limited replay when learning a new task. Prior research has typically relied on either a single adaptive centroid or fixed multiple centroids to represent each class in the latent space. However, such methods struggle when class data streams are inherently multimodal and require continual centroid updates. To overcome this, we introduce an online Mixture Model learning framework grounded in Optimal Transport theory (MMOT), where centroids evolve incrementally with new data. This approach offers two main advantages: (i) it provides a more precise characterization of complex data streams, and (ii) it enables improved class similarity estimation for unseen samples during inference through MMOT-derived centroids. Furthermore, to strengthen representation learning and mitigate catastrophic forgetting, we design a Dynamic Preservation strategy that regulates the latent space and maintains class separability over time. Experimental evaluations on benchmark datasets confirm the superior effectiveness of our proposed method.
