---
source: farmer/huggingface
farmed: 2026-10-31T08:06:35.159868+00:00
arxiv_id: 2610.38678
url: https://huggingface.co/papers/2610.38678
arxiv_url: https://arxiv.org/abs/2610.38678
date: 2026-10-30
---

# AskStream: When and What to Ask Proactively under Uncertainty in Streaming Video Understanding

Recent advances in multimodal large language models have increased interest in interaction paradigms for video understanding. The evolution from offline to streaming and proactive interaction has gradually shifted models from passive responders toward more proactive agents that can decide when to answer. However, existing proactive paradigms typically assume that the information required to answer a query is complete, leaving models to only wait or answer. In the real world, however, information is often incomplete due to uncertainty from either the video or the user. In proactive paradigms, such uncertainty can cause the model to wait forever or generate highly hallucinatory responses. We therefore argue that proactive interaction should be redefined with a third action: ask, allowing models to actively ask for missing information. To study when and what models should ask before answering, we introduce AskStream, the first multi-turn benchmark spanning video and user uncertainty for streaming video understanding, with four task categories and eight subtasks. It contains 438 videos with 2,714 manually annotated frame-level time windows across three types: wait, ask, and answer. Across both multiple-choice and open-ended settings, even the strongest model attains only 52.18% on our proposed Ask-F1 metric, highlighting substantial limitations in proactive information seeking under uncertainty.
