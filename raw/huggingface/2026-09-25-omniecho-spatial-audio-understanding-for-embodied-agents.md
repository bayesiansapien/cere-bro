---
source: farmer/huggingface
farmed: 2026-09-25T22:51:58.846051
arxiv_id: 2609.23407
url: https://huggingface.co/papers/2609.23407
arxiv_url: https://arxiv.org/abs/2609.23407
date: 2026-09-25
upvotes: 20
---

# OmniEcho: Spatial Audio Understanding for Embodied Agents

Humans can effortlessly localize the direction of a sound source and integrate it with visual cues for reasoning, yet this remains challenging for embodied agents. In particular, it is still unclear how to effectively evaluate and model spatial audio understanding in embodied settings. To address this gap, we introduce OmniEchoBench, a unified benchmark for spatial audio-visual perception and audio-vision-language navigation. OmniEchoBench comprises six tasks over 197 real-world spatial audio-visual scenes, 2,972 question-answer pairs, and 900 navigation samples with first-order ambisonics (FOA) audio collected from 30 real-world environments. To enable scalable training supervision, we develop a controllable rendering pipeline for spatial audio. It preserves geometric consistency among sound sources, visual observations, and agent trajectories. Building on this, we propose OmniEcho, a spatially aware omni-modal model. It introduces an FOA spatial encoder alongside a pretrained semantic audio pathway. Extensive experiments show that OmniEcho achieves state-of-the-art performance on spatial audio-visual perception. For our sound-guided navigation, OmniEcho reaches a performance level close to that of traditional vision-language navigation. These results demonstrate that spatial audio can serve as a valuable signal for embodied scene reasoning and navigation, while also highlighting fine-grained spatial localization and distance estimation as important open challenges.
