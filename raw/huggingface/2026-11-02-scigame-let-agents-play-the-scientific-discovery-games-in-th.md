---
source: farmer/huggingface
farmed: 2026-11-03T14:58:56.501306+05:30
arxiv_id: 2610.37919
url: https://huggingface.co/papers/2610.37919
arxiv_url: https://arxiv.org/abs/2610.37919
date: 2026-11-02
---

# SciGame: Let Agents Play the Scientific Discovery Games in the Real and Counterfactual World

Large language model agents are increasingly used for scientific discovery. However, existing benchmarks mix law inference with programming, score data fitting instead of prediction on unseen inputs, and do not separate empirical evidence from pretrained priors. We introduce SciGame, a controlled benchmark that converts scientific literature into structured scientific cards. Each card yields a pair of Original and dimensionally consistent Counterfactual environments with the same task interface. SciGame contains a Historical collection of canonical laws and a live Temporal collection curated from papers published after model knowledge cutoffs. It evaluates agents in candidate-guided Identification and open-ended Discovery settings. Each setting runs under Prior-only, Fixed, and Adaptive protocols. Experiments on five frontier models yield three findings. First, familiar priors hurt performance once the governing relation is altered. Second, adaptive experimentation helps the strongest models but harms weaker ones under limited budgets. Third, good explanations can hide quantitative failures. Recovering the exact symbolic form remains the main bottleneck, even when agents interpret evidence correctly. Current agents can investigate systems actively, but inducing exact laws in unfamiliar settings remains an open challenge.
