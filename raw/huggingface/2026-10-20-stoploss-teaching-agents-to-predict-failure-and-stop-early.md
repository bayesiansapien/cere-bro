---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.25525
url: https://huggingface.co/papers/2610.25525
arxiv_url: https://arxiv.org/abs/2610.25525
date: 2026-10-20
---

# StopLoss: Teaching Agents to Predict Failure and Stop Early

Coding agents keep working on runs that will fail verification, and asking a frontier model to watch for this is expensive in its own right. We introduce StopLoss, a small external monitor that learns failure recognition from completed trajectories and their verifier outcomes. The name is inspired by the stop-loss order in finance: StopLoss ends a run early when the run is likely to fail, which saves resources. Final outcomes label earlier local windows, so a fine-tuned language model can score the most recent tool steps in a single forward pass, and a threshold calibrated on successful runs turns that score into an abort decision without changing the executor. Trained on GPT-family SWE-rebench trajectories and evaluated on SWE-bench Verified and a SWE-bench Pro subset with GPT and Claude executors, StopLoss is compared against six general-purpose judges reading identical windows. Outcome supervision lifts failure prediction from near chance to a useful signal at the first check, at one to two orders of magnitude lower cost per check than any tested judge. This translates into savings: relative to completing every task, StopLoss lowers cost per retained solve by 4.5\% on Verified while preserving 99\% of successful runs, and by up to 31\% on the costlier Pro subset, reaching 48\% with a Qwen3-8B backbone, and in all four settings its cost per retained solve is below that of every judge policy. Outcome-trained small monitors can make failure recognition cheap enough for early stopping to pay for itself.
