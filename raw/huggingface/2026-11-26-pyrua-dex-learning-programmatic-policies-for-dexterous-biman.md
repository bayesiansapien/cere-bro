---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.903335+00:00
arxiv_id: 2611.33144
url: https://huggingface.co/papers/2611.33144
arxiv_url: https://arxiv.org/abs/2611.33144
date: 2026-11-26
---

# PyRUA-Dex: Learning Programmatic Policies for Dexterous Bimanual Manipulation with Coding Agents

Learning for dexterous manipulation is limited by the scarcity of high-quality demonstrations: retargeting from human video is imprecise, teleoperation gives no force feedback to the operator, and exoskeleton-based collection is hard to scale up. We present PyRUA-Dex, a framework that enables coding agents to develop dexterous manipulation through programmatic policy, without the need of demonstrations. The programmatic policy is developed in two stages: during exploration, multiple agents explore in parallel for task skills and ways to compose them, and a distilling agent condenses the successful attempts into a task library and one program. During refinement, this program is improved through randomized layouts for enhanced robustness and execution efficiency. In simulated environments, PyRUA-Dex achieves SOTA on Bench2Dex with a score of 72.9 and reaches 81.0% success on DexJoCo under full randomization, ahead of every trained policy on both benchmarks. In real world experiments on a bimanual platform with two 22-DoF hands, PyRUA-Dex learns to play piano, write calligraphy, and other tasks efficiently: learning a new piece from sheet music takes as little as 30 minutes. These results suggest that PyRUA-Dex is an effective framework for developing dexterous manipulation policies with coding agents in the absence of high quality dexterous manipulation demonstrations.
