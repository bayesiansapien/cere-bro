---
source: farmer/huggingface
farmed: 2026-09-18T16:13:44.923131+00:00
arxiv_id: 2609.20715
url: https://huggingface.co/papers/2609.20715
arxiv_url: https://arxiv.org/abs/2609.20715
date: 2026-09-18
---

# Don't Mask the Environment: Observation Supervision Changes How Agents Explore Under RL

Agent trajectories record what an agent does and what happens next. Yet standard supervised fine-tuning (SFT) applies loss only to agent-authored action tokens, using environment observations as context but not as prediction targets. We ask whether this convention provides the best initialization for subsequent reinforcement learning. We introduce ActObs, which also supervises the observation tokens already present in each trajectory. Although deployed agents never generate observations, learning to predict them encourages the policy to model action consequences without adding data, parameters, sequence tokens, or forward passes. The methods perform similarly after SFT but diverge after GRPO. On Qwen3-4B, GRPO from ActObs achieves higher pass@k at every evaluated sampling budget than its action-only counterpart on Terminal-Bench 2.0. On Qwen3-8B, it trades some pass@1 reliability for higher pass@k (+3.4 pp at pass@16) and solves more distinct tasks. The advantage extends to cross-domain code editing on aider-polyglot (+4.2 pp at pass@1 at 4B), whose tasks are unseen during SFT and RL. ActObs retains more entropy during RL while requiring less policy movement, leaving the final policy closer to its SFT initialization. Our analysis traces this difference to SFT: action and observation gradients rapidly become orthogonal, while action-only training leaves a large residual observation gradient and degrades environment prediction below the base model. Joint supervision prevents this one-sided specialization, preserving consequence prediction and preparing the policy for downstream exploration.
