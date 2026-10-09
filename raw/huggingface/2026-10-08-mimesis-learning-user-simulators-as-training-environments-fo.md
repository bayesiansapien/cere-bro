---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.305261+05:30
arxiv_id: 2610.09484
url: https://huggingface.co/papers/2610.09484
arxiv_url: https://arxiv.org/abs/2610.09484
date: 2026-10-08
---

# MIMESIS: Learning User Simulators as Training Environments for Interactive Agents

Training and evaluating interactive language agents typically requires rich user interactions, yet collecting human feedback is expensive and difficult to scale. Simulated users offer a scalable alternative, but they must both resemble real user behavior and provide useful learning experiences for agents. In contrast, most agent-training frameworks rely on off-the-shelf assistant LLMs, whose helpfulness can make them overly cooperative, explicit, and behaviorally homogeneous compared with real users. We introduce MIMESIS, a purpose-built user simulator trained on human conversations with explicit reasoning supervision and 13 realistic behavioral patterns derived from real user interactions. Empirically, our 9B model achieves a SOUL-Index of 65.7, surpassing the strongest frontier model. Compared with Claude-Opus-5, the strongest baseline on RealUserSim and SimulatorArena, MIMESIS improves behavioral fidelity by 13.4 points and reduces Turing distance by 3.6 points, respectively. We then freeze the simulator and train an agent by interacting with the frozen simulator using multi-turn reinforcement learning. Across eight environments, training with MIMESIS yields better agent performance than training with GPT-5.5 under all nine unseen user simulators, demonstrating stronger generalization to new user simulators. Moreover, we propose Coached On-Policy Self-Distillation (CSD), which leverages simulator-generated private reasoning traces and subsequent utterances as feedback on how well the agent addresses user needs. A coach converts this information into concise coaching notes that describe how the agent can better anticipate user needs and adapt its behavior over the course of an interaction. CSD turns this feedback into dense, token-level supervision beyond sparse task rewards, yielding further gains across all nine evaluation user models.
