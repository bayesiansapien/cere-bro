---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.935548+00:00
arxiv_id: 2609.35472
url: https://huggingface.co/papers/2609.35472
arxiv_url: https://arxiv.org/abs/2609.35472
date: 2026-09-29
---

# Why Deterministic PRM Guidance Underperforms in Discrete Diffusion Reasoning

Discrete diffusion language models (dLLMs) expose a denoised solution at every step, which makes process reward model (PRM) guidance look like a way to spend compute at test time. We show that once denoising, PRM scoring, and outcome reward model (ORM) scoring are charged in the same budget of forward passes, its deterministic form loses to a much simpler baseline. Our PRMs score intermediate denoising states and are trained on the correctness of the final answer. On Dream-v0-Instruct-7B with 8 candidates per GSM8K problem, keeping the candidate with the highest PRM score at every scoring step reaches 65.18%, while independent sampling plus an ORM reranker trained for the task reaches 75.13%. The gap grows to 12.69 percentage points (pp) with 32 candidates, and is 9.85 pp on MATH and 12.16 pp on MBPP. We trace it to two separable failures. First, guidance prunes on a weak signal: on GSM8K, PRM ROC-AUC falls from 0.77 to 0.54 as the mask ratio rises, a decay that persists when states are relabeled with fresh rollouts, and pruning lowers the best accuracy reachable from the candidate pool from 81.05% for independent samples to 67.30%. Second, on GSM8K and MATH, the PRM is a poor final judge: a sequential Monte Carlo sampler at the same budget restores that ceiling to 77.89%, yet selecting with the PRM gives 65.48%, on par with deterministic guidance, while a PRM retrained on final states matches the ORM on identical candidates. MBPP separates the two: there the PRM reaches 65.47% when reranking finished programs, on par with the ORM, but 50.88% when it guides denoising. The results point to two targets for dLLM guidance: keep correct partial solutions alive through early denoising, and leave the final choice to a verifier trained on final states. We release the corpus of denoising states with outcome labels and evaluation toolkit for reproducible comparisons at matched compute.
