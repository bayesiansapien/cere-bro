---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.308726+05:30
arxiv_id: 2610.06505
url: https://huggingface.co/papers/2610.06505
arxiv_url: https://arxiv.org/abs/2610.06505
date: 2026-10-08
---

# Improving Proactive AI Assistance with Hierarchical Procedural Understanding

Proactive AI assistants continuously observe a user's activity and decide whether to provide new guidance or remain silent. They should provide appropriate guidance for the task, determine when to provide the next guidance based on task progress, and adjust the guidance level to the user's expertise and needs. Supporting these capabilities requires training and evaluation data that reflect procedural structure and capture how guidance should adapt to task progress and user needs. However, existing datasets either focus on detection-based proactive understanding or provide procedural guidance at a fixed granularity. Fixed-granularity guidance provides limited information about fine-grained progress and broader procedural context, making it difficult to determine completion and adapt guidance granularity. To address these limitations, we introduce the ProactiveCoach suite, comprising ProactiveCoach-Instruct for training, ProactiveCoachBench for evaluation, and fine-tuned VLMs with an adaptive guidance system. ProactiveCoach-Instruct provides hierarchically structured guidance at the phase, step, and action levels for learning task progress and procedural context. ProactiveCoachBench evaluates whether models provide appropriate guidance at the right time across different guidance levels and adapt when the requested level changes. We fine-tune pretrained VLMs on ProactiveCoach-Instruct and demonstrate its effectiveness across backbones. Compared with fixed-granularity supervision, hierarchical supervision improves overall performance across backbones by up to 9.6%p. We further build an adaptive guidance system by combining our fine-tuned model with a lightweight guidance router. Without additional fine-tuning, our system outperforms the in-context adaptation baseline by 57.1%p across four guidance-level transitions. Our project page is available at https://jinsuby.github.io/ProactiveCoach/.
