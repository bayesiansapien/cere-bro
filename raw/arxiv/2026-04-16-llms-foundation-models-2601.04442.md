---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2601.04442
category: cs.CL
concept: llms-foundation-models
url: https://arxiv.org/abs/2601.04442
published: 2026-04-16
authors: Xingjian Diao, Zheyuan Liu, Chunhui Zhang
---

# Addressing Overthinking in Large Vision-Language Models via Gated Perception-Reasoning Optimization

**arXiv:** https://arxiv.org/abs/2601.04442
**Authors:** Xingjian Diao, Zheyuan Liu, Chunhui Zhang

## Abstract

arXiv:2601.04442v2 Announce Type: replace-cross  Abstract: Large Vision-Language Models (LVLMs) have exhibited strong reasoning capabilities through chain-of-thought mechanisms that generate step-by-step rationales. However, such slow-thinking approaches often lead to overthinking, where models produce excessively verbose responses even for simple queries, resulting in test-time inefficiency and even degraded accuracy. Prior work has attempted to mitigate this issue via adaptive reasoning strategies, but these methods largely overlook a fundamental bottleneck: visual perception failures. We argue that stable reasoning critically depends on low-level visual grounding, and that reasoning errors often originate from imperfect perception rather than insufficient deliberation. To address this limitation, we propose Gated Perception-Reasoning Optimization (GPRO), a meta-reasoning controller that dynamically routes computation among three decision paths at each generation step: a lightweight fast path, a slow perception path for re-examining visual inputs, and a slow reasoning path for internal self-reflection. To learn this distinction, we derive large-scale failure attribution supervision from approximately 790k samples, using teacher models to distinguish perceptual hallucinations from reasoning errors. We then train the controller with multi-objective reinforcement learning to optimize the trade-off between task accuracy and computational cost under uncertainty. Experiments on five benchmarks demonstrate that GPRO substantially improves both accuracy and efficiency, outperforming recent slow-thinking methods while generating significantly shorter responses.
