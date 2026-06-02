---
source: farmer/huggingface
farmed: 2026-06-02T09:40:06Z
arxiv_id: 2605.29860
url: https://huggingface.co/papers/2605.29860
arxiv_url: https://arxiv.org/abs/2605.29860
date: 2026-06-02
---

# ESPO: Early-Stopping Proximal Policy Optimization

When a large language model under reinforcement learning commits a wrong reasoning step early in a trajectory, standard algorithms force it to keep generating until the maximum horizon, spending compute on tokens that never receive positive reward and polluting advantage estimates with post-failure noise. We propose ESPO (Early-Stopping Proximal Policy Optimization), which detects trajectory failure on-the-fly and terminates rollouts early. At each generation step, ESPO computes a surrogate regret using only the logits already computed during sampling, and terminates when the smoothed cumulative regret significantly exceeds its estimated values. Truncated trajectories are treated as absorbing failure states with a terminal reward, concentrating negative temporal-difference (TD) errors near the detected failure step without any additional reward model or human annotation. On DeepSeek-R1-Distill-Qwen-7B trained for mathematical reasoning, ESPO surpasses PPO on AIME~2024 (46.28% vs. 45.25%), AMC~2023 (85.83% vs. 82.94%), and MATH-500 (87.42% vs. 85.43%), while saving more than 20% rollout tokens cumulatively.
