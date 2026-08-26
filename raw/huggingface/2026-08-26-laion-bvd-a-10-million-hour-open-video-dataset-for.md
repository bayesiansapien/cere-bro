---
source: farmer/huggingface
farmed: 2026-08-26T12:46:47.908232
arxiv_id: 2608.24845
url: https://huggingface.co/papers/2608.24845
arxiv_url: https://arxiv.org/abs/2608.24845
date: 2026-08-26
upvotes: 1
---

# LAION-BVD: A 10-Million-Hour Open Video Dataset for Multimodal Pre-training

We present LAION-BVD, a large-scale open video dataset for multimodal learning, which contains 1.3B platform-specific video URLs collected from CommonCrawl. From these, we download 80M videos with a total duration of 10 million hours. The dataset is designed for multimodal pre-training across the video, audio, and image modalities. Using content-aware scene detection, we extract clips for which we synthetically generate video and audio captions. Models trained on these data achieve competitive performance on standard video-text and audio-text benchmarks, with consistent improvements as training or model scale increases. Additionally, we explore video frames as an alternative source of image-text data by extracting scene-changing frames. These frames exhibit a visual distribution distinct from standard web image corpora, and models trained on this dataset achieve strong image-text retrieval performance. We release LAION-BVD to the research community. It significantly expands open access to multimodal videos at an unprecedented scale.
