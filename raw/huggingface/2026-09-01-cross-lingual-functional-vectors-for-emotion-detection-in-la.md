---
source: farmer/huggingface
farmed: 2026-09-01T08:46:18.970698+00:00
arxiv_id: 2608.29613
url: https://huggingface.co/papers/2608.29613
arxiv_url: https://arxiv.org/abs/2608.29613
date: 2026-09-01
---

# Cross-lingual Functional Vectors for Emotion Detection in Large Language Models

Function vectors (FVs) have recently emerged as a promising mechanism for steering the behavior of large language models (LLMs) by injecting task-specific latent direction representations derived from in-context demonstrations. While prior studies have shown that FVs can recover task behavior in structured in-context learning settings, their effectiveness on semantically complex tasks and their ability to generalize across languages remain underexplored. We investigate the cross-lingual transferability of FVs using multilingual multi-label emotion recognition as a challenging semantic classification benchmark. Specifically, we examine whether FVs extracted from a source language can steer task behavior in another language under both standard clean and perturbed zero-shot settings without providing demonstrations during inference. Across diverse cross-lingual settings, applying FVs substantially improves performance, suggesting that FVs capture language-agnostic, task-relevant signals rather than purely language-specific lexical patterns, and highlighting their potential as a lightweight and transferable mechanism for multilingual task adaptation. We observe that each LLM exhibits a relatively stable optimal range of attention heads for constructing effective FVs, and the pattern remains consistent across languages. In addition, FVs can partially replicate the task-steering effects of standard few-shot in-context learning while avoiding the computational overhead of processing multiple demonstrations, making them effective for large-scale practical applications. Our code is available at https://github.com/yingjie7/cross_lingual_fvs.
