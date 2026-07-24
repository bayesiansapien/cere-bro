---
source: farmer/huggingface
farmed: 2026-07-24T23:47:01.610703+05:30
arxiv_id: 2607.21051
url: https://huggingface.co/papers/2607.21051
arxiv_url: https://arxiv.org/abs/2607.21051
date: 2026-07-24
---

# Sample-Efficient Learning from Agent Experience

Real-world agent learning is often constrained by costly environment interactions, such as running time-consuming experiments or obtaining human feedback. In-context learning offers a highly sample-efficient way for agents to learn from their own interaction histories, but its gains disappear once that experience is removed from the context. Separately, context distillation provides a mechanism for internalizing contextual information into model weights. However, applying it to agents' interaction histories without sacrificing environment sample efficiency remains underexplored. We term this problem Experience Distillation and develop an implementation that requires no further environment interaction beyond the collected experience. Experiments on 749 curated software-engineering tasks and six text-adventure games show that it retains at least 64.8\% of the gains from in-context learning across both domains, whereas direct supervised fine-tuning on the collected experience recovers only 3.8\%. Compared with classical reinforcement-learning baselines, in-context learning from trial-and-error experience followed by Experience Distillation matches their performance with at least \(9.6\times\) fewer environment samples.
