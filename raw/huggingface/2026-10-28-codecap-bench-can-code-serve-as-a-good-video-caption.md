---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.994166+05:30
arxiv_id: 2610.37341
url: https://huggingface.co/papers/2610.37341
arxiv_url: https://arxiv.org/abs/2610.37341
date: 2026-10-28
---

# CodeCap-Bench: Can Code Serve as a Good Video Caption?

Video captioning aims to preserve visual information through compact descriptions, predominantly using natural language. However, precisely expressing fine-grained spatial structures and temporal dynamics in natural language often leads to lengthy and potentially ambiguous descriptions. In this work, we explore Code as Video Caption, a paradigm where executable programs serve as a complementary representation of visual content through graphical primitives, layout rules, and functions of time. To examine whether code captions effectively preserve video information, we compare them with natural language captions on downstream question answering and video reconstruction tasks. Our results show that code captions achieve superior reasoning accuracy and reconstruction fidelity. Despite these advantages, realizing the potential of code captioning depends on whether current multimodal large language models (MLLMs) can generate faithful code captions. To systematically assess this capability, we introduce CodeCap-Bench, which comprises 323 videos spanning five categories of structured 2D content, along with fine-grained annotations and a multi-level evaluation framework. Extensive experiments reveal that while leading proprietary MLLMs demonstrate promising code captioning capabilities, they still struggle to faithfully capture complex temporal dynamics, with open-source models lagging substantially behind.
