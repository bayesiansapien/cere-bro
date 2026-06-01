---
source: farmer/huggingface
farmed: 2026-06-01T09:02:45Z
arxiv_id: 2605.29447
url: https://huggingface.co/papers/2605.29447
arxiv_url: https://arxiv.org/abs/2605.29447
date: 2026-06-01
---

# Recovering Policy-Induced Errors: Benchmarking and Trajectory Synthesis for Robust GUI Agents

While GUI agents have advanced rapidly, they often lack the robustness to recover from their own errors, hindering real-world deployment. To bridge this gap at both the evaluation and data levels, we introduce GUI-RobustEval and propose Robustness-driven Trajectory Synthesis. GUI-RobustEval contains 1,216 executable test cases that systematically measure error recovery capabilities across a broad and realistic spectrum of error modes. At the data level, RoTS is a scalable synthesis framework that creates 800k high-quality data via a tree-based pipeline that proactively discovers diverse error modes and synthesizes corresponding recovery steps. Our two models, RoTS-7B and RoTS-32B, fine-tuned on our dataset, both demonstrate significant gains on GUI-RobustEval and traditional GUI benchmarks. Notably, RoTS-32B achieves state-of-the-art performance on OSWorld, with a 47.4% success rate and a 33.8% All-Pass@4 score, suggesting that improved long-horizon error recovery ability contributes to both robustness and overall performance.
