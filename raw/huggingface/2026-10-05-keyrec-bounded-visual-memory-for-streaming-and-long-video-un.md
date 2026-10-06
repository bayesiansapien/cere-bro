---
source: farmer/huggingface
farmed: 2026-10-06T11:30:06.338949+05:30
arxiv_id: 2609.32182
url: https://huggingface.co/papers/2609.32182
arxiv_url: https://arxiv.org/abs/2609.32182
date: 2026-10-05
---

# KeyRec: Bounded Visual Memory for Streaming and Long-Video Understanding

Vision-language models are increasingly used to understand long videos and continuous streams. However, dense visual tokens accumulate with video duration, making long-context inference prohibitively expensive. Existing training-free visual-token selection methods reduce this cost by retaining informative tokens, but may lose coherent event evidence and fail to distinguish detailed recent observations from long-range history. We propose KeyRec, a training-free framework for constructing bounded visual memory. During query-agnostic writing, KeyRec preserves fine-grained recent observations in a visual cache and organizes historical evidence into a structured event bank. Candidate events are proposed according to their novelty relative to previously stored events and maintained through an online add--merge--evict update. When a question arrives, a text-only router adaptively allocates a fixed readout budget between recent and event memory, without reprocessing historical frames. KeyRec operates on model-facing visual embeddings and supports both modular encoder--projector VLMs and the encoder- and projector-free NEO-ov architecture. Across four streaming and long-video benchmarks and three VLM backbones, KeyRec achieves the best compressed performance in 13 of 15 settings using only 10\% of the dense decoder-facing visual-token budget. It outperforms the strongest compressed baseline by 2.21--18.37 points on real-time questions, achieves the best compressed result in five of six long-video settings, and performs best in every NEO-ov 2B setting.
