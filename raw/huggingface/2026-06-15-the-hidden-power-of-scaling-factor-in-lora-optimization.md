---
source: farmer/huggingface
farmed: 2026-06-15T06:21:28Z
arxiv_id: 2606.12883
url: https://huggingface.co/papers/2606.12883
arxiv_url: https://arxiv.org/abs/2606.12883
date: 2026-06-15
---

# The Hidden Power of Scaling Factor in LoRA Optimization

In Low-Rank Adaptation (LoRA), the scaling factor alpha is often treated as a mere complement to the learning rate, yet its role in optimization remains poorly understood. In this paper, we reveal that the scaling factor alpha and the learning rate function differently, with alpha emerging as the dominant driver of effective optimization, delivering gains that cannot be replicated by learning rate scaling alone. Through the synergy of extensive empirical analysis and a theoretical Signal-Drift framework, we uncover three findings into LoRA's scaling mechanism: First, LoRA's spectral suppression smooths the optimization landscape, rendering standard hyperparameters overly conservative and creating an optimization gap. Second, when leveraging this smoothness to accelerate convergence, alpha outperforms the learning rate by amplifying the task signal without increasing the drift ratio. Third, the optimal scaling factor follows a sublinear relationship with the rank, well characterized by a square-root law with an unexpectedly large coefficient, revealing the insufficient scaling of existing rank-tied heuristics. Based on these insights, we propose LoRA-alpha, a minimalist framework that restores alpha to its principled regime, making LoRA compatible with standard small learning rates. Extensive evaluations across diverse tasks demonstrate that LoRA-alpha consistently improves performance while streamlining hyperparameter search, unleashing the learning potential of LoRA.
