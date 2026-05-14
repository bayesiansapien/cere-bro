---
source: farmer/huggingface
farmed: 2026-05-14T10:39:11Z
arxiv_id: 2605.10899
url: https://huggingface.co/papers/2605.10899
arxiv_url: https://arxiv.org/abs/2605.10899
date: 2026-05-13
---

# RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards

Training deep research agents, namely systems that plan, search, evaluate evidence, and synthesize long-form reports, pushes reinforcement learning beyond the regime of verifiable rewards. Their outputs lack ground-truth answers, their trajectories span many tool-augmented decisions, and standard post-training offers little mechanism for turning past attempts into reusable experience. In this work, we argue that rubrics should serve not merely as final-answer evaluators, but as the shared interface that structures policy execution, judge feedback, and agent memory. Based on this view, we introduce RubricEM, a rubric-guided reinforcement learning framework that combines stagewise policy decomposition with reflection-based meta-policy evolution. RubricEM first makes research trajectories stage-aware by conditioning planning, evidence gathering, review, and synthesis on self-generated rubrics. It then assigns credit with Stage-Structured GRPO, which uses stagewise rubric judgments to provide denser semantic feedback for long-horizon optimization. In parallel, RubricEM trains a shared-backbone reflection meta-policy that distills judged trajectories into reusable rubric-grounded guidance for future attempts. The resulting RubricEM-8B achieves strong performance across four long-form research benchmarks, outperforming comparable open models and approaching proprietary deep-research systems. Beyond final performance, we perform thorough analyses to understand the key ingredients of RubricEM.
