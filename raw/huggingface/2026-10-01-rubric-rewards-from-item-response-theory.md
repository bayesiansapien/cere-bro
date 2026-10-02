---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.349558+05:30
arxiv_id: 2609.35646
url: https://huggingface.co/papers/2609.35646
arxiv_url: https://arxiv.org/abs/2609.35646
date: 2026-10-01
---

# Rubric Rewards from Item Response Theory

Many language tasks have no single answer that can be checked automatically. Rubrics provide criteria for judging responses to these tasks. For reinforcement learning, the resulting verdicts must be combined into a scalar reward. A common approach sums the points assigned to satisfied criteria. Distinct verdict patterns can thus receive the same reward, and the fixed points encode how much each criterion should count, not how strongly its verdict distinguishes the current rollouts. Beyond this aggregation problem, judging the full rubric needs more judge requests as the criterion count grows. To address these limitations, Rubric Response Theory (RRT) measures quality and selects criteria when rubric criteria are monotone indicators of a shared target. Rather than adding assigned points, RRT uses a two parameter item response model that treats the verdict pattern as evidence about scalar quality specific to the rubric. Under this model, its likelihood score maximizes the local signal-to-noise ratio for quality. Its Response Parameter Network (RPN) reads the prompt and criterion text to predict criterion difficulty and discrimination. As the policy distribution changes during training, RRT uses online expectation maximization to update the RPN from current rollout verdicts. With Qwen3.5-4B as the policy, RRT's macro criterion score across Medical, Science, Rubrics as Rewards Science, and RubricBench is 1.7 points above that of group relative policy optimization (GRPO). On hard and very hard criteria in Medical and Science, RRT gains 2.8 to 5.6 points over GRPO. At half the criterion budget, adaptive Fisher selection with a frozen RPN keeps the macro criterion score across four datasets within 0.1 points of GRPO with full judging. These results show RRT can reduce judge requests while remaining competitive with GRPO.
