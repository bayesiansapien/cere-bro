---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.32100
url: https://huggingface.co/papers/2611.32100
arxiv_url: https://arxiv.org/abs/2611.32100
date: 2026-11-25
---

# EEGJev: A System One Decision Model and Benchmark for Multi-Task EEG Question Answering

A single electroencephalographic (EEG) recording can support multiple decoding tasks. Fixed-label tests cannot show how EEG foundation models handle changing questions or options. We introduce EEGJev, a fast decision model that scores candidate answers in one pass. Our benchmark, EEGJev-Bench, covers six question types across 19 public EEG sources. We held the recording and options fixed while switching between questions about attributes paired during training, such as facial expression and the hand participants were asked to use. Across 13 test sources, EEGJev selected a label for the requested attribute with 99.70% accuracy (49.20% under uniform choice). Balanced accuracy for the specific answer was 62.04%. Its 95th-percentile response time was shorter than NeuroLM's on matched validation questions answered individually. EEGJev lets users switch decoding targets by changing the question. With EEGJev-Bench, researchers can test whether new decoders follow the question more reliably, identify the correct answer more often, or both.
