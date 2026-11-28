---
source: farmer/huggingface
farmed: 2026-11-28T10:45:04+05:30
arxiv_id: 2611.34693
url: https://huggingface.co/papers/2611.34693
arxiv_url: https://arxiv.org/abs/2611.34693
date: 2026-11-27
---

# ShowNow: Fine-Grained Speculative Streaming for Responsive World Models

Interactive world models must generate video continuously while responding promptly to user actions. Real-time throughput alone leaves input latency unresolved: coarse generation blocks delay action updates, and generation after input adds work to the response path. We introduce ShowNow, a fine-grained speculative streaming framework that uses computation available during playback to prepare action-conditioned futures before input arrives. Single-latent commitment enables frequent decisions, while configurable preparation covers one to eight actions. We construct a matched multi-future dataset to train alternative continuations from a common state; shared-history tree execution and fused commitment make their preparation efficient. On a single H100, our 5B model sustains 480p generation at 16 fps with eight prepared futures. In ViZDoom, the complete ShowNow deployment reduces median input-to-display latency from 620 to 208 ms relative to the native-block SolarWM-FT deployment. Matched-policy experiments reduce restart empty ticks from 1.56% to 0.09% (94%) and improve on-time responses to action changes. These results establish complementary roles for fine-grained commitment and advance preparation, with measured trade-offs in visual fidelity and long-horizon consistency. ShowNow turns playback-time computation into responsive visual interaction. Project: https://github.com/showlab/ShowNow.
