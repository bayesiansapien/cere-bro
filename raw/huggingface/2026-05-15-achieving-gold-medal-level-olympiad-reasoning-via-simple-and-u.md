---
source: farmer/huggingface
farmed: 2026-05-15T00:00:00Z
arxiv_id: "2605.13301"
url: https://huggingface.co/papers/2605.13301
arxiv_url: https://arxiv.org/abs/2605.13301
date: 2026-05-15
---

# Achieving Gold-Medal-Level Olympiad Reasoning via Simple and Unified Scaling

Recent progress in reasoning models has substantially advanced long-horizon mathematical and scientific problem solving, with several systems now reaching gold-medal-level performance on International Mathematical Olympiad (IMO) and International Physics Olympiad (IPhO) problems. This paper introduces a simple and unified recipe for converting a post-trained reasoning backbone into a rigorous olympiad-level solver. The recipe consists of three main stages: (1) Rigorous SFT using a reverse-perplexity curriculum to instill rigorous proof-search and self-checking behaviors on around 340K sub-8K-token trajectories; (2) a Two-Stage RL Pipeline with Coarse RL scaling reasoning behaviors through verifiable rewards followed by Refined RL with generative rewards, self-refinement, and experience replay; and (3) Test-Time Scaling boosting solving performance through self-verification and refinement loops. The work trains a 30B-A3B backbone model called SU-01 with 200 RL steps, achieving gold-medal-level performance on IMO 2025 (35 points), USAMO 2026 (35 points, exceeding gold line by 10 points), and IPhO 2024/2025. The model supports stable reasoning on difficult problems with trajectories exceeding 100K tokens and reaches 57.6% on IMO-ProofBench with direct generation, 70.2% with test-time scaling. The work supports a "specializable-generalist" view: with the right training and inference recipe, a broadly capable compact backbone can be driven toward expert-level proof reasoning while retaining meaningful scientific transfer.
