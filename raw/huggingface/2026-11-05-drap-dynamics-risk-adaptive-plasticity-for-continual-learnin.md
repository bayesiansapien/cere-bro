---
source: farmer/huggingface
farmed: 2026-11-06T05:50:41.308204+00:00
arxiv_id: 2611.05029
url: https://huggingface.co/papers/2611.05029
arxiv_url: https://arxiv.org/abs/2611.05029
date: 2026-11-05
---

# DRAP: Dynamics-Risk Adaptive Plasticity for Continual Learning in Physical AI

Continual learning in physical AI differs from conventional continual learning because small per-step policy errors can accumulate over a trajectory. Each deviation may move the agent outside the training distribution, increase subsequent prediction errors, and ultimately cause closed-loop task failure. This work introduces Dynamics-Risk Adaptive Plasticity (DRAP), a replay-free method that estimates the historical importance of adaptable model tensors from sample-level action gradients weighted by local trajectory-amplification risk. A ridge-regularized local linear model is fitted to expert state-action transitions, and the largest singular value of its state-transition matrix provides a policy-independent, Lyapunov-inspired estimate of one-step perturbation amplification. After each task, risk-weighted squared gradients are accumulated in a tensor-level importance memory. During subsequent tasks, DRAP uses normalized cumulative importance to scale the effective AdamW learning rate of each tensor, immediately reducing the plasticity of components that supported previous behavior at dynamically sensitive trajectory points. We instantiate DRAP on a fixed KappaTune-selected subnetwork of OpenVLA and evaluate replay-free sequential adaptation across the LIBERO Spatial, Object, and Goal suites. Compared with standard AdamW fine-tuning and EWC, the results show substantially improved retention of previously learned behaviors while preserving strong new-suite acquisition.
