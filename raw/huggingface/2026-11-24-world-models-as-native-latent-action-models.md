---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.920110+00:00
arxiv_id: 2611.30898
url: https://huggingface.co/papers/2611.30898
arxiv_url: https://arxiv.org/abs/2611.30898
date: 2026-11-24
---

# World Models as Native Latent Action Models

Large and diverse video sources, such as egocentric human video and heterogeneous robot recordings, carry rich dynamics but come either without actions or without a shared action space. Latent action models (LAMs) can recover these dynamics, but they train their inverse- and forward-dynamics models (IDM, FDM) from scratch, trading off pixel reconstruction against latent capacity and accuracy. Pretrained video world models natively generate high-fidelity dynamics, yet represent them densely, entangled across all layers. Viewing the world model as a LAM, we show that these dynamics can be extracted with minimal changes to the model. Native LAM operates one pretrained video diffusion transformer as both IDM and FDM, with learnable dynamics registers as the only causal bridge between the two, and trains on counterfactual temporal pairs that differ in motion alone, so that the registers distill a video's dynamics into a compact native latent action. We further propose a pretraining paradigm for vision-language-action (VLA) policies, Pretraining Actions from World models (PAWlicy), in which Native LAM serves as a dynamics teacher on large-scale video; unlike world action models, it never generates video. Native latent actions outperform existing LAMs on the LARY benchmark in both action classification and control regression, and replay the same motion on new robots, in new scenes, and from human hands to robots, although no transfer objective is used in training. With a 3.8B model, PAWlicy reaches a 93.6% average success rate on RoboTwin 2.0 trained with domain-randomized demonstrations, the highest among VLAs. On RoboDojo, it is competitive on every dimension we evaluate, and its Precision, evaluated by us, is on par with the leading leaderboard entries. On real robots, it improves over the pi_0.5 baseline on both tasks. Both stages use only public data and a publicly released world model.
