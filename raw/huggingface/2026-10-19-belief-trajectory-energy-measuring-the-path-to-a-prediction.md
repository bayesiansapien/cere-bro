---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.05114
url: https://huggingface.co/papers/2610.05114
arxiv_url: https://arxiv.org/abs/2610.05114
date: 2026-10-19
---

# Belief-Trajectory Energy: Measuring the Path to a Prediction

Large language models (LLMs) progressively revise their predictions across Transformer layers, yet we typically observe only the final output, discarding the trajectory through which it is formed. We introduce Belief-Trajectory Energy(BTE), a model-grounded measure that characterizes an input through the layerwise predictive revisions it induces in a model. By mapping intermediate states into a shared predictive space, BTE provides a principled measure of belief change that can be summarized as either a scalar or a structured depth profile. Theoretically, we show that local BTE corresponds to predictive revision under the Fisher-Rao geometry, while the sequence of revisions captures information beyond the initial-to-final belief change. Empirically, scalar BTE provides a model-relative signal of difficulty across diverse reasoning tasks, while richer BTE representations support human-LLM review detection and fine-grained generator attribution, reaching up to 0.998 macro-AUROC and 95.6% eight-way attribution accuracy. Further analysis shows that BTE develops throughout pretraining and is selectively reshaped by targeted training, demonstrating that the resulting measurement reflects what the scoring model has learned. Together, our results establish belief trajectories as a principled model-grounded signal and suggest a broader perspective in which learned models can themselves serve as instruments for characterizing the data they process. More demonstrations can be found at https://yingjiahao14.github.io/BTE-web/.
