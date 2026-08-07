---
source: farmer/huggingface
farmed: 2026-08-07T06:50:52.124211+00:00
arxiv_id: 2608.06352
url: https://huggingface.co/papers/2608.06352
arxiv_url: https://arxiv.org/abs/2608.06352
date: 2026-08-07
---

# CalibForge: Adversarial Solver Calibration for Scaling Learnable Terminal Tasks

Training terminal agents requires executable and verifiable tasks that are not merely solvable, but appropriately challenging for learning. Executable validation establishes feasibility, yet does not reveal how a task behaves relative to a given solver setting. In this paper, we present CalibForge, an autonomous terminal-task synthesis system that uses verified solver behavior to revise candidate tasks through adversarial solver calibration. Multi-solver calibration targets disagreement within a heterogeneous solver pool, whereas contrastive solver calibration targets a designated strong-pass/weak-fail relation; both operationalize a solver-relative learnable zone anchored in demonstrated solvability. Using CalibForge, we construct 5,431 calibrated terminal tasks. Our ablations show that both strategies yield more effective supervision than authoring and validation alone or ordinary single-solver feedback. Models trained on the full collection achieve 32.58% and 47.57% on Terminal-Bench 2.0. The largest improvements over the corresponding base model reach 24.71 percentage points on Terminal-Bench 2.0, 27.68 points on SWE-bench Pro, and 30.04 points on Doc2Repo. Together, these results support solver-relative learnability as a practical target for constructing effective and transferable agent training data.
