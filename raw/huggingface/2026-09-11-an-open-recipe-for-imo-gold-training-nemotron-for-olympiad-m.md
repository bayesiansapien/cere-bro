---
source: farmer/huggingface
farmed: 2026-09-11T21:57:41.002444
arxiv_id: 2609.10712
url: https://huggingface.co/papers/2609.10712
arxiv_url: https://arxiv.org/abs/2609.10712
date: 2026-09-11
---

# An Open Recipe for IMO Gold: Training Nemotron for Olympiad Mathematics

We study how model post-training and test-time inference design affect natural-language proof generation for hard olympiad mathematics. Starting from Nemotron 3 Ultra, we train two specialist checkpoints using supervised fine-tuning and reinforcement learning, and evaluate checkpoint choice, verification, and refinement. Based on these findings, we present an open-model test-time-compute pipeline. The system operates entirely in natural language, with no formal prover, external tools, or internet access. Three Nemotron 3 Ultra checkpoints - the general-availability model and two post-trained specialists - power an iterative search that generates, verifies, and refines candidate proofs; a separate high-compute stage then selects each final submission. The system scored 30 out of 42 points at IMO 2026, reaching the gold-medal threshold. We release the two post-trained checkpoints as well as the training data, the training and inference code, the submitted solutions, and Nemotron-IMO-Bench, a new benchmark of 200 novel olympiad-level problems.
