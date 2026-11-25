---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.933177+00:00
arxiv_id: 2611.26103
url: https://huggingface.co/papers/2611.26103
arxiv_url: https://arxiv.org/abs/2611.26103
date: 2026-11-24
---

# UniVEP: Unifying Velocity and Endpoint Prediction for Robot Manipulation

Flow-matching robot policies usually use one prediction target throughout action generation, even though recovering actions from noise and polishing nearly clean actions bring different challenges. We systematically compare velocity prediction (V), endpoint prediction (X), and velocity-weighted endpoint prediction (X--V) across multiple robot policies, benchmarks, and inference budgets. On StarVLA and LiLa-WAM, X--V works best for few-step generation, while V gains more from iterative refinement. We further uncover their complementary strengths across noise levels: clean actions have concentrated covariance spectra, endpoint predictions stay more stable under high noise, and velocity predictions offer more accurate corrections near clean actions. Inspired by these findings, we introduce UniVEP, which learns both prediction targets together with consistency supervision and switches from endpoint recovery to velocity refinement as noise drops. Each step only needs one network run, and joint training also boosts single-step endpoint generation. Tests on simulated and real-world manipulation show better success rates and efficiency. On RoboTwin, UniVEP hits 61.36% success with one StarVLA run, beating the best single-target baseline at sixteen runs (59.96%). With LiLa-WAM, two runs outperform the best sixteen-step single-target baseline and cut inference latency by 77.1%.
