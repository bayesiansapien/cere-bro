---
source: farmer/huggingface
farmed: 2026-08-25T14:22:16.352902
arxiv_id: 2608.20169
url: https://huggingface.co/papers/2608.20169
arxiv_url: https://arxiv.org/abs/2608.20169
date: 2026-08-25
upvotes: 3
authors: ["Atsuyuki Miyai", "Kiyoharu Aizawa", "Toshihiko Yamasaki"]
---

# Task-CoEvolve: Efficient Harness Optimization via Adaptive Validation Task Selection

**Upvotes:** 3
**Authors:** Atsuyuki Miyai, Kiyoharu Aizawa, Toshihiko Yamasaki

We present a novel approach to efficient LLM harness optimization through adaptive validation task selection. Harness optimization iteratively rewrites the harness code based on validation performance, enabling substantial performance gains without updating the underlying model weights. Existing approaches, however, evaluate a fixed validation set in full at every iteration, incurring substantial evaluation costs even on tasks that become less discriminative as the harness evolves. We propose Task-CoEvolve, which co-evolves the validation tasks with the harness by addressing two challenges: selecting informative tasks and estimating full-set performance from partial evaluations. Task-CoEvolve builds on the observation that tasks on which candidate harnesses disagree are more informative for distinguishing among them than tasks that are consistently solved or failed. It uses variance-weighted sampling based on past outcomes to focus evaluation on tasks near the capability frontier, with the sampling distribution adapting as the harness evolves. It then estimates full-set scores from the sampled tasks by accounting for their sampling probabilities, enabling consistent comparisons across iterations despite evaluating different subsets. Experiments on online text classification and Terminal-Bench 2.1 show that Task-CoEvolve consistently outperforms subset-based baselines and matches the final performance of full-set search while reducing the number of evaluations during optimization by 80%. Code will be released at https://github.com/Agent4Science-UTokyo/Task-CoEvolve.
