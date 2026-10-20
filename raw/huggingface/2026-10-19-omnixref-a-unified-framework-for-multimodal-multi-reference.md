---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.22744
url: https://huggingface.co/papers/2610.22744
arxiv_url: https://arxiv.org/abs/2610.22744
date: 2026-10-19
---

# OmniXRef: A Unified Framework for Multimodal Multi-Reference Video Editing

Creative intent in video editing can be expressed through text instructions (e.g., "remove the people"), image references (e.g., subject appearance), video references (e.g., camera movement), or a combination of the above. We introduce OmniXRef, a unified framework for multimodal multi-reference video editing that allows users to combine variable numbers of text, image, and video references to control diverse attributes of a source video. We first devise a unified input design with a reference-bank interface and introduce R^2-RoPE to support generalization to more references. Then our model, OmniXRef-Model, uses a single-stream diffusion transformer to jointly process the source video and multimodal context from an MLLM in an interleaved sequence. To address the scarcity of training data for video-reference editing, we construct OmniXRef-Data using synthesis pipelines for different editing tasks and combinations of references. We use curriculum learning to progressively increase task complexity and resolution. To support systematic evaluation of video as a control modality, we introduce OmniXRef-Bench, a benchmark for video-reference attribute transfer across Camera, Motion, Content, Style, and Visual Effects (VFX). Comprehensive evaluations show that our OmniXRef-Model outperforms task-specific baselines and commercial models.
