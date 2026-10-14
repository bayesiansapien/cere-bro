---
source: farmer/huggingface
farmed: 2026-10-14T17:45:17.067247+05:30
arxiv_id: 2610.12099
url: https://huggingface.co/papers/2610.12099
arxiv_url: https://arxiv.org/abs/2610.12099
date: 2026-10-13
---

# UNITAS: A 3D-Native World Action Model for Embodied Manipulation

World action models (WAMs) aim to answer a coupled physical question: given a task instruction, what motion should the robot execute, and how will that motion change the surrounding world? Most existing WAMs build on pretrained video generators and represent world evolution through images or visual latents. Robotic interaction, however, takes place in metric three-dimensional space, while images are view-dependent projections whose pixel distances do not directly encode physical distances. We introduce UNITAS, to our knowledge the first 3D-native world action model that unifies observations, actions, and scene dynamics in a shared metric 3D frame within each interaction, using a common representation across robot embodiments and human hands. Action flow represents human hands and robot grippers as 3D point trajectories, while scene flow describes scene-point displacements conditioned on these trajectories. World-aligned 3D positional embeddings ground visual tokens with or without depth input, and a physical-time trajectory tokenizer encodes each point trajectory as one token anchored at its current 3D position. This interface supports both direct action execution and action-conditioned scene prediction. With 1.7B parameters, UNITAS achieves the best action-conditioned scene prediction on RoboTwin among the compared methods, with up to 49% lower displacement errors than PointWorld, and state-of-the-art manipulation success, including 99.8% on LIBERO and an average of 85% across real-world tasks. The code is available at https://github.com/DexForce/UNITAS.
