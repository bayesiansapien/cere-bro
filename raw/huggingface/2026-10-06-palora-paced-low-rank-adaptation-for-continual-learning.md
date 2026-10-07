---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.04226
url: https://huggingface.co/papers/2610.04226
arxiv_url: https://arxiv.org/abs/2610.04226
date: 2026-10-06
---

# PaLoRA: Paced Low-Rank Adaptation for Continual Learning

LoRA-based continual learning methods mitigate catastrophic forgetting through various mechanisms, yet nearly all complement these with small learning rates as a heuristic to restrict gradient scaling magnitude. Such fixed heuristics lack theoretical guidance on how the strength of this restriction should evolve as tasks accumulate. We reveal that even under directional constraints such as nullspace projection, finite-precision updates inevitably leak into the subspace of accumulated prior knowledge along multiple directions. While small learning rates attenuate such leakage, they cannot prevent the accumulated forgetting from intensifying as the effective rank of historical knowledge grows. We show that the optimal magnitude restriction should adaptively increase with this effective rank to balance stability and plasticity, i.e., preservation of previous knowledge and acquisition of new task information. Under an anisotropic leakage model, we derive a pacing law s^*=R/c that characterizes the optimal scaling of gradient steps, i.e., the magnitude restriction itself, where R is the effective rank of past updates. Based on this insight, we propose PaLoRA, which compresses historical knowledge via adaptive SVD truncation, projects gradients onto the nullspace of prior tasks, and applies rank-aware adaptive pacing. Experiments demonstrate consistent improvements over prior methods, with particularly strong performance in long-horizon settings, achieving substantial gains of 4% accuracy on challenging 50-task ImageNet-A and ImageNet-R benchmarks.
