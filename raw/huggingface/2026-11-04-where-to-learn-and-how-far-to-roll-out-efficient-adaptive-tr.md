---
source: farmer/huggingface
farmed: 2026-11-05T20:36:55.366556+05:30
arxiv_id: 2610.39251
url: https://huggingface.co/papers/2610.39251
arxiv_url: https://arxiv.org/abs/2610.39251
date: 2026-11-04
---

# Where to Learn and How Far to Roll Out: Efficient Adaptive Training for GUI Agents

Trajectory-level GRPO is a common approach for training multi-step GUI agents, but repeatedly rolling out complete trajectories from the task root can be inefficient: task-level rewards provide coarse supervision over which intermediate decisions require improvement, while already-mastered prefixes are repeatedly re-executed before reaching difficult states. We introduce a two-stage adaptive training framework that jointly addresses where to learn and how far to roll out. We first construct reusable intermediate checkpoints from successful expert trajectories and select informative pivots using action disagreement, which measures uncertainty directly from sampled GUI actions. Stage I performs one-step RL at these pivots to improve uncertain local decisions. Stage II then progressively expands policy responsibility through adaptive Local, Suffix, and Root training according to task progress. Recoverable checkpoints enable repeated training from intermediate states without replaying the preceding trajectory. Across MobileGym and CUA-Gym-Hub, our method reduces environment interaction by 56-61% relative to Vanilla GRPO while improving task performance, demonstrating that jointly allocating training across states and rollout ranges can substantially improve GUI-agent RL efficiency.
