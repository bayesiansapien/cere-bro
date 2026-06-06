---
source: farmer/huggingface
farmed: 2026-06-06T09:05:36Z
arxiv_id: 2606.04351
url: https://huggingface.co/papers/2606.04351
arxiv_url: https://arxiv.org/abs/2606.04351
date: 2026-06-06
---

# Video2LoRA: Parametric Video Internalization for Vision-Language Models

Processing video in vision-language models is expensive: each frame occupies hundreds of tokens, and inference cost scales with every frame and every repeated query. We introduce Video2LoRA, a method for parametric video internalization. A perceiver hypernetwork reads the intermediate representations produced layer-by-layer as a frozen VLM encodes a video, and generates a Low-Rank Adaptation (LoRA) adapter in a single forward pass. Unlike standard LoRA fine-tuning, which requires iterative gradient updates, Video2LoRA predicts these weights directly from the video. Trained for SmolVLM2 500M and 2.2B on video summarization and captioning, Video2LoRA enables the same frozen VLM to answer queries from the adapter alone, with zero visual tokens in its context at query time. Video2LoRA is statistically non-inferior and equivalent to direct video-in-context inference across all five captioning benchmarks at both model scales, and across seven of eight video question answering benchmark-scale pairings. Although trained only on 12 frames at 384px, it remains stable up to 1,024 frames and 1024px, where direct video-in-context inference often degenerates. Across this sweep, it reduces answer-time visual-token load by up to 1,500x and query TTFT by 6-80x, while preserving video-faithful outputs. We also find that independently generated adapters for non-overlapping video segments can compose in rank space, suggesting a path toward chunked long-video internalization.
