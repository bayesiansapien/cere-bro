---
source: farmer/huggingface
farmed: 2026-07-31T19:58:50.731985
arxiv_id: 2607.26769
url: https://huggingface.co/papers/2607.26769
arxiv_url: https://arxiv.org/abs/2607.26769
date: 2026-07-31
---

# See2Think: Do Multimodal Models Really Use Intermediate Visual States?

Multimodal large language models increasingly use sketches, annotations, tools, and intermediate images during reasoning, but it remains unclear whether they truly rely on these visual states. Existing benchmarks are limited both by task collections with narrow coverage or partially text-solvable samples and by evaluations that emphasize final answers without diagnosing how intermediate visual states are generated, rendered, and used. We introduce See2Think, a unified evaluation framework comprising See2ThinkBench and Visual Action-of-Thought (VAoT). See2ThinkBench contains 1,200 open-ended, visually dependent problems across 12 task categories spanning 2D structured, 3D scene, and real-world reasoning. VAoT records textual thoughts, visual actions, rendered states, and subsequent reasoning under four controlled inference settings. Evaluating representative proprietary and open-source multimodal models, we find that visual reasoning is strongly model- and environment-dependent, with no single setting consistently dominating across tasks. Process analysis further shows that models usually select relevant visual operations, while faithful rendering remains the clearest bottleneck and high feedback uptake does not necessarily translate into accuracy gains. Under task-relevant corrupted feedback, models exhibit behavioral dependence on visual states, with accuracy dropping by over 10 percentage points in controlled interventions.
