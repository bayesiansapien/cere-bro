---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.25666
url: https://huggingface.co/papers/2610.25666
arxiv_url: https://arxiv.org/abs/2610.25666
date: 2026-10-20
---

# Frechet Forcing: Training Long-Horizon Streaming World Models from Short Clips

Streaming video world models generate the future chunk by chunk, conditioned on their own past and a stream of actions. Trained on short clips, they drift once a rollout exceeds the training horizon, as prediction errors re-enter the context and compound. A common remedy is to train the model on its own rollouts via distribution matching distillation (DMD). For action-conditioned world models, the teacher becomes a bottleneck: an external video model is agnostic to the actions, whereas the model's own pretrained network drifts in the same manner as the student. We observe that a long rollout need not match a teacher, provided it remains a realistic continuation of its own scene that follows the commanded actions. Realism and scene fidelity can be measured against real-data statistics, which remain valid at any horizon, while action following is preserved by the model's conditional generation loss. We propose Fréchet Forcing, which fine-tunes a world model together with its deployed multi-step sampler under three constraints. Generative anchoring applies the flow-matching loss after a self-generated history ending on real data. Context fidelity, a Fréchet distance (FD) on latent statistics of the free rollout centred on each clip's own ground truth, keeps every rollout faithful to its scene. Reality matching, an FD to real frames in a frozen perceptual space, keeps the generated frames realistic. Because all three targets are derived from short real clips without comparing a rollout against a long recorded future, training requires no teacher, no online critic and no long videos. Fine-tuning MiniWorld-1B, pretrained on 253-frame clips, for at most 36 GPU-hours on 381-frame clips yields rollouts that remain stable beyond 4,000 frames and continue to follow their actions in both robot manipulation and camera-controlled exploration.
