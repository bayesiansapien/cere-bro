---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.937038+00:00
arxiv_id: 2609.34241
url: https://huggingface.co/papers/2609.34241
arxiv_url: https://arxiv.org/abs/2609.34241
date: 2026-09-29
---

# AdaGuard: An Adaptive Guard Model with User-defined Policies

Guard models support the safe deployment of language model agents, but fixed risk taxonomies limit their ability to accommodate requirements that vary across applications and tasks. Under user-defined policies, detecting violations requires interpreting both the applicable rules and the agent's behavior, since identical actions can receive different judgments under different policies. To support learning this capability, we introduce AdaptiveSafety, a dataset of 10,939 training examples and 1,000 test examples covering policies with 1--100 rules. The dataset combines trajectories from multiple sources with policy and behavioral counterfactuals, pairing each example with an explanation and the complete set of violated rules. These counterfactuals expose changes that alter compliance, while structural augmentations provide supervision for consistency under rule reordering and identifier remapping. Building on this supervision, we propose SafePO, a reinforcement learning algorithm for refining violation identification while balancing explanatory reasoning and final verdicts. SafePO uses structured rewards to assess prediction correctness, retains group-relative advantages at the response level, and employs a separately trained value model to modulate token weights within explanation and verdict regions. Separate normalization controls their relative contribution to training despite differences in length. Through supervised initialization followed by SafePO, we develop AdaGuard, a family of 0.6B, 4B, and 8B guard models that assess agent trajectories under policies supplied at inference time. Our 4B model achieves binary accuracies of 89.30\% on AdaptiveSafety and 71.82\% on DynaBench. The project repository is available at https://github.com/Yunhao-Feng/AdaGuard
