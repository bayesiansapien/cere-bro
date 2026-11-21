---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.381841+00:00
arxiv_id: 2611.26409
url: https://huggingface.co/papers/2611.26409
arxiv_url: https://arxiv.org/abs/2611.26409
date: 2026-11-20
---

# WeMM-Video: Pushing the Frontiers of Open-Source Omni-Modal Video Understanding

Video understanding, particularly with accompanying audio, remains a central challenge in multimodal intelligence. In this report, we introduce WeMM-Video, a family of Chinese-English bilingual omni-modal foundation models spanning 2B, 4B, 9B, and 35B-A3B variants. Centering on joint audio-visual perception and reasoning, WeMM-Video unifies text, image, audio, and video processing within a hybrid-thinking paradigm, seamlessly supporting both a non-thinking instruct mode for fast, direct responses and a thinking mode for explicit step-by-step reasoning. The models are trained on a large-scale multimodal corpus of approximately 1.2 trillion tokens through progressive pre-training and a multi-stage post-training pipeline incorporating multi-teacher OPD, anti-repetition MrDPO, and specialist RL. Evaluated across more than 120 benchmarks, WeMM-Video demonstrates superior performance in omni-modal video understanding and reasoning, while maintaining highly competitive capabilities across general audio, silent video, image, and text tasks. Specifically, in omni-modal video evaluations, our flagship WeMM-Video-35B-A3B establishes a new open-source state of the art, substantially outperforming proprietary models such as Qwen3.5-Omni-Flash and Seed2.0-Mini-0428 while narrowing the gap with the strong Gemini-3.0-Flash, and our compact WeMM-Video-9B surpasses the larger open-source Qwen3-Omni-30B-A3B-Instruct. We publicly release the WeMM-Video family along with our evaluation and reproduction pipeline to foster further research and development in the open-source community.
