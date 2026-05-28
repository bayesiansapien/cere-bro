---
source: farmer/huggingface
farmed: 2026-05-28T03:40:35Z
arxiv_id: 2605.27762
url: https://huggingface.co/papers/2605.27762
arxiv_url: https://arxiv.org/abs/2605.27762
date: 2026-05-28
---

# PEAM: Parametric Embodied Agent Memory through Contrastive Internalization of Experience in Minecraft

We present PEAM, a Parametric Embodied Agent Memory framework in Minecraft that transforms agent memory from inference-time retrieval into parameter-resident skills internalized through experience. PEAM pairs a slow deliberative LLM for open-ended reasoning with a fast parametric module for reflexive execution of consolidated skills. The fast module is a multimodal Mixture-of-Experts LoRA architecture with per-category physically isolated adapters, enabling parameter-level continual learning without catastrophic forgetting. We treat failure as a first-class training signal: failure--correction trajectory pairs are internalized through a joint behavioral-cloning and contrastive objective, so the agent learns not only what succeeds but also how corrected actions differ from failed ones. To govern consolidation, PEAM introduces a parameterization-worthiness score for deciding which experience should be internalized, and a scale-free self-triggered consolidation mechanism for deciding when to internalize without task-specific hand-tuned thresholds, making the agent self-evolving as the trigger transfers across task distributions without re-tuning. Experiments in Minecraft show that PEAM improves long-horizon task performance, mitigates forgetting on previously consolidated skills, and improves parametric-versus-retrieval efficiency over retrieval-based embodied agents and parametric memory variants.
