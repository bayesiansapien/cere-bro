---
source: farmer/huggingface
farmed: 2026-09-18T16:13:44.923131+00:00
arxiv_id: 2609.12397
url: https://huggingface.co/papers/2609.12397
arxiv_url: https://arxiv.org/abs/2609.12397
date: 2026-09-18
---

# UFO: Chain-of-Evaluation for Omni-Condition Alignment in Multi-Modal Image Generation

Multi-modal image generation, particularly subject-driven customization, has garnered growing attention in recent years. Despite the rapid advancement of generative models, their evaluation remains largely lagging. Existing methods, whether embedding-based or Multi-modal Large Language Model (MLLM)-based, evaluate alignment with each modal condition in isolation, which contradicts the simultaneous condition alignment objective of multi-modal image generation, leading to poor consistency with human judgments. To address this challenge, we propose UFO, the first unified framework for omni-condition alignment simultaneous evaluation. Specifically, UFO introduces a novel Atomized Chain-of-Evaluation paradigm, i.e., it first decomposes omni-condition alignment into a sequential chain of fine-grained, disentangled Atomic Evaluation Units (AEUs), categorizes them into distinct modality-relevance classes, and then employs general or dedicated functional calls for accurate verification of different AEU types. Experimental results demonstrate that UFO achieves the highest correlation with human evaluation preferences, delivering an average improvement of 15.25%. Furthermore, we present UFO-Bench, a dedicated benchmark designed to holistically evaluate the performance of existing customization models under the diverse mutual interactions of textual and visual conditions.
