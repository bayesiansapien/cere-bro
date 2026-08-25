---
source: farmer/huggingface
farmed: 2026-08-25T14:22:16.352902
arxiv_id: 2608.23070
url: https://huggingface.co/papers/2608.23070
arxiv_url: https://arxiv.org/abs/2608.23070
date: 2026-08-25
upvotes: 1
authors: ["Tong Wang", "Huan Deng", "Mucheng Yang", "Yang He", "Xiaohui Kuang", "Gang Zhao"]
---

# From Generation to Simulation: How Far Are World Models from Being True Simulators?

**Upvotes:** 1
**Authors:** Tong Wang, Huan Deng, Mucheng Yang, Yang He, Xiaohui Kuang, Gang Zhao

With the rapid progress of diffusion models and large-scale video generation, generative world models are increasingly expected to replace traditional simulators, including physics engines, game engines, and reinforcement-learning environments. Yet the remaining distance from generation to simulation lacks a systematic assessment. We present a capability-based study using an external yardstick: eight capabilities of a traditional simulator, namely asset construction, physics engine, interaction, controllability, stability, state feedback, diversity, and evaluation metrics. We trace three main technical routes--latent dynamics, video generation, and joint-embedding prediction--and map exactly 200 representative works published from 2018 to June 2026 onto these capabilities. Our analysis shows that world models have achieved functional substitution in interaction and controllability for specific scenarios, but remain short of traditional simulators in formal guarantees of physical laws, structured state feedback, and reproducible long-horizon evolution. State feedback is the most neglected cross-route shortcoming: only 6 of 163 implementation papers expose a runtime interface for querying entity states or physical parameters. We identify six research directions: formalized physics, a unified action interface, first-class state feedback, long-horizon stability, downstream-utility evaluation, and cross-route hybridization. Project page: https://github.com/AtongWang/world-model-simulators
