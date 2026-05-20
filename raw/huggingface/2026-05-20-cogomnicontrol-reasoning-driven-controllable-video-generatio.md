---
source: farmer/huggingface
farmed: 2026-05-20T09:55:03.047697+00:00
arxiv_id: 2605.19995
url: https://huggingface.co/papers/2605.19995
arxiv_url: https://arxiv.org/abs/2605.19995
date: 2026-05-20
---

# CogOmniControl: Reasoning-Driven Controllable Video Generation via Creative Intent Cognition

Recent diffusion models achieve strong photorealism and fluency in video generation, yet remain fragile under abstract, sparse or complex conditions, leading to poor performance in professional production workflows such as storyboard sketches and clay render conditions. Existing video generation models, either inject conditions through adapters or couple a generic vision-language model (VLM) within a diffusion backbone, leaving a capability gap and failing to produce the videos that align with the user&#39;s creative intent. We present CogOmniControl, a reasoning-driven framework that factorizes controllable video generation into creative intent cognition and generation. Specifically, we train a specialized CogVLM using authentic anime production data. Compared to generic VLMs, it generates more professional and clear outputs, accurately cognizing user creative intent from sparse and abstract conditions and tuning these cues into dense reasoning output. Besides, CogOmniDiT unifies the controls from various conditions through in-context generation and is aligned to the CogVLM reasoning outputs via reinforcement learning. Furthermore, leveraging CogVLM&#39;s robust capability in guiding video generation, we release its potential in planning specific evaluators and enable a Best-of-N selection for the generated videos. This integration transforms the entire framework into a closed-loop &#34;harness-like&#34; architecture. We further introduce CogReasonBench and CogControlBench, built from professional workflows data that carry genuine creative intent rather than simulated ones. Experiments on two benchmarks show that CogOmniControl surpassed the existing open-source models. The project website: this https URL
