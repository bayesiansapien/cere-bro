---
source: farmer/huggingface
farmed: 2026-11-06T05:50:41.306613+00:00
arxiv_id: 2611.04760
url: https://huggingface.co/papers/2611.04760
arxiv_url: https://arxiv.org/abs/2611.04760
date: 2026-11-05
---

# Koopman Generative Operators for Efficient Probabilistic Time-Series Forecasting

Probabilistic time-series forecasting requires models that simultaneously capture structured temporal dynamics, expressive uncertainty, and efficient inference, yet existing approaches fall short of this goal: latent dynamical models impose structure but rely on restrictive generation mechanisms, while modern generative methods such as diffusion and flow matching achieve flexibility at the cost of iterative and computationally expensive sampling. We introduce the Koopman Generative Operator (KGO), a probabilistic forecasting method that conceptualizes prediction as the evolution of structured uncertainty. KGO integrates three core components: (1) Koopman Patch Embedding (KoPE) for temporally consistent latent trajectory extrapolation; (2) Koopman Flow Matching (KoFM), which enables fast, single-step generation through a closed-form matrix exponential in a Koopman latent space, bypassing iterative sampling; and (3) an Adaptive Uncertainty Gate (AUG), which provides probabilistic forecasts by adapting uncertainty per-variable and per-horizon, corresponding to a learned decomposition of aleatoric uncertainty without manual tuning. By unifying these components, KGO achieves state-of-the-art accuracy on 13/17 ProbTS benchmarks in CRPS and 16/17 in NMAE. Further, by eliminating iterative sampling, KGO delivers at least a 25times reduction in inference time compared to iterative generative models. These results position KGO as a practical and principled framework that advances the accuracy-efficiency trade-off in probabilistic time-series forecasting, combining leading accuracy on the evaluated benchmarks with fast, single-step generation.
