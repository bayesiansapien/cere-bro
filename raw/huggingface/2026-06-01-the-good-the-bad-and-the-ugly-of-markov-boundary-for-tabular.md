---
source: farmer/huggingface
farmed: 2026-06-01T09:02:45Z
arxiv_id: 2605.29411
url: https://huggingface.co/papers/2605.29411
arxiv_url: https://arxiv.org/abs/2605.29411
date: 2026-06-01
---

# The Good, the Bad, and the Ugly of Markov Boundary for Tabular Prediction

Under standard graphical assumptions, the Markov boundary of a target variable is the smallest set of features that renders every other feature redundant. Once the boundary is observed, the target is conditionally independent of the rest of the table. This is a tempting object for tabular prediction, since it names exactly the columns a model should need. Yet modern regressors are still trained on the full feature set. We ask whether the Markov boundary is genuinely useful for prediction on SCM3K, a 3,450-task synthetic SCM benchmark with feature counts from 40 to 1000 and six SCM families, evaluated with six regressors. The answer is more nuanced than the theory suggests. Restricting a regressor to the oracle boundary often improves prediction substantially, and the improvement grows as the feature space becomes larger and sparser. But the natural pipeline of recovering the boundary with causal discovery and training on the recovered mask does not deliver.
