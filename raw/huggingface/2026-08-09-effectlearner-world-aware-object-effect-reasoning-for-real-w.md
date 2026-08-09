---
source: farmer/huggingface
farmed: 2026-08-09T07:10:01.249497+00:00
arxiv_id: 2608.05565
url: https://huggingface.co/papers/2608.05565
arxiv_url: https://arxiv.org/abs/2608.05565
date: 2026-08-09
---

# EffectLearner: World-Aware Object-Effect Reasoning for Real-World Video Object Removal

Video object removal must eliminate not only the target object but also its induced effects while maintaining high-fidelity and spatiotemporally coherent restoration. Existing methods mainly learn object-effect correspondences implicitly from predefined effect categories and fixed data distributions, limiting their generalization to complex real-world scenes involving compositional effects, spatially detached or weakly correlated effects, long-tail physical phenomena, and dynamically evolving interactions. We propose EffectLearner, a semantic-reasoning-enhanced framework that combines a VLM-based Object-Effect Reasoner with a DiT-based Video Eraser. Guided by a structured effect-analysis prompt, the Reasoner performs cross-modal reasoning over a target-highlighted video and extracts compact effect-aware context, which guides the Video Eraser toward comprehensive object-effect removal. Motion-aware mask guidance and motion-consistency supervision further improve removal coverage and spatiotemporal stability under object motion and evolving scene dynamics. To fully exploit the framework in challenging real-world scenarios, we further construct EffectWorld, a paired video dataset specifically designed for complex object-induced effects, and introduce a progressive training curriculum that combines common supervision with complex-effect data. On the standard ROSE-Bench, EffectLearner outperforms existing baselines on most metrics and achieves clear advantages on both EffectWorld-Eval and the challenging EffectWorld-Wild, demonstrating its ability to deliver high-quality video object removal in complex real-world scenes.
