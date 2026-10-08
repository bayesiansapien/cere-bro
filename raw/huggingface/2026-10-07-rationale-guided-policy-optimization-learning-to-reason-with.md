---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.07342
url: https://huggingface.co/papers/2610.07342
arxiv_url: https://arxiv.org/abs/2610.07342
date: 2026-10-07
---

# Rationale-Guided Policy Optimization: Learning to Reason with Adaptive Rationale Scaffolding

On-policy reinforcement learning has become a central paradigm for improving the reasoning abilities of large language models. However, its effectiveness is often limited by reward sparsity: when a model fails to discover correct trajectories for difficult problems, the optimization process receives little useful signal and may stagnate. Existing approaches mitigate this issue by incorporating off-policy demonstrations, expert traces, or model-generated solutions, but they typically require the auxiliary data to match the format of the reinforcement-learning task, often relying on rejection sampling from stronger models to obtain suitable training trajectories. We introduce Rationale-Guided Policy Optimization (RGPO), a framework that adaptively leverages ground-truth rationale information according to the model's current capability while preserving its freedom to explore. Rather than treating reference solutions as fixed imitation targets, RGPO uses them as temporary scaffolds: rationales help the model generate improved responses, after which only higher-reward, model-generated solutions are transferred back to the original unguided setting. This design allows training to exploit available ground-truth information without requiring off-policy data to follow the same format as the RL task. Across both language-only and vision-language reasoning settings, RGPO consistently improves performance over RLVR baselines, and ablation studies show that adaptive rationale guidance is a key contributor to these gains. These results suggest that RGPO offers a practical and general approach for reducing reward sparsity, stabilizing reinforcement learning, and improving reasoning performance in both text-only and multimodal models.
