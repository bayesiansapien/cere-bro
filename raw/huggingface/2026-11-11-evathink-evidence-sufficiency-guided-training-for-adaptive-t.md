---
source: farmer/huggingface
farmed: 2026-11-12T12:57:12.903698+05:30
arxiv_id: 2611.13907
url: https://huggingface.co/papers/2611.13907
arxiv_url: https://arxiv.org/abs/2611.13907
date: 2026-11-11
---

# EVAThink: Evidence Sufficiency-Guided Training for Adaptive Thinking in Video Understanding

Under a fixed frame budget, video understanding with vision-language models (VLMs) depends on whether the sampled frames provide sufficient evidence for the question. Sufficient frame evidence supports direct answering, whereas less informative observations may benefit from reasoning that connects the available cues. We introduce EVAThink, which enhances video understanding through evidence sufficiency-guided training for adaptive thinking. First, Recoverable Evidence Gap Mining constructs evidence-dense and evidence-sparse video views that share the same question and answer under an identical frame budget. It retains pairs where sparse views yield lower direct-answer accuracy than dense views but benefit from explicit reasoning, providing supervision for response-mode selection. Second, Evidence-Guided Two-Stage Reinforcement Learning uses stage-specific rewards to guide training with evidence-based mode preferences and then refine response efficiency, while first-token advantage regularization mitigates mode collapse. Trained on only 6.7K curated samples, EVAThink consistently improves upon the base model across video understanding benchmarks under both 32- and 64-frame budgets, while outperforming strong baselines on average. The code, model, and datasets are available at https://github.com/ChangtiWu/EVAThink{EVAThink}.
