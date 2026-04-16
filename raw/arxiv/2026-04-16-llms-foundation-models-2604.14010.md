---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.14010
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.14010
published: 2026-04-16
authors: Zekai Lin, Chao Xue, Di Liang
---

# Parameter Importance is Not Static: Evolving Parameter Isolation for Supervised Fine-Tuning

**arXiv:** https://arxiv.org/abs/2604.14010
**Authors:** Zekai Lin, Chao Xue, Di Liang

## Abstract

arXiv:2604.14010v1 Announce Type: new  Abstract: Supervised Fine-Tuning (SFT) of large language models often suffers from task interference and catastrophic forgetting. Recent approaches alleviate this issue by isolating task-critical parameters during training. However, these methods represent a static solution to a dynamic problem, assuming that parameter importance remains fixed once identified. In this work, we empirically demonstrate that parameter importance exhibits temporal drift over the course of training. To address this, we propose Evolving Parameter Isolation (EPI), a fine-tuning framework that adapts isolation decisions based on online estimates of parameter importance. Instead of freezing a fixed subset of parameters, EPI periodically updates isolation masks using gradient-based signals, enabling the model to protect emerging task-critical parameters while releasing outdated ones to recover plasticity. Experiments on diverse multi-task benchmarks demonstrate that EPI consistently reduces interference and forgetting compared to static isolation and standard fine-tuning, while improving overall generalization. Our analysis highlights the necessity of synchronizing isolation mechanisms with the evolving dynamics of learning diverse abilities.
