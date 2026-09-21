---
source: farmer/huggingface
farmed: 2026-09-21T05:24:18.050611+00:00
arxiv_id: 2609.20669
url: https://huggingface.co/papers/2609.20669
arxiv_url: https://arxiv.org/abs/2609.20669
date: 2026-09-21
---

# Learning Foresight without Explicit Trajectories for 3D Diffusion Policies

3D diffusion policies are strong at generating geometrically grounded actions from current observations, but successful manipulation requires not only knowing what motion is feasible now, but also anticipating where the interaction is heading. Existing policies largely leave such foresight to emerge implicitly from action learning. We introduce Movement Trend Guidance, a simple but effective way to provide this foresight without introducing an explicit plan. From a short observation history, the policy learns a compact latent representation of interaction evolution. During training, sparse future gripper states supervise this representation; at inference, only the latent is retained as future-oriented conditioning alongside the current observation. The latent provides global conditioning for action generation, while an additional gated FiLM branch is used only at the UNet bottleneck. Despite adding only 3.52% more parameters to DP3, our method preserves the original dense-action and receding-horizon formulation and consistently improves upon DP3 across RoboTwin2.0, LIBERO-40, and DexArt. It reaches 62.8% vs. 56.1% in 50-task RoboTwin2.0 mixed training, 71.93% vs. 37.08% on LIBERO-40, and 72.0% vs. 49.0% on five real-robot tasks. These results show that a diffusion policy can benefit substantially from knowing where an interaction is heading, without being told exactly where to move.
