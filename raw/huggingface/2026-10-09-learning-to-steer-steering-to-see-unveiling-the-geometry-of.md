---
source: farmer/huggingface
farmed: 2026-10-10T05:09:51.420344+00:00
arxiv_id: 2609.34344
url: https://huggingface.co/papers/2609.34344
arxiv_url: https://arxiv.org/abs/2609.34344
date: 2026-10-09
---

# Learning to Steer, Steering to See: Unveiling the Geometry of RLVR in Large Language Models via Trainable Vectors

Reinforcement learning (RL) has become a key paradigm for enhancing the reasoning of large language models, yet the high dimensionality of parameter updates makes its training dynamics hard to analyze. We study reinforcement learning with verifiable rewards (RLVR) and use vector steering to identify a low-dimensional effective manifold in activation space associated with RL-induced gains. We uncover two geometric properties. (1) Effective Manifold Capacity: the capacity needed to reproduce RL gains can be very small but is not infinitely compressible; at extremely low capacity, intervention dimensionality and input-dependent expressiveness become key constraints, and this requirement varies with injection depth. (2) Control Manifold Separation: effective control directions lie mainly in the low-variance complement of the activation principal subspace. Within a task and base model, the learned geometry stays largely consistent across training configurations, and across tasks geometric alignment correlates with capability transfer. Experiments on 5 LLMs and 6 verifiable-reward tasks support these findings. We then propose Alpha-Stabler, a plug-and-play framework with a Predictor that monitors principal-subspace intrusion for early collapse warnings, and a Controller that removes the principal-subspace component of activation gradients during backpropagation while preserving the orthogonal complement. Alpha-Stabler stabilizes training for 2,000 steps and consistently improves RL gains, offering practical insights for robust post-training. Code: https://github.com/caiyuchen-ustc/On_Policy_Vector_Training
