---
source: farmer/huggingface
farmed: 2026-05-19T09:55:00.432604+00:00
arxiv_id: 2605.17283
url: https://huggingface.co/papers/2605.17283
arxiv_url: https://arxiv.org/abs/2605.17283
date: 2026-05-19
---

# OProver: A Unified Framework for Agentic Formal Theorem Proving

Recent progress in formal theorem proving has benefited from large-scale proof generation and verifier-aware training, but agentic proving is rarely integrated into prover training, appearing only at inference time. We present OProver, a unified framework for agentic formal theorem proving in Lean 4, in which failed proof attempts are iteratively revised using retrieved compiler verified proofs and Lean compiler feedback. OProver is trained through continued pretraining followed by iterative post-training: each iteration runs agentic proving, indexes newly verified proofs into OProofs and the retrieval memory, uses repair trajectories as SFT data, and uses unresolved hard cases for RL. OProofs is built from public Lean resources, large-scale proof synthesis, and agentic proving traces, containing 1.77M Lean statements, 6.86M compiler-verified proofs, and serialized trajectories with retrieved context, failed attempts, feedback, and repairs. Across five benchmarks, OProver-32B attains the best Pass@32 on MiniF2F (93.3%), ProverBench (58.2%), and PutnamBench (11.3%), and ranks second on MathOlympiad (22.8%) and ProofNet (33.2%) more top placements than any prior open-weight whole-proof prover.
