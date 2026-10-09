---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.312752+05:30
arxiv_id: 2605.09742
url: https://huggingface.co/papers/2605.09742
arxiv_url: https://arxiv.org/abs/2605.09742
date: 2026-10-08
---

# TIDES: Implicit Time-Awareness in Selective State Space Models

Selective state space models (SSMs), such as Mamba, achieve strong per-token expressivity by making the time discretization step TildeΔ a learned function of the input. However, in doing so, TildeΔ no longer equals the physical time gap Δ between consecutive observations, limiting the ability of these models to handle irregular time series. Continuous time SSMs, such as S5, keep TildeΔequivΔ and therefore handle irregular timestamps natively, but their dynamics remain linear time invariant (LTI), limiting per token expressivity. We propose TIDES, a selective SSM variant that reconciles selective and continuous architectures by moving input dependence off the step size and onto the diagonal state matrix. As a result, TildeΔequivΔ as in S5, allowing the model to handle irregular timestamps natively without sacrificing the per-token expressivity that makes selective SSMs effective. We show this on a novel Fading Flash experimental benchmark, a compact controlled diagnostic for sequence models that jointly tests input dependence and extrapolation to out-of-distribution Δ values, and isolates the distinct failure modes of current state-of-the-art architectures that TIDES avoids by construction. On large-scale benchmarks, TIDES sets the new best average rank on UEA time series classification and the Physiome ODE regression benchmark, and matches or exceeds the reference baseline model on 6 of 8 natively irregular datasets from astronomy, agriculture, neuromorphic sensing, and climate events. Code available at: https://github.com/TaylanSoydan/TIDES.
