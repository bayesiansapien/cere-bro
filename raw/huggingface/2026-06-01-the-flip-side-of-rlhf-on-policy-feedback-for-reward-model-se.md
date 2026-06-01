---
source: farmer/huggingface
farmed: 2026-06-01T09:02:45Z
arxiv_id: 2605.30888
url: https://huggingface.co/papers/2605.30888
arxiv_url: https://arxiv.org/abs/2605.30888
date: 2026-06-01
---

# The Flip Side of RLHF: On-Policy Feedback for Reward Model Self-Supervised Improvement

Building strong reward models (RMs) for language model alignment is bottlenecked by the cost and difficulty of acquiring diverse and reliable preference data from human annotation or judge models. It is dramatically worse as the policy evolves beyond the static RM training. Therefore, we propose SAVE (Self-supervised reward model improvement via Value-Anchored On-policy feedback), a framework that grades on-policy responses as feedback by using the value function for on-policy RM training. SAVE naturally converts the reward-graded on-policy responses into supervision with a prompt-specific value head as an adaptive anchor. It computes RM advantages and filters ambiguous samples to update the RM via a contrastive objective. The effectiveness of SAVE for enhancing RM training is strongly validated through rigorous empirical evaluation across six diverse benchmarks. It achieves outperforming results across all datasets while maintaining consistent improvements across three RL algorithms (GRPO, RLOO, GSPO) and different policy backbones.
