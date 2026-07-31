---
source: farmer/huggingface
farmed: 2026-07-31T19:58:50.731985
arxiv_id: 2607.28509
url: https://huggingface.co/papers/2607.28509
arxiv_url: https://arxiv.org/abs/2607.28509
date: 2026-07-31
---

# RefCaptioner: Multi-Reference Image-Grounded Video Captioning

Existing video captioning models generate natural descriptions of video content but cannot explicitly ground local visual elements to multiple reference images. We introduce multi-reference image-grounded video captioning, a new task requiring factual video descriptions with phrase-level reference grounding, and propose RefCaptioner, a two-stage post-training framework for this task. RefCaptioner combines mixed-data SFT with Hierarchical Coverage-Discounted GRPO to jointly improve reference selection, phrase-level binding, distractor rejection, and cross-reference consistency while preserving general video-captioning ability. To support training, we construct a corpus containing 20,000 videos and 171,354 reference images. We further introduce MRVBench, a benchmark for evaluating caption factuality and multi-reference grounding on both real-world and AI-generated videos. Experiments show that RefCaptioner achieves the best overall performance among the open-source models while remaining competitive on standard video captioning benchmarks. Human evaluation further confirms that its captions are preferred by annotators and enable more source-faithful video reconstruction with both open-source and proprietary video generators.
