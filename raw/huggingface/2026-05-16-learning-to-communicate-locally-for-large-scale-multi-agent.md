---
source: farmer/huggingface
farmed: 2026-05-16T03:36:10Z
arxiv_id: "2605.07637"
url: "https://huggingface.co/papers/2605.07637"
arxiv_url: "https://arxiv.org/abs/2605.07637"
date: 2026-05-16
---

# Learning to Communicate Locally for Large-Scale Multi-Agent Pathfinding

Multi-agent pathfinding (MAPF) is a widely used abstraction for multi-robot trajectory planning problems, where multiple homogeneous agents move simultaneously within a shared environment. Although solving MAPF optimally is NP-hard, scalable and efficient solvers are critical for real-world applications such as logistics and search-and-rescue. To this end, the research community has proposed various decentralized suboptimal MAPF solvers that leverage machine learning. Such methods frame MAPF (from a single agent perspective) as a Dec-POMDP where at each time step an agent has to decide an action based on the local observation and typically solve the problem via reinforcement learning or imitation learning. We follow the same approach but additionally introduce a learnable communication module tailored to enhance cooperation between agents via efficient feature sharing. We present the Local Communication for Multi-agent Pathfinding (LC-MAPF), a generalizable pre-trained model that applies multi-round communication between neighboring agents to exchange information and improve their coordination. Our experiments show that the introduced method outperforms the existing learning-based MAPF solvers, including IL and RL-based approaches, across diverse metrics in a diverse range of (unseen) test scenarios. Remarkably, the introduced communication mechanism does not compromise LC-MAPF's scalability, a common bottleneck for communication-based MAPF solvers.
