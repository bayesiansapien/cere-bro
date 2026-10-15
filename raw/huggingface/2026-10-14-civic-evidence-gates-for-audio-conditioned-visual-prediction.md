---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.508322+00:00
arxiv_id: 2610.15327
url: https://huggingface.co/papers/2610.15327
arxiv_url: https://arxiv.org/abs/2610.15327
date: 2026-10-14
---

# CIViC: Evidence Gates for Audio-Conditioned Visual Prediction on Proxy Tasks

Removing audio can shift a visual predictor's output without showing whether the task uses the intended audio information. We introduce Conditional Input and Visual Interpretation Checks (CIViC), a four-gate protocol that links an interpretation to an intervention, held-out task comparison, or endpoint control. We demonstrate CIViC on actor-disjoint face-raster tests, a synthetic audio-feature mixture, and source-video-disjoint SpeakerVid proxy tasks. In the static face-raster test, cross-actor audio replacement meets the registered detection rule with a small effect; on a separate temporal endpoint, constant-audio fits score better than audio-trained fits in four matched seeds. In the synthetic mixture, the condition-augmented fit has higher 1,000-step RMSE than the audio-only fit (0.1807 vs. 0.1707), with the gap shrinking during training. In the SpeakerVid proxy, the five-feature-zero fit (five low-level audio summaries zeroed; identity, dialogue, and condition inputs retained) has lower whole-frame grayscale RMSE than aligned audio across four held-out conditions and five paired seeds, while aligned audio has lower segment-drift error. The results show that output activation, held-out error, and endpoint controls support different interpretations across these proxy tasks.
