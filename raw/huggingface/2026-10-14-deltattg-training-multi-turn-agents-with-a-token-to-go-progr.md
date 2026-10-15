---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.504252+00:00
arxiv_id: 2610.17666
url: https://huggingface.co/papers/2610.17666
arxiv_url: https://arxiv.org/abs/2610.17666
date: 2026-10-14
---

# DeltaTTG: Training Multi-Turn Agents with a Token-to-Go Progress Meter

Reinforcement learning with verifiable rewards (RLVR) for multi-turn agents relies on sparse terminal rewards that say little about individual steps. Within-group step comparisons depend on reliable state matching and sufficiently diverse sampled outcomes, while direct step scoring may require costly external evaluators, human annotations, or task-specific heuristics. We introduce DeltaTTG to learn a reusable progress signal through a shared progress meter, using low-cost supervision from diverse policies' recorded trajectories without task-specific progress rules. Its supervision target, Token-to-Go (TTG), the number of tokens remaining to be generated until task completion, serves as an observable proxy for remaining completion effort. During actor training, changes in the frozen meter's estimates redistribute outcome-derived advantages across steps without altering the reward, preserving each trajectory's advantage sign and token-average scale. On ALFWorld, PaperSearchQA, and BFCLv3, DeltaTTG improves the average score over GRPO by 5.7 and 7.2 points with Qwen3-4B and Llama-3.1-8B-Instruct, respectively, outperforms all compared RL baselines on average, and keeps actor-training GPU-hours close to GRPO. Further experiments show improved sample efficiency and out-of-domain performance, and support the meter's ability to distinguish step quality and guide test-time action selection across actor sizes. The code is available at https://github.com/Xuyan923r/DeltaTTG.
