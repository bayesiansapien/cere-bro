---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.32183
url: https://huggingface.co/papers/2611.32183
arxiv_url: https://arxiv.org/abs/2611.32183
date: 2026-11-25
---

# ThinkMorph-SSL: Scaling Interleaved Multimodal Reasoning with Pretext Tasks

People reason with pictures as well as words. Interleaved multimodal reasoning gives models a similar way to solve problems by creating intermediate images and using them to guide further reasoning. Training models with this ability usually relies on task-specific demonstrations, which are difficult to collect. We introduce ThinkMorph-SSL, a two-stage training recipe that uses images themselves as a source of supervision. The first stage, pretext reasoning, converts visual pretext tasks, such as image colorization and denoising, into instruction-free interleaved traces. Models describe a corrupted or transformed image, generate a restored or canonical image, and interpret the result. The second stage uses automatically constructed demonstrations for question-driven instruction tuning. At the same instruction-tuning budget, models trained with pretext reasoning outperform those trained with instruction tuning alone. The full recipe improves over the base model by an average of 11.33 accuracy points across twelve benchmarks. These results show that supervision derived from images can build the visual skills needed for interleaved reasoning and improve learning from task-specific demonstrations.
