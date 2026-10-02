---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.348314+05:30
arxiv_id: 2609.32720
url: https://huggingface.co/papers/2609.32720
arxiv_url: https://arxiv.org/abs/2609.32720
date: 2026-10-01
---

# BiasReducer: Adaptive Bias Mitigation for Reward Models

Reward models score responses from large language models (LLMs) and guide LLM training toward human preferences. However, reward models can favor superficial attributes such as length or confidence, leading LLMs to produce higher-scoring but not more correct responses. Existing mitigation methods either retrain the reward model or apply a fixed correction to one known bias, such as a preference for longer responses. Retraining requires additional data and computational resources, while existing editing methods require the target bias to be specified in advance and use a fixed edit for that bias. To this end, we propose BiasReducer, a lightweight framework that edits only the linear reward head and selects the relevant edits for each new dataset. First, BiasReducer uses a sparse autoencoder (SAE)-style encoder to learn which attributes (e.g., length and confidence) the reward model is sensitive to. Second, it learns how to reduce the reward model's dependence on each attribute by determining which direction to adjust the reward head and how much to adjust it. Third, for a new dataset, it ranks the attributes by their influence on reward scores, selects the relevant ones, and edits the reward model accordingly. BiasReducer consistently improves reward-model robustness to biases toward superficial response attributes. Across five reward models, BiasReducer-M improves the three benchmarks by 8.3, 18.0, and 6.9 percentage points on average, outperforming the two training-based baselines. The gains transfer downstream, reducing unnecessary verbosity and sycophancy while maintaining comparable judged quality.
