---
source: farmer/huggingface
farmed: 2026-05-22T10:21:55.060746+00:00
arxiv_id: 2605.21431
url: https://huggingface.co/papers/2605.21431
arxiv_url: https://arxiv.org/abs/2605.21431
date: 2026-05-21
---

# iTryOn: Mastering Interactive Video Virtual Try-On with Spatial-Semantic Guidance

Video Virtual Try-On (VVT) aims to seamlessly replace a garment on a person in a video with a new one. While existing methods have made significant strides in maintaining temporal consistency, they are predominantly confined to non-interactive scenarios where models merely showcase garments. This limitation overlooks a crucial aspect of real-world apparel presentation: active human-garment interaction. To bridge this gap, we introduce and formalize a new challenging task: Interactive Video Virtual Try-On (Interactive VVT), where subjects in the video actively engage with their clothing. This task introduces unique challenges beyond simple texture preservation, including: (1) resolving the semantic ambiguity of interactions from standard pose information, and (2) learning complex garment deformations from video where interactive moments are sparse and brief. To address these challenges, we propose iTryOn, a novel framework built upon a large-scale video diffusion Transformer. iTryOn pioneers a multi-level interaction injection mechanism to guide the generation of complex dynamics. At the spatial level, we introduce a garment-agnostic 3D hand prior to provide fine-grained guidance for precise hand-garment contact, effectively resolving spatial ambiguity. At the semantic level, iTryOn leverages global captions for overall context and time-stamped action captions for localized interactions, synchronized via our novel Action-aware Rotational Position Embedding (A-RoPE). Extensive experiments demonstrate that iTryOn not only achieves state-of-the-art performance on traditional VVT benchmarks but also establishes a commanding lead in the new interactive setting, marking a significant step towards more dynamic and controllable virtual try-on experiences.
