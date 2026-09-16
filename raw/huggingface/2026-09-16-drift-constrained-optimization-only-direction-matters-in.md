---
source: farmer/huggingface
farmed: 2026-09-16T13:11:10.933414
arxiv_id: 2609.13680
url: https://huggingface.co/papers/2609.13680
arxiv_url: https://arxiv.org/abs/2609.13680
date: 2026-09-16
---

# Drift-Constrained Optimization: Only Direction Matters in Fine-Tuning Instruct Models

Fine-tuning instruct models often improves target performance while inducing behavioral drift from the reference model, which can degrade existing capabilities. Rather than treating this drift as an uncontrolled consequence of optimization, we specify a behavioral drift budget before optimization and ask how to boost the target-task performance within it. Locally, behavioral drift induces a shared geometry anchored at the reference model, with the drift budget defining a boundary within this space. In this space, drift determines distance from the reference, leaving update direction as the remaining degree of freedom. Fine-tuning updates can therefore be compared through their directional efficiency, naturally reformulating fine-tuning as a direction-selection problem. This reformulation makes a concrete prediction: changing the accessible directions can qualitatively alter the outcome of fine-tuning. We test this prediction in a stringent QA-only setting, where strong instruct models are fine-tuned only on final answers but must still generate multi-step reasoning at inference. Despite this mismatch, a coarse layer-selective probe reverses the failure of QA-only fine-tuning and reveals the existence of effective directions, with multiple neighboring configurations improving target performance while preserving reasoning and general capabilities. Across Qwen3-8B and Qwen3-14B, these directions substantially improve scientific reasoning and multilingual translation. Over more than 100 languages, the resulting models match or outperform dedicated translation systems and provide a stronger initialization for subsequent reinforcement learning. Our results suggest that fine-tuning is not just about how much a model changes, but how that change is spent. https://github.com/CONE-MT/DCO and https://huggingface.co/collections/LLaMAX/dco
