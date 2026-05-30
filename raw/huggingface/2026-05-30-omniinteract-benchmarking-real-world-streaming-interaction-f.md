---
source: farmer/huggingface
farmed: 2026-05-30T09:33:08Z
arxiv_id: 2605.26485
url: https://huggingface.co/papers/2605.26485
arxiv_url: https://arxiv.org/abs/2605.26485
date: 2026-05-30
---

# OmniInteract: Benchmarking Real-World Streaming Interaction for Real-Time Omnimodal Assistants

We introduce OmniInteract, a streaming benchmark for real-time omnimodal large language models evaluated through native online inference over audio-visual streams. Unlike offline video understanding or text-prompted streaming QA, OmniInteract preserves the original audio-visual stream and requires models to process it online, without access to future content. User queries and ambient sounds are embedded in the audio track, requiring models to detect multimodal triggers, decide when to respond, and answer while the stream unfolds. OmniInteract contains 250 videos with 1,430 temporally grounded response slots: 1,062 1Q1A slots across real-time, proactive, and nested scenarios, and 368 1QnA slots for continuous task monitoring and step guidance. Each slot includes a trigger, response window, and target answer. We evaluate response correctness, timing, invalid outputs, interruption handling, and context continuity using Interaction-Aware Quality-Timeliness F1, Interruption Diagnostic Suite, and Nested Chain Completion Score. Experiments show that current models remain weak in streaming interaction, with the best overall IA-QTF1 reaching only 0.368 and the best 1QnA IA-QTF1 only 0.052. Further study on mathematical reasoning in full-duplex settings shows that offline capability does not necessarily transfer to online interaction. Code and datasets will be made publicly accessible at https://github.com/Lucky-Lance/OmniInteract.
