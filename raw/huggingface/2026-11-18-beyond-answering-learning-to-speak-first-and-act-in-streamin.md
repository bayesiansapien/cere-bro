---
source: farmer/huggingface
farmed: 2026-11-19T11:13:13+05:30
arxiv_id: 2611.17048
url: https://huggingface.co/papers/2611.17048
arxiv_url: https://arxiv.org/abs/2611.17048
date: 2026-11-18
---

# Beyond Answering: Learning to Speak First and Act in Streaming Video

Most AI assistants respond only when prompted, remaining silent even when events in the video stream offer meaningful opportunities for conversation. To move beyond purely user-driven interaction, we present AURA 2.0, a streaming video large language model that introduces three core upgrades to AURA. The key advance is Model-Initiated Conversation (MIC), which enables the model to identify topics worth discussing in the evolving visual stream and initiate conversations at appropriate moments without a user query. Stream-Aware Tool Calling (SATC) lets the model act on what it sees by invoking external tools using the current visual and conversational context and incorporating returned information into the ongoing interaction. Interactive Visual Grounding (IVG) supports visual grounding in both user inputs and model outputs. The model can identify objects marked by users on video frames and produce frame-aligned bounding boxes to link its responses to specific objects and regions. To develop these capabilities, we construct a dedicated streaming interaction dataset and adopt a three-stage training scheme to integrate the new behaviors with AURA's existing streaming interaction abilities. We further incorporate Long-Horizon Interaction Memory (LHIM) to maintain contextual continuity over extended video streams. Evaluations on public streaming benchmarks show that AURA 2.0 achieves leading performance among open-source streaming models, while targeted evaluations further validate its new interaction capabilities.
