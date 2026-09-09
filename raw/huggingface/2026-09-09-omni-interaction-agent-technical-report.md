---
source: farmer/huggingface
farmed: 2026-09-09T05:28:24.738031+00:00
arxiv_id: 2609.08977
url: https://huggingface.co/papers/2609.08977
arxiv_url: https://arxiv.org/abs/2609.08977
date: 2026-09-09
---

# Omni Interaction Agent Technical Report

In this work, we present Gander, an end-to-end model that unifies omni perception, realtime interaction, and agentic capabilities within a single framework. In contrast to turn-based conventional paradigms, Gander continuously receives streaming inputs across multiple modalities, including video, speech, and text, enabling natural full-duplex interaction in both everyday conversations and complex workflow-oriented agent scenarios. Users can interrupt the model at any time, while the model can also proactively provide intermediate feedback or ask follow up questions. To natively support these capabilities, Gander adopts two key architectural designs: 1) It employs a Cerebellum-Brain collaborative framework, in which the Cerebellum is responsible for realtime interaction and omni conversational capabilities, while the Brain handles complex reasoning and higher-level agentic tasks. The two components interact continuously through tool calling and the agent orchestration runtime. 2) The Cerebellum is built upon a streaming Thinker-Talker architecture, user inputs and model outputs are further flattened into an ordered token stream at the chunk level, providing a unified representation for low latency, continuous interaction. We conduct comprehensive evaluations of Gander across four dimensions: conversational ability, omni understanding, interactive capability, and agentic intelligence. Internal human evaluations demonstrate that Gander maintains the natural and expressive spoken dialogue capabilities of SOTA open source models while achieving competitive performance in omni interaction. Gander also demonstrates robustness in challenging real-world scenarios, including background noise interference, multi-party interactions, and backchannel communication. We release Gander together with its models, code, and data to facilitate further research and development in the community.
