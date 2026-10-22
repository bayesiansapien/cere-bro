---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.647011
arxiv_id: 2610.28074
url: https://huggingface.co/papers/2610.28074
arxiv_url: https://arxiv.org/abs/2610.28074
date: 2026-10-21
---

# Slot-JEPA: Object-Structured Prediction Interfaces for Latent World Models

As a prototypical latent world model, Joint-Embedding Predictive Architectures (JEPAs) provide strong semantic representations. However, dense patch representations expose a redundant interface to downstream predictors, which must implicitly infer spatial organization and temporal correspondence, presenting three challenges. First, object information is distributed across patches, forcing each downstream predictor to redundantly recover object structure that could otherwise be reused across tasks before modeling interactions. Second, the lack of explicit entity correspondence across time makes historical transitions expensive, restricting the predictor's flexibility in utilizing context. Third, without explicit transport structure, existing JEPA models typically use pointwise l1/l2 distances, which are insensitive to spatial displacement when predicted and goal supports are largely disjoint. We propose the Slot-based Joint-Embedding Predictive Architecture (Slot-JEPA), which decomposes dense representations into stable semantic slots and time-varying spatial masks. Pretrained once and frozen downstream, this decomposition exposes a reusable object-structured interface. Building on it, our Transition Memory Predictor (TMP) stores visual transitions as compact masks and retrieves useful context using statistics of corresponding slots. Its two branches separate slot-specific dynamics from shared cross-slot dynamics. We further use Unbalanced Optimal Transport (UOT) to supervise mask prediction and evaluate candidate plans by transporting mass between aligned predicted and goal masks, providing a signal better aligned with spatial progress. Across seven visual-understanding benchmarks, the slot-reconstructed features remain transferable. Slot-JEPA also improves goal-conditioned planning across six planar environments and four robotic arm planning tasks on the REALM-JEPA benchmark.
