---
source: farmer/huggingface
farmed: 2026-04-30T00:00:00
arxiv_id: 2604.19835
url: https://huggingface.co/papers/2604.19835
arxiv_url: https://arxiv.org/abs/2604.19835
date: 2026-04-23
upvotes: 18
---

# Expert Upcycling: Shifting the Compute-Efficient Frontier of Mixture-of-Experts

Mixture-of-Experts (MoE) has become the dominant architecture for scaling large language models: frontier models routinely decouple total parameters from per-token computation through sparse expert routing. Scaling laws show that under fixed active computation, model quality scales predictably with total parameters, and MoEs realize this by increasing expert count. However, training large MoEs is expensive, as memory requirements and inter-device communication both scale with total parameter count.

Expert upcycling is a method for progressively expanding MoE capacity by increasing the number of experts during continued pre-training (CPT). Given a trained E-expert model, the upcycling operator constructs an mE-expert model through expert duplication and router extension while holding top-K routing fixed, preserving per-token inference cost. Duplication provides a warm initialization: the expanded model inherits the source checkpoint's learned representations, starting from a substantially lower loss than random initialization. Subsequent CPT then breaks the symmetry among duplicated experts to drive specialization.

Introduces utility-based expert selection, which uses gradient-based importance scores to guide non-uniform duplication, more than tripling gap closure when CPT is limited. In 7B→13B total parameter experiments, the upcycled model matches the fixed-size baseline on validation loss while saving ~32% of GPU hours. Amazon Stores Foundation AI.
