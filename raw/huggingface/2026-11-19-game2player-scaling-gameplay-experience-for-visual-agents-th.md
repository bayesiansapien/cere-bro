---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.140170+00:00
arxiv_id: 2611.24154
url: https://huggingface.co/papers/2611.24154
arxiv_url: https://arxiv.org/abs/2611.24154
date: 2026-11-19
---

# Game2Player: Scaling Gameplay Experience for Visual Agents through Environment-Player Co-Development

Games are a rich testbed for visual agents, demanding perception, long-horizon planning, and precise control. However, collecting human gameplay is costly, and learning from gameplay videos requires inferring missing actions. Existing datasets also cover a limited range of games, often without explicit tasks or verifiable outcomes. To address these gaps, we introduce Game2Player, a framework that co-develops game environments and players to collect diverse and verifiable gameplay experience at scale. In the Game2Player loop, a Builder agent adapts existing web games, exposes their internal state, and defines tasks with state-based progress measures and success checks. A Coding Player and a VLM Player then attempt the tasks and report problems to the Builder for repair, so that play serves as both environment validation and training data collection. With Game2Player, we build 568 verified web games with 3,436 tasks, collect 15.7K trajectories (307 hours of gameplay), and hold out 50 games as the benchmark PlayerBench. To evaluate the collected experience as training data, we train VLM agents with progress-weighted SFT, assigning greater weight to steps that advance task progress. Game2Player-9B improves progress from 14.3% to 31.2% on PlayerBench and from 30.0% to 53.1% on the external GameWorld benchmark. More broadly, our work suggests a path for visual agents to scale their gameplay experience by building, verifying, and learning from existing game worlds.
