---
source: farmer/huggingface
farmed: 2026-05-12T00:00:00Z
arxiv_id: 2509.24244
url: https://huggingface.co/papers/2509.24244
arxiv_url: https://arxiv.org/abs/2509.24244
date: 2026-05-12
---

# Model Merging Scaling Laws in Large Language Models

We study empirical scaling laws for language model merging measured by cross-entropy. Despite its wide practical use, merging lacks a quantitative rule that predicts returns as we add experts or scale the model size. We identify a compact power law that links model size and expert number: the size-dependent floor decreases with model capacity, while the merging tail exhibits clear diminishing returns in the number of experts. The law holds in-domain and cross-domain, tightly fits measured curves across diverse architectures and methods (Average, TA, TIES, DARE), and explains two robust regularities: most gains arrive early, and variability shrinks as more experts are included. Building on this, we present a simple theory that explains why gains fall roughly as 1/k and links the floor and tail to properties of the base model and the diversity across domains. This law enables predictive planning: estimating how many experts are needed to reach a target loss, deciding when to stop adding experts, and trading off scaling the base model versus adding experts under a fixed budget. These results make merging a predictable, budget-aware alternative to multitask fine-tuning.
