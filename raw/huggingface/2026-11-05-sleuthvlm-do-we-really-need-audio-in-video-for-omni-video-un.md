---
source: farmer/huggingface
farmed: 2026-11-06T05:50:41.305497+00:00
arxiv_id: 2611.06083
url: https://huggingface.co/papers/2611.06083
arxiv_url: https://arxiv.org/abs/2611.06083
date: 2026-11-05
---

# SleuthVLM: Do We Really Need Audio-in-Video for Omni Video Understanding?

Omni models answer questions about videos by jointly processing sampled frames and audio in one turn, with progress driven largely by scaling model size and omni training data. We ask whether a model needs to hear the audio directly at all, and present SleuthVLM, an agent harness built on a VLM that never hears the audio directly: speech will be transcribed into text, and the VLM will sleuth the video on its own without any predefined workflow. On four omni benchmarks with videos up to 90 minutes, SleuthVLM achieves the best average accuracy: 75.0%, 2.6 points above Gemini 3.8 Flash, and it also tops the Video-MME-v2 leaderboard with 77.8%; with an open-source 27B VLM, it beats all open-source omni models. We draw three findings: SleuthVLM beats a model that glances; hearing is not the bottleneck, agentic ability is; omni understanding needs better agentic ability, not just more omni data for modality alignment. So we provide a simple but effective starting point for doing omni video understanding. Omni understanding needs better agents, not just bigger models that hear.
