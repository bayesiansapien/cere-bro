---
source: farmer/huggingface
farmed: 2026-09-01T08:46:18.970698+00:00
arxiv_id: 2608.29910
url: https://huggingface.co/papers/2608.29910
arxiv_url: https://arxiv.org/abs/2608.29910
date: 2026-09-01
---

# Matrix-Game 3.5: Enhancing Real-Time Streaming Interactive World Models with Patch Memory

Interactive world models extend video generation from offline clip synthesis toward persistent simulation of interactive virtual worlds, enabling applications in games, robotics, embodied agents, and XR. Achieving stable long-horizon interactive generation, however, remains challenging, as the model must simultaneously preserve scene geometry, dynamic consistency, and camera control while supporting real-time autoregressive generation. Building upon Matrix-Game 3.0, we present Matrix-Game 3.5, as shown in Figure 1, which advances real-time interactive world generation toward geometry-aware and long-horizon consistent simulation through three key improvements. First, we propose a unified geometry-aware memory framework, whose patch-memory and tiled-PRoPE components introduce no additional learnable parameters, combining explicit 3D patch retrieval with projective camera conditioning to enable geometry-consistent camera control and faithful long-horizon scene recall. Second, we introduce a static-dynamic disentangled world representation that separately models static scene geometry and dynamic subjects, preserving both geometric consistency and subject identity throughout long-horizon generation. Third, we develop a two-stage progressive real-time distillation framework that converts a bidirectional diffusion model into a few-step causal generator through Perceptual Flow Matching and curriculum based Self-Rollout DMD, enabling minute-long real-time interactive generation. Extensive experiments demonstrate that, with a unified training corpus spanning Unreal simulation environments, open-world games, and internet videos, MatrixGame 3.5 achieves strong performance in long-horizon scene recall, precise camera control, subject consistency, prompt-driven world generation, and stable real-time open-world interaction.
