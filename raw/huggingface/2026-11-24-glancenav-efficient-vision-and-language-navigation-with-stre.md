---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.927115+00:00
arxiv_id: 2611.30900
url: https://huggingface.co/papers/2611.30900
arxiv_url: https://arxiv.org/abs/2611.30900
date: 2026-11-24
---

# GlanceNav: Efficient Vision-and-Language Navigation with Streaming Memory and Counterfactual Rewind

Multimodal large language models (MLLMs) have become strong policies for vision-and-language navigation (VLN). However, most of them encode a sample of past frames again at every decision and are trained on isolated decisions, so computation is redundant and the usable history is short. They also learn from their own mistakes through outcome rewards that give one scalar to a whole episode. We ask whether a navigator can encode each frame only once, at a constant cost per step, and still remember what matters and learn efficiently from its mistakes. We present GlanceNav, a streaming navigator built on a hybrid MLLM. Its Gated DeltaNet layers carry a recurrent state through the whole episode, while its attention layers keep a short window of recent observations and a small bank of keyframes, selected by how much each frame changes the recurrent state. This constant-size memory keeps the cost per step fixed and allows training on whole episodes with the same memory as at inference. Because the entire memory can also be copied in constant time, we further propose Counterfactual Rewind (CoRe), a reinforcement learning stage that rewinds a drifting rollout to its closest approach to the goal, lets an expert correct a few actions, and credits decisions by the resulting change in outcome. Trained only on the R2R-CE and RxR-CE training splits, with 1,000 instructions for reinforcement learning, a 4B GlanceNav reaches success rates of 71.9% and 73.6% on R2R-CE and RxR-CE val-unseen. On R2R-CE, it outperforms the strongest previous single-RGB method trained without external data by 9.1 points, while running at 104 ms per step.
