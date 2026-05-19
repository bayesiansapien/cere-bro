---
source: farmer/huggingface
farmed: 2026-05-19T09:55:00.432604+00:00
arxiv_id: 2605.18678
url: https://huggingface.co/papers/2605.18678
arxiv_url: https://arxiv.org/abs/2605.18678
date: 2026-05-19
---

# Lance: Unified Multimodal Modeling by Multi-Task Synergy

We present Lance, a lightweight native unified model supporting multimodal understanding, generation, and editing for both images and videos. Rather than relying on model capacity scaling or text-image-dominant designs, Lance explores a practical paradigm for unified multimodal modeling via collaborative multi-task training. It is grounded in two core principles: unified context modeling and decoupled capability pathways. Specifically, Lance is trained from scratch and employs a dual-stream mixture-of-experts architecture on shared interleaved multimodal sequences, enabling joint context learning while decoupling the pathways for understanding and generation. We further introduce modality-aware rotary positional encoding to mitigate interference among heterogeneous visual tokens and boost cross-task alignment. During training, Lance adopts a staged multi-task training paradigm with capability-oriented objectives and adaptive data scheduling to strengthen both semantic comprehension and visual generation performance. Experimental results demonstrate that Lance substantially outperforms existing open-source unified models in image and video generation, while retaining strong multimodal understanding capabilities. The homepage is available at https://lance-project.github.io.
