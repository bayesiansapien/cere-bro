---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.823473+00:00
arxiv_id: 2610.00360
url: https://huggingface.co/papers/2610.00360
arxiv_url: https://arxiv.org/abs/2610.00360
date: 2026-10-02
---

# DexPolicy: Scheduled Exploration for Trajectory-Guided Dexterous Manipulation

Reinforcement learning (RL) for dexterous manipulation must discover finger-object contacts and then control the object precisely; the action noise that serves the first goal can interfere with the second. In trajectory-guided settings such as ViViDex, where RL refine hand-object trajectories from human video, our baseline PPO runs end near their initial action noise after 5M steps, motivating explicit control of exploration scale. DexPolicy makes that scale an explicit function of training steps, annealing from broad to narrow exploration while holding loss, architecture, reward, and optimizer settings fixed. We study three policy-optimization settings: PPO, critic-free GRPO continuation, and a flow-parameterized PPO variant (FPO). Across five YCB objects and three training seeds, mean deterministic Target success rises from 49.4% to 68.1% (FPO), 14.1% to 45.4% (GRPO), and 32.0% to 35.7% (PPO). On a RealMan RM75 arm with an Inspire/RH56 hand, 360 trials over three objects raise mean Target success from 25.0% to 85.0% (FPO), 10.0% to 63.3% (GRPO), and 8.3% to 43.3% (PPO), with one trained model per object-method condition. PPO component screening favors noise control over the tested optimizer contraction; the selected PPO schedule yields higher mean Target success than linear decay with the same endpoints on three tested objects. Training return, deterministic Target success, and tolerance to execution noise dissociate; schedules should therefore be judged by terminal task success under the intended execution conditions, per task and policy-optimization setting. Code: https://github.com/AIGeeksGroup/DexPolicy. Website: https://aigeeksgroup.github.io/DexPolicy.
