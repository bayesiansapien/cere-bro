---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.142285+00:00
arxiv_id: 2611.23388
url: https://huggingface.co/papers/2611.23388
arxiv_url: https://arxiv.org/abs/2611.23388
date: 2026-11-19
---

# QDA: Closed-Loop LLM Quantization Design with Agents

Post-training quantization is the standard way to serve large language models at low cost. However, the best quantization recipe differs across models and precisions. As a result, experts must redesign it for every new model, which is time-consuming and often sub-optimal. Fortunately, an LLM agent can take over this design by refining the recipe over rounds of building and evaluating candidates, so that more rounds lead to better recipes. However, evaluating one quantized reasoning model takes tens of GPU-hours, and combining methods from different codebases means porting each to the new architecture by hand. We present QDA, a system in which an agent designs the recipe for each model and precision. To make evaluation fast, QDA scores each candidate in minutes by its output KL divergence from the original model on reasoning traces that the agent never sees, and checks promising ones with long generations to catch failures such as repetition loops. To make building fast, QDA provides a library of public PTQ methods that are compatible with one another and with new model architectures. Across four reasoning models, QDA improves accuracy over the strongest public recipe by 0.9, 1.4 and 2.2 percentage points on average at W4A16, W4A8 and W3A16, using 64 GPU-hours per search. On the 320B-parameter MoE model GLM-5.3-Flash at NVFP4 W4A4, it recovers 98.3% of the FP8 model's accuracy, against 96.9% for the best vendor checkpoint. Every QDA checkpoint also runs on existing serving kernels with no inference overhead. We will release the library, the evaluator and the harness.
