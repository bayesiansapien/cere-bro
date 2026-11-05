---
source: farmer/huggingface
farmed: 2026-11-05T20:36:55.363846+05:30
arxiv_id: 2611.03685
url: https://huggingface.co/papers/2611.03685
arxiv_url: https://arxiv.org/abs/2611.03685
date: 2026-11-04
---

# LOLPlay: Benchmarking Real-Time Visual Agents in League of Legends

Visual agents need to coordinate reasoning and action while their environment evolves during inference. We introduce LOLPlay, a benchmark in native League of Legends with 36 champion-specific tasks spanning resource management, combat, cooperation, and objectives. Agents interact through screenshots and mouse--keyboard actions; automated initialization and 82 executable subgoal checks distinguish partial progress from completion. Across 324 task evaluations of three models at three reasoning-effort settings, GPT-6 Astra achieves the highest task success rate of 25.0\% at low and medium effort, and the highest subgoal success rate of 40.3\% at medium effort. However, high effort improves neither metric over low effort for any model. For Astra, longer requests leave fewer interaction rounds, suggesting a cost to additional reasoning in real-time control. Trajectories reveal incomplete subgoal composition and actions executing after the observed scene changes, motivating agents that combine visual reasoning with timely action.
