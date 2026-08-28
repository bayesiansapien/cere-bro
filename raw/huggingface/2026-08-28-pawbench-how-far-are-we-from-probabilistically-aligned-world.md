---
source: farmer/huggingface
farmed: 2026-08-28T14:50:07.734667+05:30
arxiv_id: 2608.27345
url: https://huggingface.co/papers/2608.27345
arxiv_url: https://arxiv.org/abs/2608.27345
date: 2026-08-28
---

# PAWBench: How Far Are We from Probabilistically Aligned World Modeling?

Recent video generation models are increasingly framed as world models. Many physical processes can unfold in more than one valid way. Therefore, a world model should reproduce not only a plausible trajectory, but also the distribution of possible behaviors under the same initial observation and action. We call this distribution-level requirement probabilistic alignment. However, existing evaluations largely assess individual-video plausibility and do not test whether repeated generations recover the correct distribution. This raises a central question: how far are current video generators from probabilistically aligned world modeling? To answer it, we formalize probabilistic alignment as a distributional criterion for world models and introduce PAWBench, a benchmark for evaluating video generators as stochastic samplers of world dynamics. We further introduce PAWEval, an outcome-level protocol that converts repeated video rollouts into empirical distributions over possible physical behaviors. Across 50 scenarios and eleven current systems, no model consistently matches the reference probabilities while recovering the range of valid behaviors. Having established this gap, we test whether language prompts, initial noise sampling, or model training can reshape the model's predictive distribution. We believe our work can serve as a foundation for future efforts to move towards probabilistically aligned world modeling.
