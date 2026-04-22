---
source: farmer/huggingface
farmed: 2026-04-22T00:00:00
arxiv_id: 2604.19295
url: https://huggingface.co/papers/2604.19295
arxiv_url: https://arxiv.org/abs/2604.19295
date: 2026-04-22
---

# TEMPO: Scaling Test-time Training for Large Reasoning Models

Test-time training (TTT) adapts model parameters on unlabeled test instances during inference time, which continuously extends capabilities beyond the reach of offline training. Despite initial gains, existing TTT methods for LRMs plateau quickly and do not benefit from additional test-time compute. Without external calibration, the self-generated reward signal increasingly drifts as the policy model evolves, leading to both performance plateaus and diversity collapse. We propose TEMPO, a TTT framework that interleaves policy refinement on unlabeled questions with periodic critic recalibration on a labeled dataset. By formalizing this alternating procedure through the Expectation-Maximization (EM) algorithm, we reveal that prior methods can be interpreted as incomplete variants that omit the crucial recalibration step. Reintroducing this step tightens the evidence lower bound (ELBO) and enables sustained improvement. Across diverse model families (Qwen3 and OLMO3) and reasoning tasks, TEMPO improves OLMO3-7B on AIME 2024 from 33.0% to 51.1% and Qwen3-14B from 42.3% to 65.8%, while maintaining high diversity.
