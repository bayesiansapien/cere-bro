---
source: farmer/huggingface
farmed: 2026-10-06T11:30:06.338949+05:30
arxiv_id: 2609.33463
url: https://huggingface.co/papers/2609.33463
arxiv_url: https://arxiv.org/abs/2609.33463
date: 2026-10-05
---

# Rethinking Token Reweighting for SFT: Suppress, Reverse, and Extrapolate Learned Features

Supervised fine-tuning (SFT) learns most aggressively from tokens that the model deems least likely. This helps acquire new behaviors, but also amplifies noisy or conflicting supervision and can overwrite useful pretrained knowledge. Through a unified policy-loss view, we revisit existing token-reweighting methods and show that they assign nonnegative coefficients to demonstrated tokens. Consequently, they can suppress or amplify supervised updates, but cannot reverse harmful features once learned. Moreover, larger training weights do not amount to feature extrapolation, since they change the optimization trajectory rather than scale a fixed SFT direction. We argue that reversal and extrapolation require a stable reference frame defined by a fixed SFT delta. Motivated by this, we propose SCALE (Selective Control of Adaptation via Local Entropy), an entropy-guided adaptation-strength-control method that freezes the pretrained model and the SFT delta and learns bounded token- and module-specific gates by minimizing predictive entropy alone. These gates suppress, reverse, or extrapolate frozen SFT features according to their alignment with entropy reduction. Across Qwen2.5-Math-1.5B, Qwen2.5-Math-7B, and Qwen3-4B-Base, SCALE achieves mathematical-reasoning averages of 37.84, 43.60, and 36.57, exceeding the strongest corresponding baselines while remaining competitive on general-retention benchmarks. It also attains the best average code-generation performance across HumanEval, HumanEval+, and MBPP for all three models. These results suggest that effective SFT correction can benefit from controlling how already learned residuals are used, rather than only modifying how they are learned.
