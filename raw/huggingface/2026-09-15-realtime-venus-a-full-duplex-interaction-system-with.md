---
source: farmer/huggingface
farmed: 2026-09-15T10:58:02.142912
arxiv_id: 2609.13814
url: https://huggingface.co/papers/2609.13814
arxiv_url: https://arxiv.org/abs/2609.13814
date: 2026-09-15
---

# Realtime-Venus: A full-duplex interaction system with asynchronous delegation

Natural interaction in digital and physical environments requires continuous perception and timely responses. Spoken dialogue relies on acoustic and linguistic cues, while video interaction also requires grounding the conversation in evolving visual context. We present Realtime-Venus, a proactive full-duplex interaction system with two separately trained 9B models: Realtime-Venus-Omni for audio-visual interaction and Realtime-Venus-Audio for spoken interaction. Each model serves as a complete conversational frontend, integrating continuous perception, conversational control, and native speech generation through a shared causal timeline for user inputs, model outputs, and delegation events.
  A dual-loop runtime coordinates live interaction with background reasoning and tool execution. Foreground interaction continues while Realtime-Venus-Harness executes tasks asynchronously and returns results for integration into the ongoing dialogue.
  Both models follow a common post-training recipe combining offline understanding, proactive full-duplex trajectories, and delegation workflows.
  Among the evaluated online models, Realtime-Venus-Omni achieves the highest scores on six of eight video benchmarks, including StreamingBench (70.2%), OVO-Bench (64.7%), and Daily-Omni (81.3%). Across eight audio understanding and spoken question answering benchmarks, Realtime-Venus-Audio leads the compared models on MMAU (78.0%), MMAU-Pro (63.2%), Llama Questions (83.8%), and Speech CMMLU (67.8%), while matching the best VoiceBench AlpacaEval score of 4.81. On Full-Duplex-Bench v1.5, Realtime-Venus-Audio responds to 75% of user interruptions and achieves continuation rates of 97%, 88%, and 86% under backchannels, other-directed speech, and background speech, respectively, exceeding Gemini 3.1 Live and GPT-4o on all three continuation metrics.
