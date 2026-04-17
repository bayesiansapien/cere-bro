---
source: farmer/huggingface
farmed: 2026-04-17T07:40:59Z
arxiv_id: 2603.27844
url: https://huggingface.co/papers/2603.27844
arxiv_url: https://arxiv.org/abs/2603.27844
date: 2026-04-17
---

# Model Capability Dominates: Inference-Time Optimization Lessons from AIMO 3

Majority voting over multiple LLM attempts improves mathematical reasoning, but correlated errors limit the effective sample size. A natural fix is to assign different reasoning strategies to different voters. The approach, Diverse Prompt Mixer, is tested on the AIMO 3 competition: 3 models, 23+ experiments, 50 IMO-level problems, one H100 80 GB, 5-hour limit. Every prompt-level intervention fails. High-temperature sampling already decorrelates errors; weaker strategies reduce accuracy more than they reduce correlation. Across an 8-point capability gap at equal N=8 and every optimization tested, model capability dominates. The gap between the best majority-vote score (42/50) and pass@20 (~45.5) is selection loss, not prompt loss. A verifier-based selector could close it. Prompt engineering cannot.
