---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.503578+00:00
arxiv_id: 2610.17928
url: https://huggingface.co/papers/2610.17928
arxiv_url: https://arxiv.org/abs/2610.17928
date: 2026-10-14
---

# Learning How to Remember: Memory Modality Selection for GUI Agents

Recent advances in vision-language models (VLMs) have substantially improved the capabilities of GUI agents, while memory augmentation has emerged as a promising approach for reusing knowledge from past interactions. However, existing memory augmented GUI agents typically adopt a fixed representation strategy, providing retrieved experience as a static modality. It remains unclear whether a single memory modality is consistently optimal, or how modality preference changes across interaction steps. In this work, we conduct a systematic study of memory modality in VLM based GUI agents. Across GUI benchmarks, we find that the preferred memory representation is strongly step dependent. Motivated by the finding, we introduce SwitchMem, a routing framework that dynamically selects between textual and visual memory representations at each step. Across three GUI benchmarks, SwitchMem outperforms memory augmented baselines that rely on static memory representations. Our findings validate our claim that memory modality is a step dependent decision rather than a fixed design choice. Code and project resources are available at https://txxnrd.github.io/switchmem
