---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.643605
arxiv_id: 2610.28069
url: https://huggingface.co/papers/2610.28069
arxiv_url: https://arxiv.org/abs/2610.28069
date: 2026-10-21
---

# Training the Whole Agent, Not Just the Model

Training coding agents typically updates the policy while keeping the harness fixed. During training, trajectories reveal flawed repair strategies and interaction problems that vary across tasks and change as the policy learns. We introduce HarnessAdapt-RL, which trains the policy and adapts its harness during reinforcement learning. For flawed repair strategies, a frozen teacher generates task-specific mechanism-level skills. For interaction problems recurring across tasks, a separate teacher model evolves tools and hooks, keeping each change only if it improves the observed pass rate or the observed trainable rate without lowering either. The policy trains with the adapted harness, and its new trajectories guide further adaptation. With a 9B base model, HarnessAdapt-RL improves pass@1 over GRPO by 9.8, 12.6, and 6.4 percentage points on SWE-bench Verified, Multilingual, and Pro, and outperforms GRPO with the human-designed OpenHands harness. Gains from mechanism-level skills persist after their removal at evaluation. Re-evolving tools and hooks as the policy changes outperforms freezing early versions. Removing them at deployment, in contrast, costs up to 7.7 percentage points. Training therefore produces a model-harness pair: the trained policy and the evolved tools and hooks, with skills removed at deployment.
