---
source: farmer/huggingface
farmed: 2026-06-18T00:00:00Z
arxiv_id: 2606.19338
url: https://huggingface.co/papers/2606.19338
arxiv_url: https://arxiv.org/abs/2606.19338
date: 2026-06-18
---

# Beyond the Current Observation: Evaluating Multimodal Large Language Models in Controllable Non-Markov Games

Deploying multimodal foundation models as closed-loop policies increasingly requires conditioning actions on observations that are no longer visible. However, existing benchmarks either expose the full state, conflate hidden-state reconstruction with other agent skills, or test recall only after an episode has ended. We introduce RNG-Bench (Reconstructive Non-Markov Games), a benchmark suite designed to isolate a base model's ability to reconstruct past observations and act on them during multi-step interaction. RNG-Bench includes two complementary games: Matching Pairs, where card identities briefly revealed at specific locations must later be recalled, and 3D Maze, where egocentric views must be integrated into a spatial map. Both games are evaluated under a unified harness with three controlled difficulty axes: grid size, visual pattern, and observation modality. The benchmark further introduces a head-to-head duel protocol to control for instance-level variance and a Memory Gap metric that disentangles forgetting from poor action selection. The hardest configurations require contexts of roughly 128K tokens and 350 image inputs per episode, and remain far from saturated by frontier MLLMs. Memory Gap analysis shows that most residual errors stem from forgetting earlier observations rather than from suboptimal decision making. Finally, fine-tuning Qwen3.5-9B on optimal-policy rollouts and filtered model demonstrations improves performance on RNG-Bench and transfers to existing benchmarks without degrading general multimodal capability.
