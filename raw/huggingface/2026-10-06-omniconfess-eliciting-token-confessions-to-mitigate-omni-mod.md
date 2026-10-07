---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.02999
url: https://huggingface.co/papers/2610.02999
arxiv_url: https://arxiv.org/abs/2610.02999
date: 2026-10-06
---

# OmniConfess: Eliciting Token Confessions to Mitigate Omni-Modal Hallucination

Omni-modal large language models (OmniLLMs) unify text, images, audio, and video, yet hallucinate when generation relies on the wrong evidence. Existing inference-time methods can reduce hallucinations, but rarely reveal which evidence sustains a generated commitment. We introduce OmniConfess, a training-free method for mitigating omni-modal hallucinations. It fixes a candidate response and re-scores it at token resolution under controlled channel-wise evidence interventions, producing a structured token-by-channel confession that reveals the response's evidential dependence. OmniConfess uses this confession to preserve grounded content and correct commitments driven by irrelevant or contradictory evidence. To evaluate OmniConfess, we construct OmniHalluBench, a 3,540-example benchmark built from six datasets spanning text, image, audio, and video settings and both judgment and free-form generation. Experiments show that OmniConfess mitigates hallucinations across heterogeneous modality and task settings. Our code and benchmark are publicly available at https://github.com/RongHuiQiang/OmniConfess.
