---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.141305+00:00
arxiv_id: 2611.22925
url: https://huggingface.co/papers/2611.22925
arxiv_url: https://arxiv.org/abs/2611.22925
date: 2026-11-19
---

# Code World Model 2.0: Towards Infinite Controllable Video Generation

Visual proxies decouple explicit world-state simulation from photorealistic video synthesis, offering a controllable interface for both offline clip creation and real-time interactive streaming. Yet a practical renderer must address two challenges. Upstream proxies vary from coarse layouts to fine articulated geometry depending on the interaction, and streaming inference must operate in a few causal steps without accumulating drift across self-generated history. We present Invoker-Render, pairing a bidirectional creation model with a causal four-step streaming model under a shared conditioning interface over structural proxies, an appearance reference, and language. Trained on an aligned approximately 200-hour multi-granularity corpus, Invoker-Render honors fine geometric constraints when supplied while synthesizing plausible local motion under coarse proxies, enabling runtime selection of input detail. To bridge bidirectional creation and real-time streaming without compounding step compression and rollout drift, we introduce Progressive Forcing (ProForcing). ProForcing first trains a causal predictor and distills it into a four-step renderer using histories derived from training videos. Training then shifts to continuous self-generated rollouts. A pipelined serving stack supports efficient streaming inference. Experiments show versatile control across proxy families, granularities, and camera paths, consistent gains over recent streaming baselines, and stable 30-minute racing rollouts that preserve scene and subject appearance.
