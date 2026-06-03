---
source: farmer/huggingface
farmed: 2026-06-03T06:14:02Z
arxiv_id: 2606.03603
url: https://huggingface.co/papers/2606.03603
arxiv_url: https://arxiv.org/abs/2606.03603
date: 2026-06-03
---

# World Models Meet Language Models: On the Complementarity of Concrete and Abstract Reasoning

World models and multimodal large language models (MLLMs) provide complementary capabilities for predicting future outcomes from static visual observations. World models can generate concrete visual rollouts of possible futures, while MLLMs can reason abstractly over questions, goals, and rules. However, generated rollouts are stochastic and may be visually plausible but task-incorrect, making it necessary to determine when visual simulation is useful, whether a rollout is credible, and how it should influence the final answer. We formulate this problem as controlled concrete reasoning, where a model learns to invoke, verify, and integrate visual future simulation alongside abstract reasoning. To study this setting, we construct two human-verified benchmarks, VRQABench for controllable spatial lookahead and OpenWorldQA for open-domain physical prediction, and propose Privileged-Future On-Policy Self-Distillation (PF-OPSD). During training, PF-OPSD uses ground-truth future videos and answers only as teacher-side privileged context to evaluate on-policy concrete-reasoning trajectories, while the deployable student never observes true futures at test time. Experimental results show that PF-OPSD outperforms baseline by 10.6% and 10.9% on VRQABench and OpenWorldQA, respectively, while increasing robustness to noisy or conflicting rollouts. Our code and dataset are available at https://github.com/yczhou001/PF-OPSD.
