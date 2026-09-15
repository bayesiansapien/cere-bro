---
source: farmer/huggingface
farmed: 2026-09-15T10:58:02.142912
arxiv_id: 2609.15128
url: https://huggingface.co/papers/2609.15128
arxiv_url: https://arxiv.org/abs/2609.15128
date: 2026-09-15
---

# Omni-Streaming Thinking

Streaming omni-modal models must decide what and when to answer from the video chunks and synchronized audio observed so far. Visual cues often support an interpretation before an utterance or sound event is complete. If that interpretation enters memory as a fact, later reasoning can keep relaying it even after audio contradicts it. We call this failure premature cross-modal commitment. We propose Omni-Streaming Thinking (OST), which generates structured outputs that include evidence observed so far, forecasts of future evidence, and claims based on this evidence. Each claim is initially marked as pending and linked to a future verification interval. Audio and visual evidence are stored separately, and OST checks a claim against the evidence from the specified modality at the end of the verification interval. When contradictory evidence is detected, a refutation process reduces the influence of the claim and its dependent states, and then guides a state update using the new evidence. An answer gate decides whether the answer-critical claims meet the conditions for giving a response. Using a frozen Qwen3-Omni-30B-A3B-Instruct backbone with lightweight adaptation, OST outperforms the strongest open baselines on five streaming and audio-visual benchmarks by more than 10% relative on average. We also introduce OST-DiagBench, which holds video fixed and edits audio to test agreement, absence, contradiction, coexistence, and subtitle-speech conflict. OST reaches d-prime = 2.95, compared with at most 1.38 for open baselines, while reducing vision-induced auditory hallucinations.
