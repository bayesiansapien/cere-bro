---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.31977
url: https://huggingface.co/papers/2611.31977
arxiv_url: https://arxiv.org/abs/2611.31977
date: 2026-11-25
---

# Distill to Loop: Turning Pretrained Diffusion Transformers into Looped Models with Adjustable Depth

Looped transformers reuse one block of shared weights along the depth of the network. Recent looped diffusion transformers are trained from scratch, which repeats the full pretraining cost although strong pretrained non-looped diffusion transformers exist. We propose Distill to Loop (Dooop), which distills a pretrained non-looped diffusion transformer into a looped student whose blocks are initialized from the teacher's. We cast distillation as a fixed-point iteration toward the teacher, in which the output after every loop is trained toward the teacher, and each loop is one step of an ordinary differential equation in depth. As a result, one model runs any number of loops at test time without retraining, and the higher-order ODE solvers of diffusion model sampling can be applied along the depth dimension for better results. Meanwhile, because a looped model produces an output after every loop, we also construct loop guidance between the outputs of different loop counts, which improves the generated samples at little extra compute. On SD3-medium, a looped student with about 37% of the teacher's parameters matches the teacher on average over GenEval, ImageReward, PickScore and HPSv2.1 with two to four loops, and with two loops it uses about 58% of the teacher's compute. And on a four-step SD3-medium, loop guidance raises the average of the four metrics from 88.2 to 99.2.
