---
source: farmer/huggingface
farmed: 2026-09-15T10:58:02.142912
arxiv_id: 2609.13356
url: https://huggingface.co/papers/2609.13356
arxiv_url: https://arxiv.org/abs/2609.13356
date: 2026-09-15
---

# ZGCM-1: A Fully Open and Extremely Efficient Foundation Model for Math and Agentic Search

In this work, we present ZGCM-1, a fully open 7B dense foundation model trained from scratch with extreme data, system, and algorithmic efficiency. ZGCM-1 is founded on a core premise: compact models cannot passively memorize the open web, but can overcome parametric capacity limits by coupling deliberate internal thinking with active external tool use. To support this paradigm across a 256K context, we develop an end-to-end, high-efficiency open training recipe: Architecture & System Co-design: interleaved gated sliding-window and full attention, and a stable FP8 Muon optimizer; Progressive Curriculum & MDP Mid-Training: context scaling across 16K, 64K, and 256K, and the reformulation of interaction traces into Markov Decision Processes. Furthermore, we establish an AI-native R&D workflow where agent swarms autonomously manage cluster operations, data curation, and rapid diagnostic evaluation. Extensive evaluations show that ZGCM-1-7B is competitive across 7B model family on general benchmarks. On several challenging mathematical reasoning and agentic search suites, it remains competitive with frontier models orders of magnitude larger, such as Qwen3-235B-A22B and GLM-5.1. We also show that our pre-training design offers a ~4.2x efficiency improvement in 16K pre-training time-to-loss. Across the full development lifecycle, we distill eight actionable empirical findings-spanning architectural scaling, SFT quality pruning, long-context generalization, and agentic co-training dynamics. To facilitate community research, we open-source model weights from the pre-training, mid-training, and post-training stages, intermediate checkpoints, training code, per-stage data and data recipes, and W&B logs.
